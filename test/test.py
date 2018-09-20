import subprocess
import glob
import os


student_id_list = ['0756079', '0756080']
hw_id_list = ['hw1', 'hw2']

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
			cfile = '%s_%s.c'%(self.stu_id, hw_id)
			cfile = cfile if os.path.isfile(cfile) else None
			self.hw_info[hw_id]['cfile'] = cfile

			### set hw state(not processed yet, pass, fail)
			self.hw_info[hw_id]['state'] = 'not processed yet'

			### fail_info
			self.hw_info[hw_id]['fail_info'] = 'Can not find .c file' if cfile is None else ''

	def evaluate_score(self):
		num_pass, num_hw = 0, len(self.hw_id_list)
		for hw_id in self.hw_id_list:
			if(self.hw_info[hw_id]['state'] == 'pass'):
				num_pass += 1
		return (num_pass / num_hw) * 100

	def runTestCase(self, hw_id, testCases, expected_outputs):
		if hw_id in self.hw_id_list:
			self.hw_info[hw_id]['state'] = 'fail'
			cFile = self.hw_info[hw_id]['cfile']
			if cFile is None : return
			exeFile = cFile.split('.c')[0]
			cmd = ['gcc','-o', exeFile, cFile]
			try:
				subprocess.call(cmd, shell=True)
			except:
				self.hw_info[hw_id]['fail_info'] += 'can not compile .c file'
			else:
				num_test, num_pass = 0, 0
				for input, expected_output in zip(testCases, expected_outputs):
					num_test += 1
					# Launch a command with pipes
					p = subprocess.Popen(exeFile + '.exe',
					          stdout = subprocess.PIPE,
					          stdin = subprocess.PIPE, 
					          shell=True)
					# Send the data and get the output
					stdout, stderr = p.communicate(str(input).encode())
					# To interpret as text, decode
					output = stdout.decode('utf-8')
					if(str(output) == str(expected_output)):
						num_pass += 1
					else:
						s = 'Test Case #%i : input [%s], expected output is [%s] but got [%s]\n' %(num_test, str(input), expected_output, output)
						self.hw_info[hw_id]['fail_info'] += s
					if stderr is not None:
						err = stderr.decode('utf-8')
						self.hw_info[hw_id]['fail_info'] += err
				if num_pass == num_test:
					self.hw_info[hw_id]['state'] = 'pass'
				else:
					self.hw_info[hw_id]['fail_info'] = 'pass ratio %i/%i\n'%(num_pass,num_test) + self.hw_info[hw_id]['fail_info']

	def __str__(self):
		s = "Student %s" %(self.stu_id)
		for hw_id in self.hw_id_list:
			s += '\n[%s]'%(hw_id)
			s += '\n\tcfile : %s' %(self.hw_info[hw_id]['cfile'])
			s += '\n\tstate : %s' %(self.hw_info[hw_id]['state'])
			s += '\n\tfail_info : %s' %(self.hw_info[hw_id]['fail_info'])
		return s




student_list = []
for stu_id in student_id_list:
	student_list.append(Student(stu_id, hw_id_list))

student_list[0].runTestCase(hw_id_list[0], [1, 2, 3], [1,2,3])
print(student_list[0])
print(student_list[0].evaluate_score())