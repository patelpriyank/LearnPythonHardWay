import subprocess

#shell=True : The only time you need to specify shell=True on Windows is when the command you wish to execute is built into the shell (e.g. dir or copy). 
#You do not need shell=True to run a batch file or console-based executable.
#Warning Executing shell commands that incorporate unsanitized input from an untrusted source makes a program vulnerable to shell injection, 
#a serious security flaw which can result in arbitrary command execution. For this reason, the use of shell=True is strongly discouraged in cases where the command string is constructed from external input:
subprocess.call('dir', shell=True)

subprocess.check_call(['dir', '/b'], shell=True)

echoOp = subprocess.check_output(['echo','Hellp world!'], shell=True, stderr=subprocess.STDOUT)
print(echoOp)

#exitcode = subprocess.check_output(['exit 1'])
#print(exitcode)

filename = input("What file would you like to display? ")

print('\nOpening file.........\n')
subprocess.call('type ' + filename, shell=True)
print('\nEnd of file...........\n')