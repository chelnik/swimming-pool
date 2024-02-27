from django import forms

from .models import InstructorReview, PoolReview


class InstructorReviewForm(forms.ModelForm):
    class Meta:
        model = InstructorReview
        fields = ['instructor', 'rating', 'comment']


class PoolReviewForm(forms.ModelForm):
    class Meta:
        model = PoolReview
        fields = ['rating', 'comment']
