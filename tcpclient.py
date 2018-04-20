# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 19:03:29 2016

@author: waradepratik
"""
#final tcp program
#import package
import socket   
import socket
import sys
import time

def Main():
    
    #create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created Successfully")
    
    #get arguments from user
    hostName_input,portNumber_input,command, count,delay=input("$").split()
    
    #print(hostName_input,portNumber_input,command,count,delay)
    #Get ip addr from hostname
    remote_ip= socket.gethostbyname(hostName_input)
    remote_port= int(portNumber_input)
    exe_count=int(count)
    
    #Assign command to message variable 
    serveraddr=(remote_ip,remote_port)
    message1=command
    message2=count
    message3=delay
   
    s.connect((remote_ip,remote_port))
    
    #print("Sending command" , command)
    s.sendall(message1.encode('utf-8'))
    time.sleep(3)
    #print("Sending count" , count)
    s.sendall(message2.encode('utf-8'))
    time.sleep(3)
    #print("Sending delay" , delay)
    s.sendall(message3.encode('utf-8'))
    time.sleep(3)
    
    #recv data and print data
    while exe_count:        
        data = s.recv(2048)
        data = data.decode('utf-8')        
        print(data)        
        exe_count=exe_count-1
    s.close()
       
    
if __name__ == '__main__':
    Main()