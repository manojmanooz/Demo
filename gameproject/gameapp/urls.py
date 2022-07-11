from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path
urlpatterns = [

    path('',views.home,name='home'),
    path('game/<int:game_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:game_id>',views.update,name='update'),
    path('delete/<int:game_id>', views.delete, name='delete'),
]
if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)
