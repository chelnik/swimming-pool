from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from datetime import timedelta


User = get_user_model()


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    qualifications = models.CharField(max_length=255)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Инструктор'
        verbose_name_plural = 'Инструкторы'


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name='lessons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'


class InstructorReview(models.Model):
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE,
                                   related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Отзыв на {self.instructor.user.get_full_name()} от "
                f"{self.author.username}")

    class Meta:
        verbose_name = 'Отзыв на инструктора'
        verbose_name_plural = 'Отзывы на инструкторов'


class PoolReview(models.Model):
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        rating_str = dict(self.RATING_CHOICES)[self.rating]
        return f"Отзыв от {self.author.username} Рейтинг: {rating_str}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class PoolPass(models.Model):
    TYPE_CHOICES = (
        ('monthly', 'Месячный'),
        ('quarterly', 'Квартальный'),
        ('yearly', 'Годовой'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='Владелец')
    pass_type = models.CharField(max_length=10, choices=TYPE_CHOICES,
                                 default='monthly',
                                 verbose_name='Тип абонемента')
    start_date = models.DateField(auto_now_add=True,
                                  verbose_name='Дата начала действия')
    end_date = models.DateField(verbose_name='Дата окончания действия')
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.pass_type == 'monthly':
                self.price = 1000
                self.end_date = timezone.now().date() + timedelta(days=30)
            elif self.pass_type == 'quarterly':
                self.price = 2000
                self.end_date = timezone.now().date() + timedelta(days=90)
            elif self.pass_type == 'yearly':
                self.price = 5000
                self.end_date = timezone.now().date() + timedelta(days=365)
            self.start_date = timezone.now().date()

        super().save(*args, **kwargs)

    def check_activation(self):
        if self.end_date < timezone.now().date():
            self.is_active = False
            self.save()

    def __str__(self):
        return (f"Абонемент: {self.pk}-{self.get_pass_type_display()}\n"
                f"годен до {self.end_date}")
