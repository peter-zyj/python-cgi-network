#! /usr/bin/python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import pexpect,os

try:
    os.remove("/var/www/html/images/map.png")
except:
    pass
paint = {}

a1=[404,404]
a2=[147,84]
a = [[a1,a2]]
paint['a'] = a

b1=[360,360]
b2=[199,174]
b3=[33,360]
b4=[199,199]
b5=[33,33]
b6=[260,199]
b7=[58,33]
b8=[260,260]
b=[[b1,b2],[b3,b4],[b4,b5],[b5,b6],[b7,b8]]
paint['b'] = b

c1=[223,135]
c2=[282,282]
c= [[c1,c2]]
paint['c'] = c

d1=[24,57]
d2=[282,282]
d3=[24,24]
d4=[310,282]
d5=[573,24]
d6=[310,310]
d7=[573,573]
d8=[410,310]
d9=[546,573]
d10=[410,410]
d=[[d1,d2],[d3,d4],[d5,d6],[d7,d8],[d9,d10]]
paint['d'] = d

e1=[529,529]
e2=[430,367]
e=[[e1,e2]]
paint['e'] = e

f1=[468,380]
f2=[445,445]
f=[[f1,f2]]
paint['f'] = f

g1=[339,251]
g2=[445,445]
g=[[g1,g2]]
paint['g'] = g


h1=[363,363]
h2=[493,457]
h=[[h1,h2]]
paint['h'] = h

i1=[573,546]
i2=[442,442]
i3=[573,573]
i4=[477,442]
i5=[25,573]
i6=[477,477]
i7=[25,25]
i8=[539,477]
i9=[58,25]
i10=[539,539]
i=[[i1,i2],[i3,i4],[i5,i6],[i7,i8],[i9,i10]]
paint['i'] = i

j1=[591,546]
j2=[429,429]
j3=[591,591]
j4=[678,429]
j5=[546,591]
j6=[674,678]
j=[[j1,j2],[j3,j4],[j5,j6]]
paint['j'] = j
########SSH logon stuff############
default_passwd = "notroot"
prompt_firstlogin = "Are you sure you want to continue connecting \(yes/no\)\?"
prompt_passwd = "root@.*'s password:"
prompt_logined = "\[root@.*\]#"
prompt_percentage = ".*100%.*"
prompt_tested = "\[root@.*\]#"
prompt_init = "continue ? (yes/no) [y]:"

def SSHClient(IP,prompt=prompt_tested):
    try:
        result = ""
        ssh = pexpect.spawn('ssh root@%s' % IP)
        result = ssh.expect([prompt_firstlogin, prompt_passwd, prompt, prompt_init, pexpect.TIMEOUT],timeout=1000)

        ssh.logfile = None
        if result == 0:
            ssh.sendline('yes')
            ssh.expect(prompt_passwd)
            ssh.sendline(default_passwd)
            ssh.expect(prompt)

        elif result == 1:
            ssh.sendline(default_passwd)
            ssh.expect(prompt)
        elif result == 2:
            pass
        elif result == 3:
            ssh.sendline('n')
            ssh.expect(prompt)
        elif result == 4:
            print "Connection::"+"ssh to %s timeout" %IP
            return result
        return ssh
    except:
        if prompt_init in ssh.before[:-1]:
            try:
                ssh.sendline('n')
                ssh.expect(prompt)
                return ssh
            except:
                print "Prompt_init Error:"
                debug = "Connection::"+ssh.before[:-1]
                print debug
                return debug
        else:
            print "result is ",result
            print 'Mismatch BTW default expect or unexpected things happen!'
            debug = "Connection::"+ssh.before[:-1]
            print debug
            return debug
        #sys.exit(0)


result = {}


ssh = SSHClient("10.94.153.206")

ssh.sendline('python /root/yijun/cdpCheck.py 10.94.153.207 Nexus-6K-R0-1A Nexus-5K-R0-1A')
ssh.expect(prompt_tested)
if "Good Connection" not in ssh.before[:-1]:
    result["a"] = 0
else:
    result["a"] = 1

ssh.sendline('python /root/yijun/cdpCheck.py 10.94.153.207 7609R1 Nexus-5K-R0-1A')
ssh.expect(prompt_tested)
if "Good Connection" not in ssh.before[:-1]:
    result["b"] = 0
else:
    result["b"] = 1

ssh.sendline('python /root/yijun/cdpCheck.py 10.94.153.213 7609R1 Row1-5596')
ssh.expect(prompt_tested)
if "Good Connection" not in ssh.before[:-1]:
    result["c"] = 0
else:
    result["c"] = 1


ssh.sendline('python /root/yijun/cdpCheck.py 10.94.153.213 7609R1 7609R2')
ssh.expect(prompt_tested)
if "Good Connection" not in ssh.before[:-1]:
    result["d"] = 0
else:
    result["d"] = 1


ssh.sendline('python /root/yijun/cdpCheck.py 10.94.153.223 3560SwitchR2 7609R2')
ssh.expect(prompt_tested)
if "Good Connection" not in ssh.before[:-1]:
    result["e"] = 0
else:
    result["e"] = 1


ssh.sendline('python /root/yijun/cdpCheck.py 10.94.153.223 5696-row2 7609R2')
ssh.expect(prompt_tested)
if "Good Connection" not in ssh.before[:-1]:
    result["f"] = 0
else:
    result["f"] = 1

ssh.sendline('python /root/yijun/cdpCheck.py 10.94.153.223 Row4Nex5596 7609R2')
ssh.expect(prompt_tested)
if "Good Connection" not in ssh.before[:-1]:
    result["j"] = 0
else:
    result["j"] = 1

ssh.sendline('python /root/yijun/cdpCheck.py 10.94.153.223 7609R3 7609R2')
ssh.expect(prompt_tested)
if "Good Connection" not in ssh.before[:-1]:
    result["i"] = 0
else:
    result["i"] = 1


ssh.sendline('python /root/yijun/cdpCheck.py 10.94.153.224 LindonFI-A 5696-row2')
ssh.expect(prompt_tested)
if "Good Connection" not in ssh.before[:-1]:
    result["g"] = 0
else:
    result["g"] = 1

ssh.sendline('python /root/yijun/cdpCheck.py 10.94.153.224 Row3-5696 5696-row2')
ssh.expect(prompt_tested)
if "Good Connection" not in ssh.before[:-1]:
    result["h"] = 0
else:
    result["h"] = 1


print result

result["a"] = 0
result["b"] = 0
result["c"] = 0
result["d"] = 0
result["e"] = 0
result["f"] = 0
result["g"] = 0
result["h"] = 0
result["i"] = 0
result["j"] = 0
lena = mpimg.imread('lab-map-base-act2.png')
plt.imshow(lena)

for x in result.keys():
    if result[x] != 1:
        l = paint[x]
        for idx in l:
            plt.plot(idx[0],idx[1],color="red",linewidth=3)


#plt.show()
plt.savefig("/var/www/html/images/map.png")

print "Content-type:text/html"
print                               
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title> Lindon Lab Network Topology! </title>'
print '</head>'
print '<body>'
print '<h2>Lindon Lab Network Topology!</h2>'
print '<form action="/cgi-bin/labMap2.py" method="post">'
print '<input type="submit" value="Topo Print" />'
print '</form>'
print '</body>'
print '</html>'
