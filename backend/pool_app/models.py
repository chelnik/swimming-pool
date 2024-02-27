from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    qualifications = models.CharField(max_length=255)

    def __str__(self):
        return self.user.get_full_name()


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name='lessons')

    def __str__(self):
        return self.title


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
