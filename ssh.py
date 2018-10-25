import paramiko
from getpass import getpass

hostname = "hostname"
port = 22
username = "username"
password = "password"
command = "ls /home"

try :
	client=paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname = hostname, port = port, username= username, password = password)
	print ("\nSSH connection to %s established.\n\n" %hostname)
	hasil = ""
	stdin, stdout, stderr = client.exec_command(command)
except paramiko.SSHException as sshException:
	print ("\n%s\n\n" %sshException)
	result_flag = False

stdout=stdout.readlines()

for line in stdout:
    hasil = hasil + line
if hasil != "":
    print (hasil)
else:
    print ("There was no result for this command")

client.close()
print ("\n\nLogged out\nConnection to %s closed.\n" %hostname)
