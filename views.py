from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Question, Choice, Submission, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        choice_ids = request.POST.getlist('choice')
        enrollment, created = Enrollment.objects.get_or_create(
            user=request.user, 
            course=course
        )
        submission = Submission.objects.create(enrollment=enrollment)
        for c_id in choice_ids:
            choice = get_object_or_404(Choice, pk=c_id)
            submission.choices.add(choice)
        
        request.session['submission_id'] = submission.id
        return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', args=(course.id,)))
    
    return render(request, 'onlinecourse/course_details_bootstrap.html', {'course': course})

def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    submission_id = request.session.get('submission_id')
    submission = get_object_or_404(Submission, pk=submission_id)
    
    selected_ids = [choice.id for choice in submission.choices.all()]
    total_score = 0
    possible_score = 0
    
    for question in course.question_set.all():
        possible_score += question.grade
        if question.is_get_score(selected_ids):
            total_score += question.grade
            
    context = {
        'course': course,
        'selected_ids': selected_ids,
        'grade': total_score,
        'possible': possible_score,
        'score': (total_score / possible_score * 100) if possible_score > 0 else 0
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
