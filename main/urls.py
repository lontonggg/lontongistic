from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, remove_item, increase_item_amount, decrease_item_amount

app_name = 'main'

urlpatterns = [
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'), 
    path('create-product', create_product, name='create_product'),
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('remove_item/<int:id>/', remove_item, name='remove_item'),
    path('increase_item_amount/<int:id>/', increase_item_amount, name='increase_item_amount'),
    path('decrease_item_amount/<int:id>/', decrease_item_amount, name='decrease_item_amount')
]