from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from cart_app import views
app_name='cart_app'
urlpatterns=[
    path('add/<int:product_id>/',views.AddCart,name='AddCart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_delete'),
    path('delete/<int:product_id>/',views.cart_delete,name='full_delete')
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)