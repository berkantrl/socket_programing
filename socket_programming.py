import socket 

#192.168.1.109 metasploitable 2

port_list = []
banner_list = []


for port in range(1,25):
    try:
    
        soket = socket.socket()
        soket.connect(("192.168.1.109",port))
        
        print ("[+]Port:",port)
        banner = soket.recv(1024)
        print (banner)
        
        banner_list.append(banner)
        port_list.append(port)

        socket.close()
        print ("-"*10)
        if "SSH" in str(banner):
            print ("This system could be linux or network device")

    except:

        pass

print (port_list)
print (banner_list)