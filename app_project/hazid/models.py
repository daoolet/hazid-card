from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager


from .utils import ACTIVITY_OBSERVED, I_OBSERVED, POSSIBLE_CONSEQUENCES


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    # Добавьте нужные поля профиля
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Survey(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)

    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=35)
    company_observed = models.CharField(max_length=20)
    activity_observed = models.CharField(max_length=30, choices=ACTIVITY_OBSERVED)
    i_obseved = models.CharField(max_length=24, choices=I_OBSERVED, default="None")
    possible_consequences = models.CharField(max_length=24, choices=POSSIBLE_CONSEQUENCES, default="None")

    class Meta:
        verbose_name = "survey"
        verbose_name_plural = "surveys"
    
    def __str__(self):
        return self.title