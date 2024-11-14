listaspesa = []
def aggiunta():
    risp = input("Dimmi un prodotto da aggiungere: ")
    listaspesa.append(risp)

def visualizza():
    for i in range(len(listaspesa)):
        print(f"{i}. {listaspesa[i]}")
        i =  i + 1

def elimina():
    risp1 = int(input("Dimmi l'indice di un prodotto da eliminare: "))
    listaspesa.pop(risp1)
    print(listaspesa)

while True:
    print("1) aggiungi 2) visualizza 3) elimina ")
    opzioni = int(input(""))
    if opzioni == 1:
        aggiunta()
    elif opzioni == 2:
        visualizza()
    elif opzioni == 3:
        elimina()  
    break  
