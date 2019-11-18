import subprocess
import glob
import os
from tqdm import tqdm
import time


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

    @staticmethod
    def processOutput(s, omit=['\r', '\t', '\n']):
        s = str(s)
        for c in omit:
            s = s.replace(c, ' ')
        s = " ".join(s.split())
        if(' 'in omit):
            s = s.replace(' ', '')
        return s


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
            self.hw_info[hw_id]['fail_info'] = 'Can not find .c file (Expected "%s//%s_%s.c")' % (
                'source_file', self.stu_id, hw_id) if cfile is None else ''

    def get_hw_results(self):
        results = []
        hw_id_list = self.hw_id_list
        for hw_id in hw_id_list:
            if(self.hw_info[hw_id]['state'] == 'pass'):
                results.append('pass')
            elif ('Can not find .c file' in self.hw_info[hw_id]['fail_info']):
                results.append('cFile')
            elif ('Can not compile' in self.hw_info[hw_id]['fail_info'] or 'Can not find .exe file' in self.hw_info[hw_id]['fail_info']):
                results.append('compile')
            elif('timeout error' in self.hw_info[hw_id]['fail_info']):
                results.append('time_out')
            elif('timeout error' in self.hw_info[hw_id]['fail_info']):
                results.append('utf-8')
            elif('pass ratio' in self.hw_info[hw_id]['fail_info']):
                ratio = self.hw_info[hw_id]['fail_info'].split('pass ratio')[1].split(')')[0]
                results.append('%s' % ratio)
            else:
                results.append(self.hw_info[hw_id]['fail_info'])
                print(self.hw_info[hw_id]['fail_info'])
        return results

    def evaluate_score(self, haveBonus=True):
        num_pass, num_hw = 0, len(self.hw_id_list)
        for i, hw_id in enumerate(self.hw_id_list):
            if haveBonus and i == num_hw - 1:
                pass_bonus = True if(self.hw_info[hw_id]['state'] == 'pass') else False
            elif(self.hw_info[hw_id]['state'] == 'pass'):
                num_pass += 1
        if haveBonus:
            score = (num_pass / (num_hw - 1)) * 100
            if pass_bonus:
                score += 10
            return score
        return (num_pass / num_hw) * 100

    def runTestCase(self, hw_id, testCase):
        self.hw_info[hw_id]['state'] = 'fail'
        self.num_questions_total += 1
        if hw_id not in self.hw_id_list:
            return
        if self.hw_info[hw_id]['cfile'] is None:
            return
        cFile = self.hw_info[hw_id]['cfile']
        exeFile = '%s//%s' % ('exe_file', os.path.split(cFile)[-1].split('.c')[0])
        cmd = ['gcc', '-o', exeFile, cFile]

        if not os.path.isdir('exe_file'):
            os.makedirs('exe_file')

        # Try to Compile
        try:
            subprocess.call(cmd)
        except:
            self.hw_info[hw_id]['fail_info'] += 'Can not compile .c file'
            return

        if not os.path.isfile(exeFile + '.exe'):
            self.hw_info[hw_id]['fail_info'] += 'Can not find .exe file (probably compile fail)'
            return

        # Start to run test case
        num_test, num_pass = 0, 0
        exeFile = '"%s.exe"' % (exeFile)
        for input_, expected_output in testCase:
            num_test += 1
            p = subprocess.Popen(exeFile, stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE)  # Launch a command with pipes
            # Send input and get ouput
            if DEBUG_MODE:
                print(hw_id, end=',')
                now = time.time()

            try:
                stdout, stderr = p.communicate(str(input_).encode(), timeout=30)
            except:
                s = '\n  <Test Case #%i> : timeout error for input [%s]' % (
                    num_test, repr(str(input_)))

                s = ''
                if DEBUG_MODE:
                    print('time_out', end=',')
                    print('%.4f' % (time.time() - now), end=',')
                p.kill()
                _ = str(input_).encode()
                self.hw_info[hw_id]['fail_info'] += s
                continue

            if DEBUG_MODE:
                print('%.4f' % (time.time() - now))
            if stderr:
                print('Test', repr(stderr))
                self.hw_info[hw_id]['fail_info'] += stderr

            # Decode output
            try:
                output = stdout.decode('utf-8')
            except:
                self.hw_info[hw_id][
                    'fail_info'] += '\n  <Test Case #%i> : output is not utf-8 format' % (num_test)
                continue

            # Compare user output with answer
            output_ = TestCase.processOutput(output)
            expected_output_ = TestCase.processOutput(expected_output)
            if output_ == expected_output_:  # Correct
                num_pass += 1
            else:  # Incorrect
                s = '\n\n  <Test Case #%i> : \n    input [%s], \n    expected output is [%s] \n    but your output is [%s]' % (
                    num_test, repr(str(input_)), expected_output_, output_, )
                self.hw_info[hw_id]['fail_info'] += s

        # After run all test case, check the pass ratio
        if num_pass == num_test:
            self.hw_info[hw_id]['state'] = 'pass'
            self.num_questions_pass += 1
        else:
            self.hw_info[hw_id]['fail_info'] = 'Unable to pass all test cases (pass ratio %i/%i)' % (
                num_pass, num_test) + self.hw_info[hw_id]['fail_info']

    # def runTestCase(self, hw_id, testCase):
    #     if hw_id in self.hw_id_list:
    #         self.num_questions_total += 1
    #         self.hw_info[hw_id]['state'] = 'fail'
    #         cFile = self.hw_info[hw_id]['cfile']
    #         if cFile is None:
    #             return
    #         if not os.path.isdir('exe_file'):
    #             os.makedirs('exe_file')
    #         exeFile = '%s//%s' % ('exe_file', os.path.split(cFile)[-1].split('.c')[0])
    #         cmd = ['gcc', '-o', exeFile, cFile]
    #         exeFile = '"%s.exe"' % (exeFile)
    #         try:
    #             subprocess.call(cmd, shell=True)
    #         except:
    #             self.hw_info[hw_id]['fail_info'] += 'can not compile .c file'
    #         else:
    #             num_test, num_pass = 0, 0
    #             for input_, expected_output in testCase:
    #                 num_test += 1
    #                 # Launch a command with pipes
    #                 p = subprocess.Popen(exeFile,stdout=subprocess.PIPE,stdin=subprocess.PIPE,
    #                                      shell=True)
    #                 # Send the data and get the output
    #                 try:
    #                     stdout, stderr = p.communicate(str(input_).encode(), timeout=3)
    #                 except:
    #                     s = '\n  <Test Case #%i> : timeout error for input [%s]' % (num_test, repr(str(input_)))
    #                     self.hw_info[hw_id]['fail_info'] += s
    #                 else:
    #                     # To interpret as text, decode
    #                     output = stdout.decode('utf-8')

    #                     if(TestCase.processOutput(output) == TestCase.processOutput(expected_output)):
    #                         num_pass += 1
    #                     else:
    #                         s = '\n\n  <Test Case #%i> : \n    input [%s], \n    expected output is [%s] \n    but got [%s]' % (num_test, repr(str(input_)), repr(expected_output), repr(output))
    #                         self.hw_info[hw_id]['fail_info'] += s
    #                     if stderr is not None:
    #                         err = stderr.decode('utf-8')
    #                         self.hw_info[hw_id]['fail_info'] += err

    #             if num_pass == num_test:
    #                 self.hw_info[hw_id]['state'] = 'pass'
    #                 self.num_questions_pass += 1
    #             else:
    #                 self.hw_info[hw_id]['fail_info'] = 'Unable to pass all test cases (pass ratio %i/%i)'%(num_pass, num_test) + self.hw_info[hw_id]['fail_info']

    def __str__(self):

        s = "\n## Student %s ##\n" % (self.stu_id)
        l = len(s) - 2
        s = '\n' + '#' * l + s + '#' * l + '\n'
        s += '-' * 13
        for hw_id in self.hw_id_list:
            s += '\n[%s]' % (hw_id)
            s += '\t%s' % (self.hw_info[hw_id]['state'].capitalize())
            if self.hw_info[hw_id]['fail_info'].strip():
                s += '\n'
                s += '\n  Fail_info : %s' % (self.hw_info[hw_id]['fail_info'])
                s += '\n'
            l = len(s.splitlines()[-1]) + 2
            s += '\n'
            s += '-' * l
        return s


