from django.urls import path
from spravchnik.index import index2, contact
from spravchnik.views_.fikr_blog import home, idea_blog
from spravchnik.views_.post import photo, important_events, events_detail
from spravchnik.views_.contact import contact_create

urlpatterns = [
    path('', home, name='home'),
    path('important-events/', important_events, name='important_events'),
    path('important-events/<int:id>/', events_detail, name='events_detail'),
    path('thoughts/', idea_blog, name='idea_blog'),
    path('contact/', contact_create, name='contact_create'),
    path('photos/', photo, name='photo'),
    path('contact/', contact, name='contact'),
]