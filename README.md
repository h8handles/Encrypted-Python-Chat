# Over The Wire Encrypted Chat

This is a simple encrypted chat application that allows users to communicate securely over the internet.
The application uses end-to-end encryption to ensure that only the intended recipients can read the messages over the network.
Uses AES Cipher Block Chaining (CBC)

## Features

- End-to-end encryption (AES)
- User authentication (work in progress)
- Group chat support (work in progress)
- gui (work in progress)


## Requirements
- pycryptodome
- sys
- socket
- threadding
- flask (for the GUI)


### Usage Server
`python3 server.py`

### Usage Client
`python3 client.py <Server-IP>`



### Client Server Communication
  ![image](https://github.com/user-attachments/assets/7df857df-64d5-47be-9cc9-7e5666e820a8)



### Wireshark analysis of encrypted traffic
![image](https://github.com/user-attachments/assets/43d57dad-73c1-4445-aa4b-9ed6689da6da)
