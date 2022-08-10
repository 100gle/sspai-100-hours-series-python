# server.py

import logging
import socketserver
import sys

logging.basicConfig(
    level=logging.INFO,
    format="[{asctime}] [{levelname}] [{module}] - {message}",
    style="{",
)
log = logging.getLogger("server")


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        request = self.request.recv(1024).decode().strip()
        log.info(f"Get request:\n{request}")
        header = "HTTP/1.0 200 OK\r\n\n"
        content = """
        <div style="text-align: center;">
            <h1>Hello, World</h1>
            <p>You got it!</p>
        </div>
        """.strip()
        response = header + content
        self.request.sendall(response.encode())


def main():
    HOST, PORT = "127.0.0.1", 8000
    srv = socketserver.TCPServer(
        server_address=(HOST, PORT),
        RequestHandlerClass=TCPHandler,
    )

    log.info(f"Listening on http://{HOST}:{PORT}...")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        log.info("Server stopped")
        srv.server_close()
        srv.shutdown()
        log.info("Bye...")
        sys.exit(0)


if __name__ == '__main__':
    main()
