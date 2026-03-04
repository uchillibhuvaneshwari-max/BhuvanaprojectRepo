from .models import Admin
from django.contrib import admin
from .models import (
    Course,
    Trainer,
    Student,
    Feedback,
    FeedbackQuestion,
    FeedbackAnswer
)


# ===============================
# COURSE ADMIN
# ===============================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# ===============================
# TRAINER ADMIN
# ===============================
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course')
    list_filter = ('course',)


# ===============================
# STUDENT ADMIN
# ===============================
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'course', 'trainer')
    search_fields = ('student_id', 'name')
    list_filter = ('course', 'trainer')


# ===============================
# FEEDBACK ADMIN
# ===============================
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student', 'trainer', 'submitted_at')
    list_filter = ('trainer',)
    search_fields = ('student__name',)


# ===============================
# FEEDBACK QUESTION ADMIN
# ===============================
@admin.register(FeedbackQuestion)
class FeedbackQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text')


# ===============================
# FEEDBACK ANSWER ADMIN
# ===============================
@admin.register(FeedbackAnswer)
class FeedbackAnswerAdmin(admin.ModelAdmin):
    list_display = ('feedback', 'question', 'rating')
    list_filter = ('question',)



