with open ('tambol.txt','r',encoding='utf-8') as f:
    tlist = list(f)                 # ทำข้อมูลเป็น list
    tt = []
    i = 0
    for i in range(len(tlist)):     # ตัด string
        t = tlist[i]
        t = t[82:]
        tt.append(t)

Newtt = []
i = 0
for i in range(len(tt)):            # replace เครื่องหมาย
    nt = tt[i]
    nt = nt.replace("(","").replace(")","").replace("'","").replace(",","").replace(";","")
    Newtt.append(nt)

LNewtt = []
i = 0
for i in range(len(Newtt)):         # ทำ list of list
    lna = Newtt[i]
    d1,d2,d3,d4 = lna.split(' ')
    ld = [d1,d2,d3,d4]
    LNewtt.append(ld)

with open ('Otambol.txt','w',encoding='utf-8') as f:  # write flie
    for output in Newtt:
        f.write(output + '\n')