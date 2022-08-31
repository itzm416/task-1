from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from patient_doctor import views
from blog import views as view
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('doctor/', views.doctor, name='doctor'),

    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),


    path('dashboard/', views.dashboard, name='d'),
    path('appoinment/<slug:slug>/', views.appoinment, name='a'),
    path('login/', views.user_login, name='l'),
    path('signup/', views.user_signup, name='s'),
    path('logout/', views.user_logout, name='logout'),

    path('blog/', view.blog, name='b'),
    path('blog-category/<slug:slug>/', view.blog_category, name='blogcategory'),
    path('upload-blog/', view.add_blog, name='upload'),
    path('my-blogs/', view.my_blog_post, name='myblogs'),
    path('my-draft-blogs/', view.my_draft_blog_post, name='mydraftblogs'),
    path('read-blog/<slug:slug>/', view.read_post, name='read'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
