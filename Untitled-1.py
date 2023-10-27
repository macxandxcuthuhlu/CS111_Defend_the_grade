
def list_to_int(list):
    list1 = []
    for i in range(len(list)):
        list1.append(int(list[i]))
    list = list1
    return list
        

lista = ['1', '12', '22', '3', '3']
lista = list_to_int(lista)
print(lista)
m = sum(lista)
print(m)


def mystery1(inp):
    out = 0
    for i in range (len(inp)):
        out = out + inp[i]
    return out

d = mystery1(lista)
print(d)

def buggy_mystery(list):
    last = list[-1]
    for i in range(len(list)-1):
        list[i] = list[i]/last
    
buggy_mystery(lista)
print(lista)

d = lista[:]
print(d)