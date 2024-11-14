listaspesa = []
def aggiunta():
    risp = input("Dimmi un prodotto da aggiungere: ")
    listaspesa.append(risp)

def visualizza():
    print(listaspesa)

aggiunta()
visualizza()