from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


def main() -> None:
    server = ThreadingHTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    print('Serving on http://127.0.0.1:8000')
    server.serve_forever()


if __name__ == '__main__':
    main()