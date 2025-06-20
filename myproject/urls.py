from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('book', views.book, name='book'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('adduserdetail', views.adduserdetail, name='adduserdetail'),
    path('showuser', views.showuser, name='showuser'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('update', views.update, name='update'),
    path('addauthor', views.addauthor, name='addauthor'),
    path('showauthor', views.showauthor, name='showauthor'),
    path('editauthor', views.editauthor, name='editauthor'),
    path('updateauthor', views.updateauthor, name='updateauthor'),
    path('upload_book', views.upload_book, name='upload_book'),
    path('bookdetail/<int:bid>', views.bookdetail, name='bookdetail'),
    path('pricing', views.pricing, name='pricing'),
    path('create_order/<int:plan_id>', views.create_order, name='create_order'),
    path('payment_success', views.payment_success, name='payment_success'),
    path('showfeedback', views.showfeedback, name='showfeedback'),
    path('complaint_submit', views.complaint_submit, name='complaint_submit'),
    path('upload_book_detail', views.upload_book_detail, name='upload_book_detail'),
    path('send_publish_request', views.send_publish_request, name='send_publish_request'),
    path('update_publisher_request', views.update_publisher_request, name='update_publisher_request'),
    path('showrequest', views.showrequest, name='showrequest'),
    path('find_products', views.find_products, name='find_products'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
]

# Serve static and media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
