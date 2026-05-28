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

import http.server
import socketserver
import urllib.request
import urllib.error

PORT = 8000

# A pagina pede /data/<arquivo>.json e o proxy tenta estas origens, em ordem,
# ate uma responder com sucesso. Se a URL do EWS mudar, ajuste aqui.
UPSTREAMS = [
    "https://ews.kylemcdonald.net/",
    "https://pub-49bb6a6f314c47be9b481c25e5f6ca9e.r2.dev/",
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
                req = urllib.request.Request(
                    url, headers={"User-Agent": "ews-monitor-local"}
                )
                with urllib.request.urlopen(req, timeout=20) as resp:
                    body = resp.read()
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
