# VPN Proxy Seguro com Python

Este projeto oferece uma **VPN simples** usando **Python 3**, que cria um **túnel criptografado** entre seu dispositivo e um servidor remoto, **mascarando seu IP** e **protegendo seu tráfego** na internet. É ideal para quem deseja maior segurança e privacidade ao navegar na web.

---

## 🚀 **Sumário**

- [Visão Geral](#-visão-geral)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-Requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração do Servidor](#-configuração-do-servidor)
- [Configuração do Cliente](#-configuração-do-cliente)
- [Como Usar](#-como-usar)
- [Segurança e Considerações](#-segurança-e-considerações)
- [Licença](#-licença)

---

## 📖 **Visão Geral**

Este projeto permite que você crie um **proxy seguro** com **criptografia SSL/TLS** para proteger o tráfego entre o cliente e o servidor. Ele permite:

- **Criptografia do tráfego** para proteger seus dados.
- **Mascaramento do seu IP** real, garantindo maior privacidade.
- **Túnel SSL** simples de configurar, com baixo overhead de processamento.

O projeto usa **Python 3** para criar o servidor e o cliente de forma simples e eficiente, sendo ideal para quem deseja aprender sobre redes, criptografia e proxy.

---

## 🛠️ **Tecnologias Utilizadas**

- **Python 3**: Linguagem de programação para criação do servidor e cliente.
- **SSL/TLS**: Para criptografar a comunicação.
- **Socket**: Para comunicação entre o cliente e o servidor.
- **Requests**: Para obter o IP público da máquina (no cliente).
- **OpenSSL**: Para gerar certificados SSL/TLS.

---

## 🧑‍💻 **Pré-Requisitos**

Antes de executar este projeto, você precisa garantir que tenha as seguintes ferramentas instaladas:

1. **Python 3** (versão 3.6 ou superior)
   - Se não tiver, instale o Python 3 em [python.org](https://www.python.org/downloads/).
   
2. **Pip3** (gerenciador de pacotes Python)
   - Pip é geralmente instalado junto com o Python, mas se necessário, instale-o [aqui](https://pip.pypa.io/en/stable/installation/).

3. **Requests** (biblioteca para realizar requisições HTTP):
   - Instale via pip3:
     ```bash
     pip3 install requests
     ```

---

## 🛠️ **Instalação**

1. **Clone o repositório:**

   Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu_usuario/vpn_proxy.git
   cd vpn_proxy
   pip3 install requests
   openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
   ```
