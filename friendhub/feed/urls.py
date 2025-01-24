from django.urls import path

from .views import Feed, CreateChirp, ChirpDetail

urlpatterns = [
    path('', Feed.as_view(), name='home'),
    path('post/chirp', CreateChirp.as_view(), name='create_chirp'),
    path('detail/chirp/<int:pk>', ChirpDetail.as_view(), name='detail_chirp')

]

