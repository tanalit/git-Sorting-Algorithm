with open ('province.txt','r',encoding='utf-8') as f:
    plist = list(f)                 # ทำข้อมูลเป็น list
    pp = []
    i = 0
    for i in range(len(plist)):     # ตัด string
        p = plist[i]
        p = p[64:]
        pp.append(p)

Newpp = []
i = 0
for i in range(len(pp)):            # replace เครื่องหมาย
    np = pp[i]
    np = np.replace("(","").replace(")","").replace("'","").replace(",","").replace(";","")
    Newpp.append(np)

LNewpp = []
i = 0
for i in range(len(Newpp)):         # ทำ list of list
    lna = Newpp[i]
    d1,d2,d3,d4 = lna.split(' ')
    ld = [d1,d2,d3,d4]
    LNewpp.append(ld)

with open ('Oprovince.txt','w',encoding='utf-8') as f:   # write flie
    for output in Newpp:
        f.write(output + '\n')