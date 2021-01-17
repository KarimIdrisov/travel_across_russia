from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from app.views import TourView, CountryView, CityView, HotelView, AirlineView, InsuranceView, DocumentView, \
    FavouriteTourView, UserProfileView, TouristView

router = SimpleRouter()
router.register('tours', TourView)  # ?city=CITY_NAME & country=COUNTRY_NAME & count_days=7
router.register('tourists', TouristView)
router.register('document', DocumentView)  # only GET and PATCH
router.register('fav-tours', FavouriteTourView)  # /fav-tour/TOUR_ID/ - удаление
router.register('countries', CountryView)
router.register('cities', CityView)  # ?country=COUNTRY_ID, или ?country_name=Россия
router.register('hotels', HotelView)  # ?city=CITY_NAME & country=COUNTRY_NAME & type_of_food=1
router.register('airlines', AirlineView)
router.register('insurances', InsuranceView)

urlpatterns = [
    path('user-profile/', UserProfileView.as_view())
]

# регистрация /auth/users/ POST (username и password)
# логин /auth/jwt/create/ POST (username и password) вернет (access, refresh)

urlpatterns += router.urls
