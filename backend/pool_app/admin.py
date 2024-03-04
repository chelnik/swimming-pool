from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Instructor, Lesson, InstructorReview, PoolReview, PoolPass


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'qualifications', 'photo')
    search_fields = ('user__username', 'bio')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'start_time', 'end_time',
                    'description')
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


@admin.register(PoolPass)
class PoolPassAdmin(admin.ModelAdmin):
    list_display = ('owner', 'pass_type', 'start_date', 'end_date',
                    'is_active')
    list_editable = ('is_active',)


admin.site.unregister(Group)
