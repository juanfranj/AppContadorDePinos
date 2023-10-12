
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from datetime import datetime   
    

class Contador(MDBoxLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    def on_kv_post(self, base_widget):
        self.fecha, self.pino = self.leer()
        self.actualizar_fecha()
        self.pizarra = self.ids["conteo"]
        self.pizarra.text = self.leer()[1]
    
    def incrementar(self): # Método para incrementar el número en el Label
        # self.ids accede a cualquier identificador de elemento dentro de esta clase
        valor_actual = int(self.ids.conteo.text)
        valor_actual += 1
        self.ids.conteo.text = str(valor_actual)
        self.actualizar_fichero(self.fecha, valor_actual)
        self.ids.my_image.source = "./images/sumar_1_press.png"

    def decrementar(self): # Método para decrementar el número en el Label
        valor_actual = int(self.ids.conteo.text)
        valor_actual -= 1
        if valor_actual < 0:
            valor_actual = 0
        self.ids.conteo.text = str(valor_actual)
        self.actualizar_fichero(self.fecha, valor_actual)
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
            self.actualizar_pinos()
            self.actualizar_fichero(str(fecha_actual.date()), 0)
            
            
    def actualizar_pinos(self):
        pinos_actuales = self.leer()[1]
        file = open("./data/TotalPinos.txt", "r")
        pinos_anteriores = file.readlines()[0]
        pinos_totales = int(pinos_anteriores) + int(pinos_actuales)
        file.close()
        #print(pinos_actuales, pinos_anteriores, pinos_totales)
        file = open("./data/TotalPinos.txt", "w")
        file.write(f"{pinos_totales}")
        file.close()


