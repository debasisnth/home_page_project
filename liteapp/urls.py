from django.urls import path
from . import views




urlpatterns = [
	path('', views.home, name='liteapp-home'),

	path('thanks/', views.thanks, name='liteapp-thanks')

]