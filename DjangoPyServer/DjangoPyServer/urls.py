from django.contrib import admin
from django.urls import include, path
from .views import error_404
from django.conf.urls import handler404, handler500

handler404 = error_404

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('AdminMap.urls')),
	path('', include('RestfulCoffeeBreaker.urls'))
]
