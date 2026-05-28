#!/usr/bin/env python3
"""
Servidor local para o Monitor de Aeronaves (EWS).

Para que serve:
  O navegador bloqueia (CORS) a busca direta dos dados do EWS a partir da
  sua pagina. Este script roda no seu computador, busca os dados pelo lado
  do servidor (onde NAO existe CORS) e os entrega para a pagina. Tambem
  serve o proprio arquivo aircraft-monitor.html.

Como usar (na pasta onde estao este arquivo e o aircraft-monitor.html):
  python ews-proxy.py
  (no Windows, se "python" nao funcionar, use:  py ews-proxy.py)

Depois abra no navegador:
  http://localhost:8000/aircraft-monitor.html

Para parar: tecle Ctrl+C nesta janela.
"""

import gzip
import http.server
import socketserver
import ssl
import urllib.request
import urllib.error

PORT = 8000

# Em redes corporativas, o firewall costuma interceptar conexoes HTTPS e o
# Python falha ao validar o certificado (CERTIFICATE_VERIFY_FAILED). Como aqui
# buscamos apenas dados PUBLICOS e somente leitura, desativamos a verificacao
# para que o download funcione mesmo atras desse tipo de rede.
SSL_CONTEXT = ssl.create_default_context()
SSL_CONTEXT.check_hostname = False
SSL_CONTEXT.verify_mode = ssl.CERT_NONE

# A pagina pede /data/<arquivo>.json e o proxy tenta estas origens, em ordem,
# ate uma responder com JSON valido. Se a URL do EWS mudar, ajuste aqui.
UPSTREAMS = [
    "https://pub-49bb6a6f314c47be9b481c25e5f6ca9e.r2.dev/",
    "https://ews.kylemcdonald.net/",
]


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/data/"):
            name = self.path[len("/data/"):].split("?")[0].lstrip("/")
            self.proxy(name)
        else:
            super().do_GET()

    def proxy(self, name):
        for base in UPSTREAMS:
            url = base + name
            try:
                # Cloudflare pode devolver 503 para pedidos que nao parecem um
                # navegador. Por isso enviamos cabecalhos de navegador comum.
                req = urllib.request.Request(url, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36",
                    "Accept": "application/json, text/plain, */*",
                })
                with urllib.request.urlopen(req, timeout=20, context=SSL_CONTEXT) as resp:
                    body = resp.read()
                # Se vier compactado (gzip), descompacta antes de seguir.
                if body[:2] == b"\x1f\x8b":
                    body = gzip.decompress(body)
                # Alguns enderecos respondem "200" mas devolvem a pagina HTML do
                # site (comeca com "<") em vez do JSON. So aceitamos JSON de verdade.
                if not body.lstrip()[:1] in (b"{", b"["):
                    print(f"[ignora]  {url}  ->  resposta nao e JSON (provavel HTML)")
                    continue
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(body)
                print(f"[ok]      {name}  <-  {url}  ({len(body)} bytes)")
                return
            except Exception as e:
                print(f"[falhou]  {url}  ->  {e}")
        self.send_response(502)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b'{"error":"nao foi possivel buscar os dados do EWS"}')
        print(f"[erro]    nenhuma origem respondeu para {name}")


def main():
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", PORT), Handler) as httpd:
        print("=" * 56)
        print(" Servidor do Monitor de Aeronaves pronto.")
        print(f" Abra:  http://localhost:{PORT}/aircraft-monitor.html")
        print(" Para parar: Ctrl+C")
        print("=" * 56)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor encerrado.")


if __name__ == "__main__":
    main()
