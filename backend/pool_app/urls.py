from django.urls import path

from .views import (instructor_list, lesson_list, instructor_detail,
                    lesson_detail, add_instructor_review, post_list,
                    index, add_pool_review, review_list,
                    instructor_review_list, buy_pool_pass, sign_up_for_lesson)

app_name = 'pool_app'

urlpatterns = [
    path('', index, name='index'),
    path('instructors/', instructor_list, name='instructor_list'),
    path('lessons/<int:lesson_id>/signup/', sign_up_for_lesson,
         name='sign_up_for_lesson'),

    path('lessons/', lesson_list, name='lesson_list'),
    path('instructors/<int:pk>/', instructor_detail, name='instructor_detail'),
    path('lessons/<int:pk>/', lesson_detail, name='lesson_detail'),
    path('instructors/<int:instructor_id>/add_review/', add_instructor_review,
         name='add_instructor_review'),
    path('add_pool_review/', add_pool_review, name='add_pool_review'),
    path('review/', review_list, name='review_list'),
    path('instructor-review/', instructor_review_list,
         name='instructor_review_list'),
    path('buy_pass', buy_pool_pass, name='buy_pool_pass'),
    path('posts/', post_list, name='post_list'),
]
