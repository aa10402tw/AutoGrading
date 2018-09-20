import subprocess
import glob
import os

student_id_list = []
hw_id_list = ['hw1']

class Student(object):
	def __init__(self, stu_id, hw_id_list):
		super(Student, self).__init__()
		self.stu_id = stu_id
		self.hw_id_list = hw_id_list
		self.init_hw_info()

	def init_hw_info(self):

		self.hw_info = {}
		for hw_id in self.hw_id_list:
			self.hw_info[hw_id] = {}

			### set mapping from hw_id to cfile path
			cfile = '%s_%s.c'%(self.stu_id, hw_id) if os.path.isfile(cfile) else None
			self.hw_info[hw_id]['cfile'] = cfile

			### set hw state(not processed yet, pass, fail)
			self.hw_info[hw_id]['state'] = 'not processed yet'

			### fail_info
			self.hw_info[hw_id]['fail_info'] = ''

	def __str__(self):
		s = "%s\n" %(self.stu_id)
		for hw_id in self.hw_id_list:
			s += '-'*50
			s += '%s\n\t'%(hw_id)
			s += 'cfile:%s, state:%s' %(self.hw_info[hw_id]['cfile'], self.hw_info[hw_id]['state'])
		return s

	def runTestCase(self, hw_id, testCase, expected_output):
		pass


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






