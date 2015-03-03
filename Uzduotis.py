def daugyba(x,y):
    sudauginti=[]
    for y in range(y):
        sudauginti.append(x*y)
    return sudauginti

def ikelimas(x,y):
    sarasas=[]
    for x in range(x):
        sarasas.append(daugyba(x,y))
    return sarasas

while True:
    try:
        eilute, stulpelis = input("Iveskite eiluciu ir stulpeliu skaiciu per kableli: ").split(",")
        break
    except ValueError:
        print("Klaida! Iveskite du skaicius per kableli ")

x=int(eilute)
y=int(stulpelis)

print(ikelimas(x,y))
