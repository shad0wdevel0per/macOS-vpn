import socket
import ssl
import threading

def handle_client(conn):
    try:
        request = conn.recv(8192)

        host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_socket.connect(("www.google.com", 80))  # Proxy fixo
        host_socket.sendall(request)

        while True:
            data = host_socket.recv(8192)
            if not data:
                break
            conn.sendall(data)

        host_socket.close()
    finally:
        conn.close()

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

sock = socket.socket()
sock.bind(('0.0.0.0', 443))  # Porta padrão HTTPS
sock.listen(5)

print("[🔐] Servidor proxy escutando...")

while True:
    client, _ = sock.accept()
    conn = context.wrap_socket(client, server_side=True)
    threading.Thread(target=handle_client, args=(conn,)).start()