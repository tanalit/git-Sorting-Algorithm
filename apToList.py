
def apTolist():
    l = []
    with open('Data\AmphoeHomework.txt','r', encoding='utf-8') as fin:
        for line in fin:
            n1,n2,n3,n4 = line.split()
            l.append(n1)
    return l


def spell(l):
    sp = []
    for i in l:
        sp.append(int(i))
    return sp

def data_ap():
    l = apTolist()
    data = []
    for i in range(len(l)):
        data.append(spell(l[i]))
    return data

