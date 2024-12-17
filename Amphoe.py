with open ('Amphoe.txt','r',encoding='utf-8') as f:
    alist = list(f)
    aa = []
    i = 0
    for i in range(len(alist)):
        a = alist[i]
        a = a[64:]
        aa.append(a)

Newaa = []
i = 0
for i in range(len(aa)):
    na = aa[i]
    na = na.replace("(","").replace(")","").replace("'","").replace(",","").replace(";","")
    Newaa.append(na)


with open ('Oamphoe.txt','w',encoding='utf-8') as f:
    for output in Newaa:
        f.write(output + '\n')