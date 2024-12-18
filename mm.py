with open ('mm.txt','r',encoding='utf-8') as f:
    mlist = list(f)                 # ทำข้อมูลเป็น list
    mm = []
    i = 0
    for i in range(len(mlist)):     # ตัด string
        m = mlist[i]
        m = m[191:-49]
        mm.append(m)

Newmm = []
i = 0
for i in range(len(mm)):            
    nm = mm[i]
    nm = nm.replace("(","").replace("'","").replace(",","")
    Newmm.append(nm)

LNewmm = []
i = 0
for i in range(len(Newmm)):         # ทำ list of list
    lna = Newmm[i]
    d1,d2,d3,d4 = lna.split(' ')
    ld = [d1,d2,d3,d4]
    LNewmm.append(ld)

with open ('Omm.txt','w',encoding='utf-8') as f:   # write flie
    for output in Newmm:
        f.write(output + '\n')