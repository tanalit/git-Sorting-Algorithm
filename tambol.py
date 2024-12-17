with open ('tambol.txt','r',encoding='utf-8') as f:
    tlist = list(f)
    tt = []
    i = 0
    for i in range(len(tlist)):
        t = tlist[i]
        t = t[82:]
        tt.append(t)

Newtt = []
i = 0
for i in range(len(tt)):
    nt = tt[i]
    nt = nt.replace("(","").replace(")","").replace("'","").replace(",","").replace(";","")
    Newtt.append(nt)


with open ('Otambol.txt','w',encoding='utf-8') as f:
    for output in Newtt:
        f.write(output + '\n')