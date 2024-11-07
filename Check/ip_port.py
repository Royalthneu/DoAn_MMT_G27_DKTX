import socket

def check_ip_address_valid(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False
    
def check_port_valid(port):
    if 0 < port <= 65535:
        return True
    else:
        return False

def input_ip(server_ip):
    ip = input("Enter the server IP address: ")
    if not check_ip_address_valid(ip):
        print("Invalid server IP address. Please try again.")
        
def input_port(port):
    ip = input("Enter Port: ")
    if not check_port_valid(port):
        print("Invalid port. Please try again.")
              
def server_socket_bind_ip_port(server_ip, port):
    if check_ip_address_valid(server_ip) and check_port_valid(port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, port))
        server_socket.listen(1) #số lượng kết nối trong 1 thời điểm
    else:
        print ("IP address or Port not open.")
        


            

