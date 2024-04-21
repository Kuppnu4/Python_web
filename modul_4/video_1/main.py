from jinja2 import Environment, FileSystemLoader
import urllib.parse
import mimetypes
import logging
import json
import socket
from pathlib import Path
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler


BASE_DIR = Path()
BUFFER_SIZE = 1024
HTTP_PORT = 8080
HTTP_HOST = '0.0.0.0'
SOCKET_PORT = 4000
SOCKET_HOST = '127.0.0.1'

jinja = Environment(loader=FileSystemLoader('templates'))


class GoitFramework(BaseHTTPRequestHandler):

    def do_GET(self):
        router = urllib.parse.urlparse(self.path)
        print(router.query)
        match router.path:
            case '/':
                self.send_html('index.html')
            case '/contact':
                self.send_html('contact.html')
            case '/blog':
                self.render_template('blog.jinja')
            case _:
                file = Path(router.path[1:])
                if file.exists():
                    self.send_static(file)
                else:
                    self.send_html('404.html', 404)

    def send_static(self, filename, status_code=200):
        self.send_response(status_code)
        mime_type, *_ = mimetypes.guess_type(filename)
        if mime_type:
            self.send_header('Content-Type', mime_type)
        else:
            self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

    def render_template(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        with open('storage/db.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        template = jinja.get_template(filename)
        message = 'Hello Aleks'
        html = template.render(blogs=data, message=message)
        self.wfile.write(html.encode())

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

    def do_POST(self):
        size = self.headers.get('Content-Length')
        data = self.rfile.read(int(size))

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(data, (SOCKET_HOST, SOCKET_PORT))
        client_socket.close()

        self.send_response(302)
        self.send_header('Location', '/contact')
        self.end_headers()


def save_data_from_form(data):
    parse_data = urllib.parse.unquote_plus(data.decode())

    try:
        parse_dict = {key: value for key, value in [el.split('=') for el in parse_data.split('&')]}
        with open('data/data.json', 'w', encoding='utf-8') as file:
            json.dump(parse_dict, file, ensure_ascii=False, indent=4)
    except ValueError as err:
        logging.error(err)
    except OSError as err:
        logging.error(err)


def run_socket_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    logging.info('Starting socket server')
    try:
        while True:
            msg, address = server_socket.recvfrom(BUFFER_SIZE)
            logging.info(f'Socket received {address}: {msg}')
            save_data_from_form(msg)
    except KeyboardInterrupt:
        server_socket.close()


def run_http_server(host, port):
    address =(host, port)
    http_server = HTTPServer(address, GoitFramework)
    logging.info('Starting http server')
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    server = Thread(target=run_http_server, args=(HTTP_HOST, HTTP_PORT))
    server.start()

    server_socket = Thread(target=run_socket_server, args=(SOCKET_HOST, SOCKET_PORT))
    server_socket.start()

