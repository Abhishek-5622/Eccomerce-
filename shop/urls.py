from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("shop/", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("help/", views.help, name="Help"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("signup/",views.handlesignup , name='handlesignup'),
    path("login/",views.handlelogin , name='handlelogin'),
    path("logout/",views.handlelogout , name='handlelogout'),
    path("about/logout/",views.handlelogout , name='handlelogout'),
    path("tracker/logout/",views.handlelogout , name='handlelogout'),
    path("contact/logout/",views.handlelogout , name='handlelogout'),
    path("help/logout/",views.handlelogout , name='handlelogout'),

]
