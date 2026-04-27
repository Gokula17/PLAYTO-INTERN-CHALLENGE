from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("KYCFlow API is running 🚀")

urlpatterns = [
    path('', home),  # 👈 add this line
    path('admin/', admin.site.urls),
    path('api/v1/', include('kyc.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
