import socket
import sys
import crypto_utils

# Configuration
HOST = sys.argv[1]  # The server's hostname or IP must match server
PORT = 65432  # The port used by the server must match server

def connect_to_server():
    try:
        # Create a socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((HOST, PORT))
            print(f'Connected to server at {HOST}:{PORT}')

            while True:
                # Get user input
                message = input('Enter message to send (or "exit" to quit): ')
                if message.lower() == 'exit':
                    print('Exiting...')
                    break
                else:
                    encrypted_message = crypto_utils.encrypt_data(message)
                    s.sendall(encrypted_message.encode('utf-8'))
                    # Receive the response from the server
                    data = s.recv(1024)
                    decrypted_data = crypto_utils.decrypt_data(data.decode('utf-8'))
                    print(f'Received from server: {decrypted_data}')
    except Exception as e:
        print(f'Error connecting to server: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python client.py <server_ip>")
        sys.exit(1)
    connect_to_server()  # Start the client

'''
we need to monitor the traffic sent. wireshark was being weird on windows. we should test it on kali.


'''
