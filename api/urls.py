from django.conf.urls import url

from api import views

urlpatterns = [
    url(
        regex=r'^photos/$',
        view=views.PhotoList.as_view(),
        name='list'
    )
]
