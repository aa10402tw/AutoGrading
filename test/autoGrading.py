import subprocess
import glob
import os

student_list = []
hw_id_list = ['hw1']

for c_file_path in glob.glob('./*.c'):
	c_file = os.path.basename(c_file_path)
	student_id = c_file.split('_')[0]
	print(c_file.split('_'))
	hw_id = c_file.split('_')[1].split('.c')[0]
	if hw_id not in hw_id_list:
		print('Wrong file name:', c_file)
	else :
		print( "file:%s stu_id:%s hw_id:%s"%(c_file, student_id, hw_id))
		file_name = c_file
		file_name_prefix = file_name.split('.c')[0]
		cmd = ['gcc','-o', file_name_prefix, file_name]
		subprocess.call(cmd)
		input = b'''100'''
		# Launch a command with pipes
		p = subprocess.Popen(file_name_prefix + '.exe',
		          stdout = subprocess.PIPE,
		          stdin = subprocess.PIPE, 
		          shell=True)
		# Send the data and get the output
		stdout, stderr = p.communicate(input)
		# To interpret as text, decode
		out = stdout.decode('utf-8')
		if stderr is not None:
			err = stderr.decode('utf-8')
			print(err)
		print(out)






