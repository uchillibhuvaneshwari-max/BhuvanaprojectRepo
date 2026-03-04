from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Avg
from .models import (
    Student,
    Course,
    Trainer,
    Feedback,
    FeedbackQuestion,
    FeedbackAnswer
)

# =====================================
# HOME
# =====================================
def home(request):
    courses = Course.objects.all()
    
    # Fetch all feedback (this is your reviews)
    reviews = Feedback.objects.select_related("student", "trainer").order_by("-submitted_at")

    return render(request, "myapp/home.html", {
        "courses": courses,
        "reviews": reviews
    })
def about(request):
    return render(request, "myapp/about.html")
def contact(request):
    return render(request, "myapp/contact.html")


# =====================================
# STUDENT LOGIN
# =====================================
def student_login(request):
    courses = Course.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student_id").strip()
        password = request.POST.get("password").strip()

        try:
            student = Student.objects.get(student_id=student_id)

            if student.password == password:
                request.session["student_id"] = student.id
                messages.success(request, "Login Successful")
                return redirect("student_dashboard")
            else:
                messages.error(request, "Invalid Password")

        except Student.DoesNotExist:
            messages.error(request, "Invalid Student ID")

    return render(request, "myapp/student_login.html", {
        "courses": courses
    })


from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Student, Course, Trainer

def student_register(request):
    courses = Course.objects.all()
    trainers = Trainer.objects.all()

    if request.method == "POST":
        # STRIP spaces (THIS FIXES LOGIN ISSUE)
        student_id = request.POST.get("student_id").strip()
        name = request.POST.get("name").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password").strip()
        course_id = request.POST.get("course")
        trainer_id = request.POST.get("trainer")

        # Validate empty fields
        if not student_id or not password:
            messages.error(request, "Student ID and Password are required!")
            return redirect("student_register")

        # Check duplicate student_id
        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student ID already exists!")
            return redirect("student_register")

        # Check duplicate email
        if Student.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("student_register")

        try:
            course = Course.objects.get(id=course_id)
            trainer = Trainer.objects.get(id=trainer_id)
        except:
            messages.error(request, "Invalid course or trainer selected!")
            return redirect("student_register")

        # Create student
        Student.objects.create(
            student_id=student_id,
            name=name,
            email=email,
            password=password,
            course=course,
            trainer=trainer
        )

        messages.success(request, "Registration Successful! Please login.")
        return redirect("student_login")

    return render(request, "myapp/student_register.html", {
        "courses": courses,
        "trainers": trainers
    })
# =====================================
# STUDENT DASHBOARD
# =====================================
def student_dashboard(request):
    student_session = request.session.get("student_id")

    if not student_session:
        return redirect("student_login")

    student = get_object_or_404(Student, id=student_session)
    courses = Course.objects.all()  # For navbar dropdown

    return render(request, "myapp/student_dashboard.html", {
        "student": student,
        "courses": courses
    })


# =====================================
# STUDENT FEEDBACK
# =====================================
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, Feedback, FeedbackQuestion, FeedbackAnswer, Course


def student_feedback(request):
    student_id = request.session.get("student_id")

    # If not logged in → redirect
    if not student_id:
        return redirect("student_login")

    student = get_object_or_404(Student, id=student_id)

    # Fetch all dynamic questions added by admin
    questions = FeedbackQuestion.objects.all()

    # For navbar (as you already use it)
    courses = Course.objects.all()

    # Check if feedback already submitted
    already_submitted = Feedback.objects.filter(student=student).exists()

    if request.method == "POST":

        if already_submitted:
            messages.error(request, "You have already submitted feedback.")
            return redirect("student_dashboard")

        comment = request.POST.get("comment")

        # Create main feedback record
        feedback = Feedback.objects.create(
            student=student,
            trainer=student.trainer,
            comment=comment
        )

        # Save answers for each question dynamically
        for question in questions:
            rating = request.POST.get(f"question_{question.id}")

            if rating:  # if student selected rating
                FeedbackAnswer.objects.create(
                    feedback=feedback,
                    question=question,
                    rating=int(rating)
                )

        messages.success(request, "Feedback submitted successfully!")
        return redirect("student_dashboard")

    return render(request, "myapp/student_feedback.html", {
        "student": student,
        "questions": questions,
        "already_submitted": already_submitted,
        "courses": courses
    })
# =====================================
# LOGOUT
# =====================================
def student_logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully")
    return redirect("student_login")


