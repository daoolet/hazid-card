from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

from multiselectfield import MultiSelectField

from .utils import ACTIVITY_OBSERVED, I_OBSERVED, POSSIBLE_CONSEQUENCES, CONDITIONS_RELATED


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
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "CUser"
        verbose_name_plural = "CUsers"

    def __str__(self):
        return self.email
    

class AllowedUser(models.Model):
    email = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Allowed User"
        verbose_name_plural = "Allowed Users"

    def __str__(self) -> str:
        return self.email
    

class Survey(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=35)
    company_observed = models.CharField(max_length=20)
    activity_observed = models.CharField(max_length=27, choices=ACTIVITY_OBSERVED, default=None)
    i_observed = models.CharField(max_length=21, choices=I_OBSERVED, default="None")
    possible_consequences = MultiSelectField(max_length=255, choices=POSSIBLE_CONSEQUENCES)
    conditions_related = MultiSelectField(max_length=500, choices=CONDITIONS_RELATED)
    description = models.CharField(max_length=300)
    swa_applied = models.BooleanField(default=False)
    corrective_measures = models.BooleanField(default=False)
    further_action = models.BooleanField(default=False)
    corrective_action = models.CharField(max_length=150)
    reported = models.BooleanField(default=False)
    if_reported = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Hazid"
        verbose_name_plural = "Hazids"
    
    def __str__(self):
        return self.title