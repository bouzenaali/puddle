from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('', include('core.urls')),
    path('item/', include('item.urls')),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)