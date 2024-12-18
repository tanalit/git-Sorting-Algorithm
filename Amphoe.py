with open ('Amphoe.txt','r',encoding='utf-8') as f: 
    alist = list(f)                 # ทำข้อมูลเป็น list
    aa = []
    i = 0
    for i in range(len(alist)):     # ตัด string
        a = alist[i]
        a = a[64:]
        aa.append(a)

Newaa = []
i = 0
for i in range(len(aa)):            # replace เครื่องหมาย
    na = aa[i]
    na = na.replace("(","").replace(")","").replace("'","").replace(",","").replace(";","")
    Newaa.append(na)

LNewaa = []
i = 0
for i in range(len(Newaa)):         # ทำ list of list
    lna = Newaa[i]
    d1,d2,d3,d4 = lna.split(' ')
    ld = [d1,d2,d3,d4]
    LNewaa.append(ld)

with open ('Oamphoe.txt','w',encoding='utf-8') as f:  # write flie
    for output in Newaa:
        f.write(output + '\n')