from django.db import models
from django.core.validators import RegexValidator

class Contacto(models.Model):
    rif_validator = RegexValidator(
        regex=r'^[J|V|G|E|P|C]-\d{8,9}-\d$',
        message='El RIF debe tener el formato J-12345678-0'
    )

    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código")
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    rif = models.CharField(max_length=15, unique=True, validators=[rif_validator], verbose_name="RIF")
    telefono_oficina = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono Oficina")
    telefono_movil = models.CharField(max_length=20, verbose_name="Teléfono Móvil")
    correo = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.codigo} - {self.nombres} {self.apellidos}"