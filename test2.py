import subprocess

# Some text to send
text = b'''100'''

file_name = 'main2.c'
file_name_prefix = file_name.split('.c')[0]
cmd = ['gcc','-o', file_name_prefix, file_name]
subprocess.call(cmd)
# Launch a command with pipes
p = subprocess.Popen('main2.exe',
          stdout = subprocess.PIPE,
          stdin = subprocess.PIPE, 
          shell=True)

# Send the data and get the output
stdout, stderr = p.communicate(text)

# To interpret as text, decode
out = stdout.decode('utf-8')
if stderr is not None:
	err = stderr.decode('utf-8')
print(out)
print(int(out.split('you age is')[1]))
p.kill()