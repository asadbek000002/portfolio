from django.urls import path
from spravchnik.index import registration, login_view, logout_user, login_photo
from spravchnik.views_.fikr_blog import home, idea_blog
from spravchnik.views_.post import photo, important_events, events_detail
from spravchnik.views_.contact import contact_create, room_, checkview, send, getMessages, get_room

urlpatterns = [
    path('', home, name='home'),
    path('registration/', registration, name='registration'),
    path('login-photo/', login_photo, name='login_photo'),
    path('login/', login_view, name='login'),
    path('logout/', logout_user, name='logout'),
    path('important-events/', important_events, name='important_events'),
    path('important-events/<int:id>/', events_detail, name='events_detail'),
    path('thoughts/', idea_blog, name='idea_blog'),
    path('contact/', contact_create, name='contact'),
    path('photos/', photo, name='photo'),


    # message
    path('room-list/', get_room, name='get_room'),
    path('<str:room>/', room_, name='room'),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),

]