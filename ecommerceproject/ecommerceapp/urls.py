from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

app_name='ecommerceapp'
urlpatterns = [
    path('shop/',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.prodetail,name='product_detail'),
]
if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)