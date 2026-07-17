from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', args=(course.id,)))
    return render(request, 'onlinecourse/course_details_bootstrap.html', {'course': course})

def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course, 'score': 85, 'status': 'Passed'}
    return render(request, 'onlinecourse/exam_result.html', context)
