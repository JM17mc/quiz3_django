import django.urls as urls
import main.views as views

urlpatterns = [
    urls.path('', views.student_list, name='student_list'),
]