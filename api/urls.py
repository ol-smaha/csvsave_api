from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('all-users/', views.AllUsersView.as_view({'get': 'list'}), name='all_users'),
    path('date-users/<str:registration_date>', views.DateUsersView.as_view({'get': 'list'}), name='date_users'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
