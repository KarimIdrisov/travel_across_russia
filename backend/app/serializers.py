from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, Serializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

import app.signals
from app.models import Tour, Country, City, Hotel, Airline, Insurance, Document, FavouriteTour, Tourist, HotelPhoto, \
    BookedTour


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'is_staff',
                  'access_right', 'document', 'email')


class UserGetUpdateSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class TourSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class TourReceivingSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = (
            'tour_id', 'name', 'price', 'count_days', 'city_name', 'country_name',
            'description', 'food_type')  # + rating, is_favourite


class FavouriteTourSerializer(ModelSerializer):
    class Meta:
        model = FavouriteTour
        fields = ['tour']


class FavouriteTourReceivingSerializer(ModelSerializer):
    class Meta:
        model = FavouriteTour
        fields = ('tour_id', 'name', 'price', 'city_name', 'country_name', 'description')  # + rating


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class AirlineSerializer(ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'


class InsuranceSerializer(ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


class HotelPhotoSerializer(ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ('hotel', 'photo')


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = ('type', 'series', 'number', 'firstname', 'lastname', 'birthdate')


class TouristSerializer(ModelSerializer):
    document = DocumentSerializer()

    class Meta:
        model = Tourist
        fields = ['email', 'document']


class BookedTourSerializer(ModelSerializer):
    tourists = TouristSerializer(many=True)

    class Meta:
        model = BookedTour
        fields = ('tour_id', 'tourists')

    def create(self, validated_data):
        tourists_data = validated_data.pop('tourists')
        booked_tour = BookedTour.objects.create(**validated_data)
        for tourist_data in tourists_data:
            document_data = tourist_data.pop('document')
            document = Document.objects.create(**document_data)

            Tourist.objects.create(booked_tour=booked_tour, document=document, **tourist_data)
        return booked_tour
