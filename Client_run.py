import socket
from XL_Chucnang.CRUDConfig import read_config_server, update_config
from XL_Chucnang.Connection import check_ip_address_valid, check_port_valid


import Client.CL_app_process
import Client.CL_services_process
import Client.CL_shutdown_reset
import Client.CL_monitor
import Client.CL_keylogger
import Client.CL_del_copy


def main():
    client_ip = socket.gethostbyname(socket.gethostname())
    client_port = 6789
    print("Client ")
    update_config("config.json", client_ip=client_ip, client_port=client_port)

    while True:
        server_ip = input("Dien dia chi IP cua Server: ")
        if not check_ip_address_valid(server_ip):
            print("IP khong hop le. Vui long dien lai.")
            continue

        sever_port = int(input("Dien so port: "))
        if not check_port_valid(sever_port):
            print("Port khong hop le. Vui long dien lai.")
            continue

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, sever_port))
            print(f"Ket noi server co dia chi {server_ip}:{sever_port} thanh cong")
            menu_chinh(client_socket)
            break
        except socket.error as e:
            print(f"Ket noi khong thanh cong: {e}. Vui long kiem tra server co dang chay khong va IP, port co dung khong.")
            client_socket.close()
            continue

    # Lưu đỉa chị server và port và config.json
    update_config("config.json", server_ip = server_ip, server_port = sever_port)


def menu_chinh(client_socket):
    while True:
        print("\n- MENU CHINH -")
        print("1. List / Start / Stop cac Applications dang chay SERVER")
        print("2. List / Start / Stop cac Services dang chay SERVER")
        print("3. Shutdown / Reset may SERVER")
        print("4. Xem man hinh hien thoi cua may SERVER")
        print("5. Khoa / Bat phim nhan (keylogger) o may SERVER")
        print("6. Xoa files ; Copy files tu may SERVER")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            Client.CL_app_process.app_process(client_socket)
        elif choice == "2":
            Client.CL_services_process.services_process(client_socket)
        elif choice == "3":
            Client.CL_shutdown_reset.shutdown_reset(client_socket)
        elif choice == "4":
            Client.CL_monitor.monitor(client_socket)
            while True:
                try:
                    server_ip, server_port = read_config_server("config.json")
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect((server_ip, server_port))
                    break
                except socket.error as e:
                    print(f"Ket noi khong thanh cong: {e}. Vui long kiem tra server co dang chay khong va IP, port co dung khong.")
                    client_socket.close()
                    continue
            menu_chinh(client_socket)

        elif choice == "5":
            Client.CL_keylogger.bat_tat_key_logger(client_socket)
        elif choice == "6":
            Client.CL_del_copy.del_copy(client_socket)
        elif choice == "0":
            client_socket.close()
            print("Disconnected from server.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
