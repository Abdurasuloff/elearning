from django.contrib import admin
from django.urls import path, include
from django.conf import  settings
from django.conf.urls.static import static
from courses.views import CourseListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('course/', include("courses.urls")),
    path('api/', include("courses.api.urls", namespace='api')),
    path('students/', include('students.urls')),
    path('chat/', include('chat.urls', namespace = 'chat')),
    # path('__debug__/', include('debug_toolbar.urls')),
    path('', CourseListView.as_view(), name='course_list'),
    
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
