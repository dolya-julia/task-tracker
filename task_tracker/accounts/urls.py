from django.urls import path
from . import views
from .views import SignUpView, CustomLoginView, profile, ChangePasswordView, task_list
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', profile, name='users-profile'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('update_task_status/<int:task_id>/', views.update_task_status, name='update_task_status'),
]
