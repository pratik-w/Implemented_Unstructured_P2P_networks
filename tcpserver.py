# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:02:11 2016

@author: waradepratik
"""
#import package
import socket
import sys
import _thread
import time
import subprocess
import datetime as dt
def Main():
    #create socket
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:     #validation for valid port number
        port=input("$Enter port number : -")
        temp=int(port)
        if temp<=0:
            raise ValueError
        else:
            port=temp           
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")
         s.close()         
         
    print("socket created")
    
    s.bind(('',port)) #bind sockete with port number and ip
    s.listen(10) #by specifying 10, it means that if 10 connections are already waiting to be processed, then the 11th connection request shall be rejected.
    print("socket is now listening")
    def clientthread(conn,):  #defining thread function       
        while True: 
             #Gett all argument from client and put them in different variable
             command = conn.recv(1024).decode('utf-8')    
             time.sleep(3)            
             if not command: 
                 break
             
             #get execution count and assign to variable
             count = conn.recv(1024).decode('utf-8')
             time.sleep(3)             
             if not count: 
                 break
             exe_count= int(count)
             
             #get delay count and assign to delay variable
             delay = conn.recv(2048).decode('utf-8')
             time.sleep(3)            
             if not delay: 
                 break
             exe_delay= float(delay) 
             
             #run till numnber of count are enter and calculate execution time
             for run_pgram in range(exe_count):#run loop till range matches to exe_count
                 start_time=dt.datetime.now()
                 op = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
                 end_time=dt.datetime.now()  #calculate execution time
                 exe_time=(end_time-start_time).microseconds
                 print("Execution Time in microsecond: " ,exe_time)
                 (output, err)=op.communicate()                 
                 time.sleep(exe_delay)                
                 temp_op=output
                 if temp_op:                     
                    # print ("Output:", (temp_op))
                     conn.sendall(temp_op)
                 else:
                    error=str(op.stderr.read())
                    #print ("Error:",str(error))
                    conn.sendall(error)         
             
            # print ("Close")    
        conn.close()
    
    while 1:
        conn,addr = s.accept()
        print("Connected with " + addr[0] + " :" + str(addr[1]))
        #print("In thread loop")
        _thread.start_new_thread(clientthread,(conn, ))
       # print("DONE")
      
    s.close
        
if __name__ == '__main__':
    Main()

    




