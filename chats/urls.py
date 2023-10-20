from django.urls import path
from chats.views import ver_conversaciones, iniciar_chat, ver_chat
from chats.views import EliminarChatView

urlpatterns = [
    path('', ver_conversaciones, name='ver_conversaciones'),
    path('nuevo/', iniciar_chat, name='nuevo_chat'),
    path('chat/<int:id>/mensajes/', ver_chat, name='ver_chat'),
    path('chat/<int:pk>/eliminar/', EliminarChatView.as_view(), name='borrar_chat'),
]