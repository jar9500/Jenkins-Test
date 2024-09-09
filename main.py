from netmiko import Netmiko
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoAuthenticationException
from netmiko.ssh_exception import NetmikoTimeoutException
from paramiko.ssh_exception import SSHException
import getpass
import os
from datetime import datetime

def backup():
    os.system("clear")
    today = datetime.today().strftime("%d-%m-%Y-%H:%M:%S")
    path = "../Backup Configuration"
    namedev = input("Nama Device : ")
    device = {
            "device_type": input("Tipe Device : "),
            "ip": input("IP X.X.X.X : "),
            "username": input("Username : "),
            "password": getpass.getpass("Password : "),
    }
    try:
        net_connect = ConnectHandler(**device)
    except NetMikoTimeoutException:
        print ("Connection Time Out, Silahkan Cek Koneksi")
    except AuthenticationException:
        print ("Authentication Failed, Silahkan Cek Username/Password")
    except SSHException:
        print ("SSH Failed, Pastikan SSH Aktif")

    print ()
    print ("Memulai Backup Konfigurasi...")
    command = net_connect.send_command("show running-config")
    savefile = os.path.join(path, str(namedev)+"_"+str(today)+".txt")
    save = open(savefile,"w")
    save.write(command)
    save.close
    print ("Selesai Backup...")
    print()
    pilih = input("Ingin backup lagi? (y/n) ")
    if pilih =="y" or pilih =="Y":
        backup()
    else:
        main()

def ipintbr():
    os.system("clear")
    device = {
            "device_type": input("Tipe Device : "),
            "ip": input("IP X.X.X.X : "),
            "username": input("Username : "),
            "password": getpass.getpass("Password : "),
    }
    net_connect = ConnectHandler(**device)
    command = net_connect.send_command("show ip int br")
    print ()
    print (command)
    print ()
    pilih = input("Melihat IP Int Brief Device lain? (y/n) ")
    if pilih =="y" or pilih =="Y":
        ipintbr()
    else:
        main()

def runconf():
    os.system("clear")
    device = {
            "device_type": input("Tipe Device : "),
            "ip": input("IP X.X.X.X : "),
            "username": input("Username : "),
            "password": getpass.getpass("Password : "),
    }
    net_connect = ConnectHandler(**device)
    command = net_connect.send_command("show running-config")
    print ()
    print (command)
    print ()
    pilih = input("Melihat Running-Config Device lain? (y/n) ")
    if pilih =="y" or pilih =="Y":
        runconf()
    else:
        main()

def linux():
    os.system("clear")
    device = {
            "device_type": input("Tipe Device : "),
            "ip": input("IP X.X.X.X : "),
            "username": input("Username : "),
            "password": getpass.getpass("Password : "),
            "port": input("Port : ")
    }
    try:
        connection = ConnectHandler(**device)
        print("Koneksi SSH berhasil!")
        
        # Menjalankan perintah di server Ubuntu
        output = connection.send_command("uname -a")
        print(output)
        
        # Menutup koneksi SSH
        connection.disconnect()
        print("Koneksi SSH ditutup.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def main():
    os.system("clear")
    print ("Program Backup Konfigurasi Netmiko Python")
    print ("=================================")
    print ()
    print ("1. Backup Konfigurasi")
    print ("2. Show Running-Config")
    print ("3. Melihat IP Interface Brief")
    print ("4. SSH Linux")
    print ("5. Keluar")
    print ()
    try:
        pilih = int(input("Input Pilihan 1-4 : "))
        if pilih == 1:
            backup()
        elif pilih == 2:
            runconf()
        elif pilih == 3:
            ipintbr()
        elif pilih == 4:
            linux()
        elif pilih == 5:
            exit()
        else:
            main()
    except ValueError:
        main()

main()
