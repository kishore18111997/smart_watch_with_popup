d = {'node1':0, 'NXL48546':0, 'node3':0,'node4':0,'node5':0}
print(d)
import socket
name = socket.gethostname()

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

# create the root window
root = tk.Tk()
root.title('Requesting Test run')
root.geometry('300x150')

# click event handler
def confirm():
    answer = askyesno(title='confirmation',
                    message='Are you sure you want to decline?')
    print(answer)
    if answer:
        root.destroy()
        name = socket.gethostname()
        index = None
        f=open(r"C:\\Users\User\\Desktop\\python-test\\slaveresults\\windowsslave4.txt", 'w')
        f.write('0')
        f.close()
        if name in d:
            index = list(d).index(name)
            key = list(d)[1]
            element = d.pop(key)
            print(d)
            value = list(d.values())[1]
    else:
        print(d)
        f = open(r"C:\\Users\User\\Desktop\\python-test\\slaveresults\\windowsslave4.txt", 'w')
        f.write('1')
        f.close()
        root.destroy()
ttk.Button(
    root,
    text='Confirm',
    command=confirm).pack(expand=True)


# start the app
root.mainloop()
'''
import paramiko
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=’174.129.111.157’,username=’Administrator’,password=’xZOJR*VZvuFimZ-HmBQEiUO;Na5jbm7g’,port=22, timeout=3)

ftp_client=ssh.open_sftp()
ftp_client.put(‘localfilepath’,remotefilepath’)
ftp_client.close()
'''