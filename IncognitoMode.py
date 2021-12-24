import subprocess as sb

Hack = 'Log'

Output = sb.check_output(['ipconfig', '/displaydns'])
f = open(Hack+'.log', 'wb')
f.write(Output)
f.close
