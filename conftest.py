import paramiko
import subprocess
import pytest


server_ip = '10.0.0.13'
password = 'Dfkthbz'
username = 'vlad'

@pytest.fixture(scope = 'function')
def server():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, username = username, password = password)
    stdin, stdout, stderr = ssh.exec_command('iperf3 -s -1')
    err = stderr.read()
    err = err.decode('utf-8')
    yield err
    ssh.close()


@pytest.fixture(scope = 'function')
def client():
    process = subprocess.Popen(['iperf3', '-c', server_ip, '-i', '1', '-l', '12'],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding = 'utf-8')
    stdout, stderr = process.communicate()
    yield stdout
    f = open('iperf3.txt', 'w')
    f.write(stdout)
    f.close()







