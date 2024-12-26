import random

def salaCumple(nPersonas):
    sala = []
    for n in range(nPersonas):
        cumple = random.randint(1,365)
        sala.append(cumple)
    
    sala.sort()    
    for n in range(len(sala)-1):
        if sala[n] == sala[n+1]:
            return True

def main():
    counter = 0
    nPersonas = input("Cuantás personas habrá en la sala? :")
    nPersonas = int(nPersonas)
    for i in range(100):
        if salaCumple(nPersonas):
            counter = counter + 1
    #print("La probabilidad de que se repita el cumpleaños es de : "+ str(counter) + "%")
    print("BUG APLICACIÓN ROTA")
    
    
if __name__ == "__main__":
    main()