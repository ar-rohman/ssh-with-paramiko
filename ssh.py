import paramiko
from getpass import getpass

hostname = "192.168.56.101"
port = 21112
#username = input ("Usename : ")
#password = getpass()
command = input("command : ")

username = "eos" 
password = "namakulah"
#command = "fdisk -l"
#command = ["hostnamectl,ls /etc/ssh/"]


try :
	client=paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname = hostname, port = port, username= username, password = password)
	print ("\nSSH connection to %s established.\n\n" %hostname)
	output = ""
	stdin, stdout, stderr = client.exec_command(command)
	#stdin.write(password)
	#stdin.flush()
except paramiko.SSHException as sshException:
	print ("\n%s\n\n" %sshException)
	result_flag = False

stdout=stdout.readlines()

#print ("Command : "+command+"\n")
for line in stdout:
    output = output + line
if output != "":
    print (output)
else:
    print ("There was no output for this command")

client.close()
print ("\n\nLogged out\nConnection to %s closed.\n" %hostname)
