from django.db import models


# ===============================
# COURSE MODEL
# ===============================
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ===============================
# TRAINER MODEL
# ===============================
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="trainers")

    def __str__(self):
        return self.name


# ===============================
# STUDENT MODEL
# ===============================
class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.student_id


# ===============================
# FEEDBACK (One per student)
# ===============================
class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="feedbacks")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="feedbacks")
    comment = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student',)  # Only one feedback per student

    def __str__(self):
        return f"{self.student.name} - {self.trainer.name}"


# ===============================
# FEEDBACK QUESTIONS
# ===============================
class FeedbackQuestion(models.Model):
    question_text = models.TextField()

    def __str__(self):
        return self.question_text


# ===============================
# FEEDBACK ANSWERS (Ratings per question)
# ===============================
class FeedbackAnswer(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(FeedbackQuestion, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.feedback.student.name} - {self.question.question_text}"


# ===============================
# CUSTOM ADMIN LOGIN MODEL
# ===============================
class Admin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
