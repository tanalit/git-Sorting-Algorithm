with open ('province.txt','r',encoding='utf-8') as f:
    plist = list(f)
    pp = []
    i = 0
    for i in range(len(plist)):
        p = plist[i]
        p = p[64:]
        pp.append(p)

Newpp = []
i = 0
for i in range(len(pp)):
    np = pp[i]
    np = np.replace("(","").replace(")","").replace("'","").replace(",","").replace(";","")
    Newpp.append(np)


with open ('Oprovince.txt','w',encoding='utf-8') as f:
    for output in Newpp:
        f.write(output + '\n')