from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from post.views import index, blog , post ,search
 #temitope
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path ('', index),  #temitope
    path('blog/', blog , name='post-list'), #temitope
    path ('search/' , search, name='search'),
    path ('post/<id>/', post, name='post-detail'),
]


#temitope
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
