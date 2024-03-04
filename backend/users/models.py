from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    '''
    Переопределенная модель пользователя.
    '''

    date_of_birth = models.DateField(blank=True, null=True)

    phone_regex = RegexValidator(regex=r'^(?:\+7|8)\d{10}$',
                                 message="Неверный формат номера телефона")
    phone_number = models.CharField(validators=[phone_regex], max_length=12,
                                    unique=True, blank=False, null=False)

    @property
    def active_pool_pass(self):
        return self.poolpass_set.filter(is_active=True).first()

    @property
    def age(self):
        if self.date_of_birth is not None:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )

        return None

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = 'username',

    def __str__(self):
        return self.username
