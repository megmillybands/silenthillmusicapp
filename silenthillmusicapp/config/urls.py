from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('silent-hill-1/', silenthillone, name='silenthillone'),
    path('silent-hill-2/', silenthilltwo, name='silenthilltwo'),
    path('silent-hill-3/', silenthillthree, name='silenthillthree'),
    path('player/<int:song_id>', player, name='player'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)