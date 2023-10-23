from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# from api.markers.models import Marker


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, username, google_id, password=None):
        if not email:
            raise ValueError('El campo "email" es obligatorio')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            google_id=google_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        if password is None:
            raise ValueError('El campo "password" es obligatorio para superusuarios')
        user = self.create_user(
            email=email,
            first_name='',
            last_name='',
            username=username,
            google_id='',
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    google_id = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff


class UserType(models.Model):

    TYPE_CHOICES = (
        ('S', 'STAFF'),
        ('C', 'CLIENT')
        )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE_CHOICES, default='C', max_length=2)


class Session(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    generation_date = models.DateTimeField()
    expiration_date = models.DateTimeField()

    def __str__(self):
        return f"Session for {self.user.username}"

    def check_expiration(self):
        if self.expiration_date <= timezone.now():
            self.active = False
            self.save()
