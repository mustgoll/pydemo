import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.80.128',port=22,username='root',password='www',timeout=3)
msg=input('>>')
stdin,stdout,stderr=ssh.exec_command(msg)
print(stdout.read().decode())