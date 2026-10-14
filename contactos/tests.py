from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Contacto

class ContactoSecurityAndCRUDTests(TestCase):
    def setUp(self):
        # Usuario de prueba
        self.user = User.objects.create_user(username='operador', password='PasswordSeguro123!')
        
        # Contacto inicial
        self.contacto = Contacto.objects.create(
            codigo="CLI-001",
            nombres="Juan",
            apellidos="Pérez",
            rif="V-12345678-0",
            telefono_oficina="02125550000",
            telefono_movil="04141234567",
            correo="juan.perez@empresa.com"
        )

    def test_acceso_anonimo_redirecciona_a_login(self):
        """Los usuarios no autenticados deben ser enviados a login."""
        response = self.client.get(reverse('contacto_list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/cuentas/login/', response.url)

    def test_listado_con_usuario_autenticado(self):
        """Un usuario logueado puede ver los contactos."""
        self.client.login(username='operador', password='PasswordSeguro123!')
        response = self.client.get(reverse('contacto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CLI-001")

    def test_creacion_contacto_valido(self):
        """Prueba de inserción vía POST."""
        self.client.login(username='operador', password='PasswordSeguro123!')
        payload = {
            'codigo': 'CLI-002',
            'nombres': 'María',
            'apellidos': 'Gómez',
            'rif': 'J-98765432-1',
            'telefono_oficina': '02125551111',
            'telefono_movil': '04247654321',
            'correo': 'maria.gomez@empresa.com'
        }
        response = self.client.post(reverse('contacto_create'), data=payload)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Contacto.objects.filter(codigo='CLI-002').exists())

    def test_validacion_formato_rif_invalido(self):
        """Comprueba que el validador rechace formatos erróneos."""
        contacto_invalido = Contacto(
            codigo="CLI-003",
            nombres="Carlos",
            apellidos="Silva",
            rif="INVALIDO-123",
            telefono_movil="04120000000",
            correo="carlos@empresa.com"
        )
        with self.assertRaises(Exception):
            contacto_invalido.full_clean()