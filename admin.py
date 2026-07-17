from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission, Enrollment

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 2

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    list_filter = ['course']
    search_fields = ['title', 'description']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'grade']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
