from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from blog import views
import authentication.views
from authentication import views as auth_views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.login_page, name='login'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', blog.views.home, name='home'),
    path('photo/upload/', blog.views.upload_photo, name='upload_photo'),
    path('upload_profile_photo/', auth_views.upload_profile_photo, name='upload_profile_photo'),
    path('blog/<int:pk>/', blog.views.view_blog, name='view_blog'),
    path('profile/', auth_views.user_profile, name='user_profile'),
    path('create/', blog.views.blog_create, name='blog_create'),
    path('changer-photo/', auth_views.upload_profile_photo, name='upload_profile_photo'),
    path('blog/<int:blog_id>/edit/', blog.views.edit_blog, name='edit_blog'),
    path('photo/upload_multiple/', blog.views.create_multiple_photos, name='create_multiple_photos'),
    path('follow_users/', blog.views.follow_users, name='follow_users')



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)