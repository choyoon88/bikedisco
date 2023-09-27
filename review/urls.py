from review import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='review'),
    path('write_review/', views.get_write_review, name='write_review'),
    path('edit/<slug:slug>/', views.edit_review, name='edit_review'),
    path('delete/<slug:slug>/', views.delete_review, name='delete_review'),
    path('add_comment/', views.write_comment, name='add_comment'),
]
