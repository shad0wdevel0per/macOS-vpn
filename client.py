import socket
import ssl
import requests

# Função para obter o IP público do servidor remoto automaticamente
def get_remote_ip():
    try:
        # Consulta o IP público da máquina (pode ser sua VPS ou outro servidor)
        ip = requests.get('https://api.ipify.org').text
        return ip
    except requests.RequestException:
        print("[❌] Erro ao obter o IP remoto automaticamente.")
        return None

# Descobre automaticamente o IP remoto
REMOTE_IP = get_remote_ip()
if REMOTE_IP is None:
    print("[❌] Não foi possível obter o IP remoto automaticamente!")
    exit(1)

REMOTE_PORT = 443  # Porta HTTPS padrão

# Criação do contexto SSL
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Conexão com o servidor remoto via SSL
with socket.create_connection((REMOTE_IP, REMOTE_PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=REMOTE_IP) as secure_sock:
        print(f"[🔌] Conectado ao túnel seguro com o IP remoto: {REMOTE_IP}")

        # Exemplo: uma requisição HTTP (GET)
        request = (
            "GET / HTTP/1.1\r\n"
            "Host: www.google.com\r\n"
            "Connection: close\r\n\r\n"
        )
        secure_sock.sendall(request.encode())

        while True:
            data = secure_sock.recv(8192)
            if not data:
                break
            print(data.decode(errors='ignore'))