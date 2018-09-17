from subprocess import call
from subprocess import check_output

file_name = 'main.c'
file_name_prefix = file_name.split('.c')[0]
cmd = ['gcc','-o', file_name_prefix, file_name]
print(cmd)
call(cmd)
output_byte = check_output('main.exe', shell=True)
out_text = output_byte.decode('utf-8')
print('result : ', out_text)



