from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import InstructorReviewForm, PoolReviewForm, PoolPassForm
from .models import Instructor, Lesson, PoolReview, InstructorReview, PoolPass


def index(request):
    has_active_pass = False
    if request.user.is_authenticated:
        has_active_pass = PoolPass.objects.filter(owner=request.user,
                                                  is_active=True).exists()

    return render(request, 'pool_app/index.html',
                  {'has_active_pass': has_active_pass})


def instructor_review_list(request):
    reviews = InstructorReview.objects.all()
    return render(request, 'pool_app/instructor_review_list.html',
                  {'reviews': reviews})


def review_list(request):
    if request.method == 'POST':
        form = PoolReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('pool_app:review_list')
    else:
        form = PoolReviewForm()
    reviews = PoolReview.objects.all()
    return render(request, 'pool_app/review_list.html', {
        'reviews': reviews,
        'form': form,
    })


def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'pool_app/instructor_list.html',
                  {'instructors': instructors})


def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'pool_app/lesson_list.html',
                  {'lessons': lessons})


def instructor_detail(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    return render(request, 'pool_app/instructor_detail.html',
                  {'instructor': instructor})


def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'pool_app/lesson_detail.html',
                  {'lesson': lesson})


@login_required
def add_instructor_review(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    if request.method == 'POST':
        form = InstructorReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.instructor = instructor
            review.author = request.user
            review.save()
            return redirect('pool_app:instructor_detail', pk=instructor.id)
    else:
        form = InstructorReviewForm()
    return render(request, 'pool_app/add_instructor_review.html',
                  {'form': form, 'instructor': instructor})


@login_required
def add_pool_review(request):
    if request.method == 'POST':
        form = PoolReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('index')
    else:
        form = PoolReviewForm()
    return render(request, 'pool_app/add_pool_review.html',
                  {'form': form})


@login_required
def buy_pool_pass(request):
    if request.method == 'POST':
        form = PoolPassForm(request.POST)
        if form.is_valid():
            pool_pass = form.save(commit=False)
            pool_pass.owner = request.user
            pool_pass.is_active = True
            pool_pass.save()
            return redirect('users:user_detail')
    else:
        form = PoolPassForm()
    return render(request, 'pool_app/buy_pool_pass.html',
                  {'form': form})
