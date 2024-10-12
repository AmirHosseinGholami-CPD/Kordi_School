from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.UserPanelView.as_view(), name="teacher"),
    path('delete-student/<int:student_id>/<str:selected_class>/', views.DeleteStudentView.as_view(), name='delete_student'),
    path("absence/", views.UserPanelAbsenceView.as_view(), name="teacher_absence"),
    path('delete-absence/<int:student_id>/<str:selected_class>/', views.DeleteStudentAbsenceView.as_view(), name='delete_absence'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
