from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main import views
from main.views import home, python01, python_page, ForgetPassword, ChangePassword, Login, SignUp, Logout, \
    python_meaning_view, interview_questions_view, small_type_interview_questions, random_questions_view, search, \
    long_type_interview_questions, small_sql_questions, python_programming_questions, python_module, regex_module, \
    django_orm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login, name="login"),
    path('signup/', SignUp, name="signup"),
    path('logout/',Logout, name='logout'),
    path('ForgetPassword/',ForgetPassword, name="forget-password"),
    path('change_password/<token>/', ChangePassword, name='change_password'),
    path('home/', home, name="home"),
    path('search/', search, name="search"),
    path('python01/', python01, name="python01"),
    path('python_page/', python_page, name="python_page"),
    path('python_meaning/', python_meaning_view, name='python_meaning'),
    path('python_module/', python_module, name='python_module'),
    path('regex_module/', regex_module, name='regex_module'),
    path('django_orm/', django_orm, name='django_orm'),
    path('interview_questions/', interview_questions_view, name="interview_questions"),
    path('random_questions/', random_questions_view, name="random_questions"),
    path('small_type_interview_questions/', small_type_interview_questions, name="small_questions"),
    path('long_type_interview_questions/', long_type_interview_questions, name="long_questions"),
    path('python_programming_questions/', python_programming_questions, name="python_programming_questions"),
    path('small_sql_questions/', small_sql_questions, name="small_sql_questions"),


    # path('api/<id>', api_question, name="api_question"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)