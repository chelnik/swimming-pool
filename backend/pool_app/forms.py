from django import forms

from .models import InstructorReview, PoolReview, PoolPass


class InstructorReviewForm(forms.ModelForm):
    class Meta:
        model = InstructorReview
        fields = ['instructor', 'rating', 'comment']


class PoolReviewForm(forms.ModelForm):
    class Meta:
        model = PoolReview
        fields = ['rating', 'comment']


class PoolPassForm(forms.ModelForm):
    class Meta:
        model = PoolPass
        fields = ['pass_type']
