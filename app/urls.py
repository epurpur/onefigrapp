from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from . import views

app_name = 'app'
urlpatterns = [
	path('', views.index, name='index'),
	path('tools/', views.tools, name='tools'),
	path('journalsByDiscipline/', views.journalsByDiscipline, name='journalsByDiscipline'),
	# path('journalsByProvider/', views.journalsByProvider, name='journalsByProvider'),
	# path('providersByMetric/', views.providersByMetric, name='providersByMetric'),
	path('disciplines_list/', views.disciplines_list, name='discipline_list'),
	path('chart_data/<str:discipline>/', views.chart_data, name='chart_data'),
	path('journals_and_disciplines_map/', views.get_journals_and_disciplines_map, name='journals_and_disciplines_map'),

    path('login/', auth_views.LoginView.as_view(template_name="app/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]