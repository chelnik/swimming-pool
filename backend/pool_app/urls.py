from django.urls import path

from .views import (instructor_list, lesson_list, instructor_detail,
                    lesson_detail, add_instructor_review,
                    index, add_pool_review, review_list, instructor_review_list
                    )

app_name = 'pool_app'

urlpatterns = [
    path('', index, name='index'),
    path('instructors/', instructor_list, name='instructor_list'),
    path('lessons/', lesson_list, name='lesson_list'),
    path('instructors/<int:pk>/', instructor_detail, name='instructor_detail'),
    path('lessons/<int:pk>/', lesson_detail, name='lesson_detail'),
    # path('instructors/<int:instructor_id>/add_review/', add_instructor_review,
    #      name='add_instructor_review'),
    # path('add_pool_review/', add_pool_review, name='add_pool_review'),
    path('review/', review_list, name='review_list'),
    path('instructor-review/', instructor_review_list, name='instructor_review_list')
]
