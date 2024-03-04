from django import forms

from .models import InstructorReview, PoolReview, PoolPass, Lesson


class InstructorReviewForm(forms.ModelForm):
    class Meta:
        model = InstructorReview
        fields = ['rating', 'comment']


class PoolReviewForm(forms.ModelForm):
    class Meta:
        model = PoolReview
        fields = ['rating', 'comment']


class PoolPassForm(forms.ModelForm):
    class Meta:
        model = PoolPass
        fields = ['pass_type']


class LessonSignUpForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = []


class JobApplicationForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100)
    email = forms.EmailField(label="Ваш Email")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea)
