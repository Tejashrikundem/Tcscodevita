from datetime import datetime, timedelta
def g_pri(m):
    for a in range(2, m+ 1):
        if p_fun(a):
            prime_num.append(a)

def p_fun(t):
    if t<= 1 :
        return False
    for k in range(2, t):
        if t % k == 0:
            return False
    return True
def g_pri(m):
  for a in range(2, m+ 1):
    if p_fun(a):
      prime_num.append(a)

dyr, dw, p= input().split()
p= int(p)
prime_num=[]
g_pri(365)
d_dic={0:"Mon", 1:"Tue", 2:"Wed", 3:"Thu", 4:"Fri", 5:"Sat", 6:"Sun"}
dyr=datetime.strptime(dyr, "%Y%m%d")
ds=-1
for j in prime_num:
    date= dyr + timedelta(j)
    if p_fun(date.month) and d_dic[date.weekday()]==dw:
        ds=j
        break
if ds==-1:
    print("no", 0,end="")
elif ds<=p:
    print("Yes", ds,end="")
else:
    print("no", ds,end="")
    
