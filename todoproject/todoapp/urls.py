from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:todo_id>/',views.delete,name='delete'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path("cbvdetail/<int:pk>/",views.TAskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
]