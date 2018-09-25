import argparse
import subprocess
import glob
import os


class TestCase(object):
    def __init__(self, inputs=[], outputs=[], mode='loose'):
        super(TestCase, self).__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.mode = mode

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, key):
        return self.inputs[key], self.outputs[key]

    def __setitem__(self, key, value):
        input_, ouput = value
        self.inputs[key] = input_
        self.outputs[key] = output

    def append(self, test_case):
        input_, ouput = test_case
        self.inputs.append(input_)
        self.outputs.append(output)


class Student(object):
    def __init__(self, stu_id, hw_id_list):
        super(Student, self).__init__()
        self.stu_id = stu_id
        self.hw_id_list = hw_id_list
        self.init_hw_info()
        self.num_questions_total = 0
        self.num_questions_pass = 0

    def init_hw_info(self):

        self.hw_info = {}
        for hw_id in self.hw_id_list:
            self.hw_info[hw_id] = {}

            # set mapping from hw_id to cfile path
            if not os.path.isdir('source_file'):
                os.makedirs('source_file')
            cfile = '%s//%s_%s.c' % ('source_file', self.stu_id, hw_id)
            cfile = cfile if os.path.isfile(cfile) else None
            self.hw_info[hw_id]['cfile'] = cfile

            # set hw state(not processed yet, pass, fail)
            self.hw_info[hw_id]['state'] = 'not processed yet'

            # fail_info
            self.hw_info[hw_id]['fail_info'] = 'Can not find .c file' if cfile is None else ''

    def evaluate_score(self):
        num_pass, num_hw = 0, len(self.hw_id_list)
        for hw_id in self.hw_id_list:
            if(self.hw_info[hw_id]['state'] == 'pass'):
                num_pass += 1
        return (num_pass / num_hw) * 100

    def runTestCase(self, hw_id, testCase):
        if hw_id in self.hw_id_list:
            self.num_questions_total += 1
            self.hw_info[hw_id]['state'] = 'fail'
            cFile = self.hw_info[hw_id]['cfile']
            if cFile is None:
                return
            if not os.path.isdir('exe_file'):
                os.makedirs('exe_file')
            exeFile = '%s//%s' % ('exe_file', os.path.split(cFile)[-1].split('.c')[0])
            cmd = ['gcc', '-o', exeFile, cFile]
            exeFile = '"%s.exe"' % (exeFile)
            try:
                subprocess.call(cmd, shell=True)
            except:
                self.hw_info[hw_id]['fail_info'] += 'can not compile .c file'
            else:
                num_test, num_pass = 0, 0
                for input_, expected_output in testCase:
                    num_test += 1
                    # Launch a command with pipes
                    p = subprocess.Popen(exeFile,
                                         stdout=subprocess.PIPE,
                                         stdin=subprocess.PIPE,
                                         shell=True)
                    # Send the data and get the output
                    try:
                        stdout, stderr = p.communicate(str(input_).encode(), timeout=3)
                    except:
                        s = 'Test Case #%i timeout error for input [%s]' % (num_test, repr(str(input_)))
                        self.hw_info[hw_id]['fail_info'] += s
                    else:
                        # To interpret as text, decode
                        output = stdout.decode('utf-8')

                        if(str(output) == str(expected_output)):
                            num_pass += 1
                        elif testCase.mode == 'loose' and (" ".join(str(expected_output).split())) in (" ".join(str(output).split())):
                            num_pass += 1
                        else:
                            s = 'Test Case #%i : input [%s], expected output is [%s] but got [%s]\n' % (num_test, repr(str(input_)), repr(expected_output), repr(output))
                            self.hw_info[hw_id]['fail_info'] += s
                        if stderr is not None:
                            err = stderr.decode('utf-8')
                            self.hw_info[hw_id]['fail_info'] += err

                if num_pass == num_test:
                    self.hw_info[hw_id]['state'] = 'pass'
                    self.num_questions_pass += 1
                else:
                    self.hw_info[hw_id]['fail_info'] = 'pass ratio %i/%i\n' % (num_pass, num_test) + self.hw_info[hw_id]['fail_info']

    def __str__(self):
        s = '-' * 50 + '\n'
        s += "Student %s" % (self.stu_id)
        for hw_id in self.hw_id_list:
            s += '\n[%s]' % (hw_id)
            s += '\n\tcfile : %s' % (self.hw_info[hw_id]['cfile'])
            s += '\n\tstate : %s' % (self.hw_info[hw_id]['state'])
            if self.hw_info[hw_id]['fail_info'].strip():
                s += '\n\tfail_info : %s' % (self.hw_info[hw_id]['fail_info'])
        s += '\n' + '-' * 50 + '\n'
        return s


#####################
### Main Program  ###
#####################

import json

with open("hw2.json") as f:
    json_data = json.load(f)

# Hw info & test case
hw_id_list = json_data['hw_id_list']
testCase_list = []
for i, hw_id in enumerate(hw_id_list):
    testCase = TestCase([], [])
    testCase_list.append(testCase)
    for test_case in json_data['test_cases'][i]['test_case']:
        input_ = test_case['input']
        output = test_case['output']
        testCase.append((input_, output))

# Student id & Create a list of student
student_id_list = ['0756079']
print('Enter your student ID : ', end='')
stuID = input()
if stuID is not None:
    print('AutoGrading for student %s' % stuID)
    student_id_list = [stuID]

student_list = []
for stu_id in student_id_list:
    student_list.append(Student(stu_id, hw_id_list))

# Start Evaluate
for stu in student_list:
    for testCase, hw_id in zip(testCase_list, hw_id_list):
        stu.runTestCase(hw_id, testCase)
    print(stu)
    print('Finish autoGrading, Your Score is %.2f (Pass %i/%i questions) ' % (stu.evaluate_score(), stu.num_questions_pass, stu.num_questions_total))

a = input()
