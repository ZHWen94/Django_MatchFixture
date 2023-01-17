from django.urls import path

from country.views.create_country_view import CreateCountryView
from country.views.get_all_country_view import GetAllCountryView
from country.views.update_country_view import UpdateCountryView

urlpatterns = [
    path('create', CreateCountryView.as_view()),
    path('get_all', GetAllCountryView.as_view()),
    path("update", UpdateCountryView.as_view())
]