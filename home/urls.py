from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', views.home, name='home'),
	path('portfolio/', views.portfolio, name='portfolio'),
	path('contacts/', views.contacts, name='contacts'),
	path('prices/', views.prices, name='prices'),
	path('video/', views.video, name='video'),
	path('makeup/', views.makeup, name='makeup'),
	path('wedding/', views.wedding, name='wedding'),
	path('hair/', views.hair, name='hair'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)