from datetime import datetime
from time import sleep
import threading


def leer():
    file = open("./data/contador.txt", "r")
    texto = file.readline().split("::")
    file.close()
    print(texto)
    return texto[0], texto[1]

def actualizar_fichero(fecha, pinos):
    file = open("./data/contador.txt", "w")
    file.write(f"{fecha.date()}::{pinos}")
    file.close()

def actualizar_fecha():
    fecha_actual = datetime.now()
    fecha, pinos = leer()
    #print(fecha, fecha_actual.date(), fecha != str(fecha_actual.date()))
    if fecha != str(fecha_actual.date()):
        actualizar_fichero(fecha_actual, pinos)
    #print(fecha_actual.date(), fecha, pinos)

def comprobar_centenas():
    fin = False
    while not fin:
        num = leer_numero_total()
        print(f"El numero total de pinos es {num}")
        sleep(2)
        if num == "12":
            fin = True
    print(f"El hilo {threading.current_thread().name} ha finalizado")

def leer_numero_total():
    file = open("./data/TotalPinos.txt", "r")
    num = file.readlines()[0]
    file.close()
    return num

if __name__ == '__main__':
    
    hilo = threading.Thread(target = comprobar_centenas, name = 'Contador')
    print(f'Comienza el hilo {hilo.name}')
    #hilo.start()
    #hilo.join()
    print(100%100)
    
    