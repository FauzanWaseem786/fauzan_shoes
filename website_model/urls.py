from . import views
from django.urls import path
app_name='website_model'
urlpatterns=[
path('', views.index, name='index'),
path('Variety/',views.Variety,name='Variety'),
path('brands/',views.brands,name='brands'),
path('location/',views.location,name='location'),
path('membership/',views.Premium,name='Premium'),
path('shoes/',views.shoes,name='shoes'),
path('sandals/',views.sandals,name='sandals'),
path('boots/',views.boots,name='boots'),
path('slippers/',views.slippers,name='slippers'),
path('Membership/',views.Membership,name='Membership'),
path('login/',views.login,name='login'),
path('ilogout/',views.ilogout,name='ilogout'),
path('order/',views.OrDer,name='OrDer'),
path('change/',views.change,name='change'),


]
