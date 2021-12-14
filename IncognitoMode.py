import subprocess as sb

Hack = 'Log'

Output = sb.check_output(['ipconfig', '/displaydns'])
f = open(Hack+'.txt', 'wb')
f.write(Output)
f.close
