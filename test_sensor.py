import unittest
from sensor_hidraulico import evaluar_temperatura_aceite

class PruebasSensorHidraulico(unittest.TestCase):

    def test_sensor_congelado(self):
        resultado = evaluar_temperatura_aceite(-5)
        self.assertEqual(resultado, "Error: Sensor congelado o falla de lectura")

    def test_temperatura_normal(self):
        resultado = evaluar_temperatura_aceite(50)
        self.assertEqual(resultado, "Normal")
        
    def test_temperatura_borde_cero(self):
        resultado = evaluar_temperatura_aceite(0)
        self.assertEqual(resultado, "Normal")

    def test_alerta_sobrecalentamiento(self):
        resultado = evaluar_temperatura_aceite(90)
        self.assertEqual(resultado, "Alerta: Sobrecalentamiento")

    def test_peligro_apagar(self):
        resultado = evaluar_temperatura_aceite(110)
        self.assertEqual(resultado, "Peligro: Apagar Motor")

if __name__ == '__main__':
    unittest.main()