#####################
### Main Program  ###
#####################


DEBUG_MODE = False

import json

with open("hw9.json") as f:
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

omit = ['\t', '\r', '\n']

# # Student Version
# print('Enter your student ID : ', end='')
# stuID = input()
# if stuID:
#     print('AutoGrading for student %s' % stuID)
#     print('Note : All the %s and extra white space will be ignored in the ouput' % omit)
#     stu = Student(stuID, hw_id_list)
#     for testCase, hw_id in zip(testCase_list, hw_id_list):
#         stu.runTestCase(hw_id, testCase)
#     print(stu)
#     print('Finish autoGrading, Your Score is %.2f (Pass %i/%i questions) ' % (stu.evaluate_score(), stu.num_questions_pass, stu.num_questions_total))
# print('\nPress anything to exit..')
# input()

# TA Version
with open("StuID.json") as f:
    json_data = json.load(f)
    student_id_list = json_data['stu_id_list']

student_list = []
for stu_id in student_id_list:
    student_list.append(Student(stu_id, hw_id_list))

import pandas as pd

data = {'ID': student_id_list, 'score': []}
for hw_id in hw_id_list:
    data[hw_id] = []


# Start Evaluate
for i_, stu in enumerate(tqdm(student_list[:])):
    for testCase, hw_id in zip(testCase_list, hw_id_list):
        stu.runTestCase(hw_id, testCase)
    # print(stu)
    # print('Finish autoGrading, Your Score is %.2f (Pass %i/%i questions) ' % (stu.evaluate_score(), stu.num_questions_pass, stu.num_questions_total))
    # print('Finish ', stu.stu_id, len(data['score']))

    score = stu.evaluate_score()
    results = stu.get_hw_results()
    data['score'] = data['score'] + [score]
    for i, hw_id in enumerate(hw_id_list):
        data[hw_id] = data[hw_id] + [results[i]]

df = pd.DataFrame(data)
df.to_csv('week9.csv', sep='\t', index=False)
df.to_excel('week9.xlsx', sheet_name='sheet1', index=False)

print(len(student_id_list))