# =====================================
# COURSE REVIEW DETAILS (MAIN FUNCTION)
# =====================================
def course_reviews(request, course_id):
    courses = Course.objects.all()  # For navbar dropdown

    # Selected course
    course = get_object_or_404(Course, id=course_id)

    # Trainers of this course
    trainers = Trainer.objects.filter(course=course)

    trainer_data = []

    for trainer in trainers:
        # Feedbacks for each trainer
        feedbacks = Feedback.objects.filter(trainer=trainer).select_related('student')

        # Average rating for each trainer
        avg_rating = FeedbackAnswer.objects.filter(
            feedback__trainer=trainer
        ).aggregate(avg=Avg('rating'))['avg']

        trainer_data.append({
            "trainer": trainer,
            "feedbacks": feedbacks,
            "average_rating": avg_rating
        })

    return render(request, "myapp/course_reviews.html", {
        "course": course,
        "trainer_data": trainer_data,  # ⭐ IMPORTANT (matches template)
        "courses": courses
    })
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def admin_login(request):
    courses = Course.objects.all()  # for navbar dropdown

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            messages.error(request, "Invalid Admin Username or Password")

    return render(request, "myapp/admin_login.html", {
        "courses": courses
    })
from django.contrib.auth import logout
from django.shortcuts import redirect

def admin_logout(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Trainer, Course, Feedback


@login_required(login_url='admin_login')  # redirect if not logged in
def admin_dashboard(request):
    total_students = Student.objects.count()
    total_trainers = Trainer.objects.count()
    total_feedback = Feedback.objects.count()

    # Optimized query (GOOD you used select_related 👍)
    students = Student.objects.select_related('course', 'trainer').all()

    context = {
        "total_students": total_students,
        "total_trainers": total_trainers,
        "total_feedback": total_feedback,
        "students": students,
    }

    return render(request, "myapp/admin_dashboard.html", context)
@login_required(login_url='admin_login')
def admin_students(request):
    students = Student.objects.select_related('course', 'trainer').all()
    return render(request, "myapp/admin_students.html", {
        "students": students
    })


from django.shortcuts import render, redirect
from .models import Trainer, Course
from .forms import TrainerForm, CourseForm


# ================= TRAINERS LIST =================
def admin_trainers(request):
    trainers = Trainer.objects.select_related('course').all()
    return render(request, "myapp/admin_trainers.html", {
        "trainers": trainers
    })


# ================= ADD TRAINER =================
def add_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_trainers')
    else:
        form = TrainerForm()

    return render(request, "myapp/add_trainer.html", {"form": form})


# ================= COURSES LIST =================
def admin_courses(request):
    courses = Course.objects.all()
    return render(request, "myapp/admin_courses.html", {
        "courses": courses
    })


# ================= ADD COURSE =================
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_courses')
    else:
        form = CourseForm()

    return render(request, "myapp/add_course.html", {"form": form})
from django.contrib.auth.decorators import login_required
from .models import Feedback, FeedbackAnswer

@login_required(login_url='admin_login')
def admin_feedback(request):
    # Get all feedback with related student & trainer (optimized)
    feedbacks = Feedback.objects.select_related(
        'student', 'trainer', 'trainer__course'
    ).all().order_by('-id')

    # Optional: include ratings if you use FeedbackAnswer model
    answers = FeedbackAnswer.objects.select_related('feedback')

    return render(request, "myapp/admin_feedback.html", {
        "feedbacks": feedbacks,
        "answers": answers
    })
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Course, Trainer


@login_required
def add_student(request):
    courses = Course.objects.all()
    trainers = Trainer.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student_id")
        name = request.POST.get("name")
        email = request.POST.get("email")  # MUST
        password = request.POST.get("password")
        course_id = request.POST.get("course")
        trainer_id = request.POST.get("trainer")

        # Validation for empty fields
        if not student_id or not name or not email or not password:
            messages.error(request, "All fields are required!")
            return redirect("add_student")

        # Check duplicate student ID
        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student ID already exists!")
            return redirect("add_student")

        # Check duplicate email (your model has unique=True)
        if Student.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("add_student")

        course = Course.objects.get(id=course_id)
        trainer = Trainer.objects.get(id=trainer_id)

        # CREATE student with ALL required fields
        Student.objects.create(
            student_id=student_id,
            name=name,
            email=email,
            password=password,
            course=course,
            trainer=trainer
        )

        messages.success(request, "Student added successfully!")
        return redirect("admin_students")

    return render(request, "myapp/add_student.html", {
        "courses": courses,
        "trainers": trainers
    })
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import * # make sure you created this form earlier
from django.contrib.auth.decorators import login_required


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()
    trainers = Trainer.objects.all()

    if request.method == "POST":
        student.student_id = request.POST.get("student_id")
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.password = request.POST.get("password")
        student.course_id = request.POST.get("course")
        student.trainer_id = request.POST.get("trainer")
        student.save()

        return redirect('admin_students')

    return render(request, "myapp/edit_student.html", {
        "student": student,
        "courses": courses,
        "trainers": trainers
    })

@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('admin_students')
from .models import FeedbackQuestion
from django.shortcuts import render, redirect


# ================= QUESTIONS LIST =================
def admin_questions(request):
    questions = FeedbackQuestion.objects.all()
    return render(request, "myapp/admin_questions.html", {
        "questions": questions
    })


# ================= ADD QUESTION =================
def add_question(request):
    if request.method == "POST":
        question_text = request.POST.get("question_text")
        if question_text:
            FeedbackQuestion.objects.create(question_text=question_text)
            return redirect("admin_questions")

    return render(request, "myapp/add_question.html")