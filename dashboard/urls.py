from django.urls import path
from.models import *
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path("",views.dashboard,name="dashboard"),
    path("projects/",views.dashboard_projects,name="dashboard_projects"),
    path("projects/add/",views.add_project,name="add_project"),
    path("projects/edit/<int:id>/", views.edit_project, name="edit_project"),
    path("projects/delete/<int:id>/", views.delete_project, name="delete_project"),
    path("gallery/",views.dashboard_gallery,name="dashboard_gallery"),
    path("gallery/add/",views.add_gallery,name="add_gallery"),
    path("gallery/delete/<int:id>/",views.delete_gallery,name="delete_gallery"),
    path("admin/blogs/", views.dashboard_blog, name="dashboard_blog"),
    path('admin/add/',views.add_blog,name='add_blog'),
    path("messages/",views.dashboard_messages,name="dashboard_messages"),
    path("admin/blogs/", views.dashboard_blog, name="dashboard_blog"),
    path("admin/add/", views.add_blog, name="add_blog"),
    path("admin/edit/<int:id>/", views.edit_blog, name="edit_blog"),
    path("admin/delete/<int:id>/", views.delete_blog, name="delete_blog"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)