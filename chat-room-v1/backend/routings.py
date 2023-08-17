from django.urls import re_path
from web.consumers import ChatConsumer #稍後自行建立的consumers.py

websocket_urlpatterns =[
	re_path(r'chat/', ChatConsumer.as_asgi()),
]
