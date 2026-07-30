"""
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('comment/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings
from config.views import home_page , HelpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page, name='home-page'),
    path('help/',HelpView.as_view(), name='help'),
    path('auth/',include('users.urls'), name='users'),
    path('post/',include('blog.urls'), name='post'),
    path('comment/',include('comment.urls'), name='comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
