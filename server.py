import socket
import crypto_utils 

# Configuration
HOST = '0.0.0.0'  # Listen on all interfaces you can change this
PORT = 65432  # The port used by the server you can also change this

def handle_client(conn, addr):
    print(f'Connected by {addr}')
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            decrypted_message = crypto_utils.decrypt_data(data.decode('utf-8'))
            print(f'Received from client: {decrypted_message}')
            response = f'Server received: {decrypted_message}'
            encrypted_response = crypto_utils.encrypt_data(response)
            conn.sendall(encrypted_response.encode('utf-8'))

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Server listening on {HOST}:{PORT}')
        while True:
            conn, addr = s.accept()
            handle_client(conn, addr)

if __name__ == '__main__':
    start_server()  # Start the server

