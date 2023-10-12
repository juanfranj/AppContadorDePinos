from datetime import datetime

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

if __name__ == '__main__':
    actualizar_fecha()
    pinos = leer()[1]
    print(pinos)
    