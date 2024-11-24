class CL_Model:
    def __init__(self):
        self.ip_address = ""
        self.port = ""

    def set_ip_address(self, ip):
        self.ip_address = ip

    def set_port(self, port):
        self.port = port

    def get_ip_address(self):
        return self.ip_address

    def get_port(self):
        return self.port