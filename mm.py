with open ('mm.txt','r',encoding='utf-8') as f:
    mlist = list(f)
    mm = []
    i = 0
    for i in range(len(mlist)):
        m = mlist[i]
        m = m[191:-49]
        mm.append(m)

Newmm = []
i = 0
for i in range(len(mm)):
    nm = mm[i]
    nm = nm.replace("(","").replace("'","").replace(",","")
    Newmm.append(nm)


with open ('Omm.txt','w',encoding='utf-8') as f:
    for output in Newmm:
        f.write(output + '\n')