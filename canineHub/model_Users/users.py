"""from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, password, phone, is_boss):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            is_boss=is_boss
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    # Campos personalizados
    is_boss = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email' # cual va a ser la PK
    REQUIRED_FIELDS = ['name', 'phone']"""

"""# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, contraseña=None, **extra_fields):
        if not correo:
            raise ValueError("El usuario debe tener un correo electrónico")
        correo = self.normalize_email(correo)
        usuario = self.model(correo=correo, nombre=nombre, **extra_fields)
        usuario.set_password(contraseña)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, nombre, contraseña=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(correo, nombre, contraseña, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    ROL_CHOICES = [
        ('administrador', 'Administrador'),
        ('asesor', 'Asesor'),
        ('cliente', 'Cliente'),
    ]


    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios',  # Cambia el nombre para evitar conflictos
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios',  # Cambia el nombre para evitar conflictos
        blank=True,
    ) 

    USERNAME_FIELD = 'correo' # Campo que se usará como nombre de usuario
    REQUIRED_FIELDS = ['nombre'] # Campos requeridos al crear un usuario


    def __str__(self): 
        return self.nombre"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, contraseña=None, **extra_fields):
        if not correo:
            raise ValueError("El usuario debe tener un correo electrónico")
        correo = self.normalize_email(correo)
        usuario = self.model(correo=correo, nombre=nombre, **extra_fields)
        usuario.set_password(contraseña)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, nombre, contraseña=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(correo, nombre, contraseña, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    ROL_CHOICES = [
        ('administrador', 'Administrador'),
        ('asesor', 'Asesor'),
        ('cliente', 'Cliente'),
    ]
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('bloqueado', 'Bloqueado'),
    ]

    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    permission = models.CharField(max_length=150, blank=True)  # Adaptación del campo permission
    identification = models.CharField(max_length=20, blank=False)  # Adaptación del campo identification

    objects = UsuarioManager()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios',  # Cambiado para evitar conflictos
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios',  # Cambiado para evitar conflictos
        blank=True,
    )

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    class Meta:
        db_table = "Usuario"

    def __str__(self):
        return self.nombre


class Rol(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    description = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{str(self.id)} {self.name}"

    class Meta:
        db_table = "Rol"


class UserRol(models.Model):
    id = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)  # Usamos Usuario
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.id)} {str(self.id_rol)}"

    class Meta:
        db_table = "UserRol"

