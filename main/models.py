from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Practice(models.Model):
    practice_number = models.CharField(max_length=100)

    def __str__(self):
        return self.practice_number

class Questions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_one = models.CharField(max_length=255)
    option_two = models.CharField(max_length=255)
    option_three = models.CharField(max_length=255)
    option_four = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class PythonMeaning(models.Model):
    title = models.CharField(max_length=255,blank=True)
    text = models.TextField()

class InterviewQuestionType(models.Model):
    type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.type

class InterviewQuestions(models.Model):
    interview_question_type = models.ForeignKey(InterviewQuestionType, on_delete=models.CASCADE)
    question = models.TextField(max_length=255, blank=True)
    img = models.ImageField(upload_to="productImages", blank=True)
    answer = models.TextField()

class RandomQuestions(models.Model):
    question = models.TextField(max_length=255, blank=True)
    img = models.ImageField(upload_to="productImages", blank=True)
    answer = models.TextField()

class SQLquestions(models.Model):
    interview_question_type = models.ForeignKey(InterviewQuestionType, on_delete=models.CASCADE)
    question = models.TextField(max_length=255, blank=True)
    img = models.ImageField(upload_to="productImages", blank=True)
    answer = models.TextField()