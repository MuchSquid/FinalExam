import unittest
import app
import json

class TestBilleteraElectronica(unittest.TestCase):
    # Establece un entorno de prueba
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    # Prueba para verificar obtener contactos
    def test_obtener_contactos(self):
        response = self.app.get('/billetera/contactos?minumero=21345')
        self.assertEqual(response.status_code, 200)
        self.assertIn('123', json.loads(response.data))

    # Prueba para verificar el éxito de un pago
    def test_pagar_exitoso(self):
        response = self.app.post('/billetera/pagar', data={
            'minumero': '21345',
            'numerodestino': '123',
            'valor': '50'
        })
        self.assertEqual(response.status_code, 200)

        # Verificar si el saldo se actualizó correctamente
        cuenta = app.encontrar_cuenta('21345')
        self.assertEqual(cuenta.saldo, 150)  # 200 - 50

    # Prueba para verificar pago fallido por saldo insuficiente
    def test_pagar_saldo_insuficiente(self):
        response = self.app.post('/billetera/pagar', data={
            'minumero': '21345',
            'numerodestino': '123',
            'valor': '250'
        })
        self.assertEqual(response.status_code, 400)

    # Prueba para verificar obtener historial
    def test_historial(self):
        response = self.app.get('/billetera/historial?minumero=21345')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Operaciones', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()