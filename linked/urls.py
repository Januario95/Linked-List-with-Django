from django.urls import path

from .views import (
    index, linked_list_api,
    remove_node
)

app_name = 'linked'


urlpatterns = [
    path('', index, name='index'),
    path('linked_list_api/', linked_list_api),
    path('remove_node/', remove_node),
]
