from Xuly_Chucnang.KetNoi_GiaoTiep import send_command, receive_response

def shutdown_reset(client_socket):   
    while True:
        print("\n-- List / Start / Stop cac Services dang chay SERVER --")
        print("1. Shutdown server")
        print("2. Reset server")  
        print("0. Quay lai menu chinh")
            
        choice = input("Dien lua chon: ")
    
        if choice == '1':
            confirmation = input("Ban co muon tat may Server khong (y/n): ").strip().lower()
            if confirmation == 'y':
                send_command(client_socket, "SHUTDOWN_SERVER")   
                print(receive_response(client_socket))
            else:
                print("Khong Shutdown may Server.")
        elif choice == '2':
            confirmation = input("Ban co muon tat may Server khong (y/n): ").strip().lower()
            if confirmation == 'y':
                send_command(client_socket, "RESET_SERVER")    
                print(receive_response(client_socket))
            else:
                print("Khong Shutdown may Server.")              
        elif choice == '0':
            break
        else:
            print("Chon khong dung. Chon lai.")


