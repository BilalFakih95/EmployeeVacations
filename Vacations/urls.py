from django.urls import path

from .views import list_vacations, create_vacation, update_vacation, delete_vacation

app_name = 'vacations'
urlpatterns = [
    # ex: /
    path('', list_vacations, name='list_vacations'),
    # ex: /create/
    path('create', create_vacation, name='create'),
    # # ex: /update/5/
    path('update/<int:id>/', update_vacation, name='update'),
    # # ex: /delete/5
    path('delete/<int:id>/', delete_vacation, name='delete'),
]
