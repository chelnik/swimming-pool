from django.contrib import admin
from .models import Instructor, Lesson, InstructorReview, PoolReview


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'qualifications')
    search_fields = ('user__username', 'bio')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'start_time', 'end_time', 'description')
    list_filter = ('instructor', 'start_time')
    search_fields = ('title', 'description')


@admin.register(InstructorReview)
class InstructorReviewAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'author', 'rating', 'comment', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment',)


@admin.register(PoolReview)
class PoolReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'comment', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment',)
