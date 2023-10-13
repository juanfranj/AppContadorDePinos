
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from datetime import datetime
from time import sleep
import threading   
    

class Contador(MDBoxLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hilo = threading.Thread(target = self.comprobar_centenas, name = 'Contador', daemon = True)
        
        

    def on_kv_post(self, base_widget):
        self.fecha, self.pino = self.leer()
        self.actualizar_fecha()
        self.pizarra = self.ids["conteo"]
        self.pizarra.text = self.leer()[1]
        self.hilo.start()

    
    def incrementar(self): # Método para incrementar el número en el Label
        # self.ids accede a cualquier identificador de elemento dentro de esta clase
        valor_actual = int(self.ids.conteo.text)
        valor_actual += 1
        self.ids.conteo.text = str(valor_actual)
        self.actualizar_fichero(self.fecha, valor_actual)
        self.actualizar_pinos(1)
        self.ids.my_image.source = "./images/sumar_1_press.png"

    def decrementar(self): # Método para decrementar el número en el Label
        valor_actual = int(self.ids.conteo.text)
        valor_actual -= 1
        if valor_actual < 0:
            valor_actual = 0
        self.ids.conteo.text = str(valor_actual)
        self.actualizar_fichero(self.fecha, valor_actual)
        if valor_actual > 0:
            self.actualizar_pinos(-1)
        self.ids.my_image_restar.source = "./images/restar_1_press.png"

    def on_release_sumar(self):
        self.ids.my_image.source = "./images/sumar_1.png"
    
    def on_release_restar(self):
        self.ids.my_image_restar.source = "./images/restar_1.png"
    
    def leer(self):
        file = open("./data/contador.txt", "r")
        texto = file.readline().split("::")
        file.close()
        return texto[0], texto[1]

    def actualizar_fichero(self, fecha, pinos):
        file = open("./data/contador.txt", "w")
        file.write(f"{fecha}::{pinos}")
        file.close()

    def actualizar_fecha(self):
        fecha_actual = datetime.now()
        fecha = self.leer()[0]
        if fecha != str(fecha_actual.date()):
            #self.actualizar_pinos()
            self.actualizar_fichero(str(fecha_actual.date()), 0)
                    
    def actualizar_pinos(self, num):
        pinos_actuales = self.leer()[1]
        file = open("./data/TotalPinos.txt", "r")
        pinos_anteriores = file.readlines()[0]
        #pinos_totales = int(pinos_anteriores) + int(pinos_actuales)
        pinos_totales = int(pinos_anteriores) + num
        file.close()
        #print(pinos_actuales, pinos_anteriores, pinos_totales)
        file = open("./data/TotalPinos.txt", "w")
        file.write(f"{pinos_totales}")
        file.close()
    
    def comprobar_centenas(self):
        fin = False
        real = False
        while not fin:
            num = self.leer_numero_total()
            #print(f"El numero total de pinos es {num}")
            if int(num)%20 == 0 and int(num) > 0 and real is False:
                self.ids.btn_inc.disabled = True
                self.ids.btn_dec.disabled = True
                valor_actual = self.ids.conteo.text
                self.ids.conteo.font_size = "50dp"
                self.ids.conteo.text = f"ENHORABUENA LLEVAS {num} PINOS EN TOTAL"
                sleep(5)
                self.ids.conteo.font_size = "200dp"
                self.ids.conteo.text = valor_actual
                self.ids.btn_inc.disabled = False
                self.ids.btn_dec.disabled = False
                real = True
            if int(num)%20 != 0 and int(num) > 0 and real is True:
                real = False 
            sleep(.2)
        #print(f"El hilo {threading.current_thread().name} ha finalizado")

    def leer_numero_total(self):
        file = open("./data/TotalPinos.txt", "r")
        num = file.readlines()[0]
        file.close()
        return num


