from django import forms
from .models import Student, Trainer, Course, Feedback


# ================= STUDENT FORM ================= #
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'password', 'course', 'trainer']
        widgets = {
            'student_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student ID'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),
            'course': forms.Select(attrs={
                'class': 'form-select'
            }),
            'trainer': forms.Select(attrs={
                'class': 'form-select'
            }),
        }


# ================= TRAINER FORM ================= #
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'course']  # Better than __all__
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter trainer name'
            }),
            'course': forms.Select(attrs={
                'class': 'form-select'
            }),
        }


# ================= COURSE FORM ================= #
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course name'
            }),
        }


# ================= FEEDBACK FORM (Admin View) ================= #
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['student', 'trainer', 'comment']  # FIXED FIELD NAMES
        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-select'
            }),
            'trainer': forms.Select(attrs={
                'class': 'form-select'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter feedback comment'
            }),
        }