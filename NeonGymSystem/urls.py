"""NeonGymSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from clients.views import *
# from users.views import *
from memberships.views import *
from gyms.views import *
from branches.views import branchData
from service.views import *
from employees.views import employeesData, testPost
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='APIs Documention')


clientsRoute = routers.DefaultRouter()
clientsRoute.register("",clients,basename='clients')


employeesRoute = routers.DefaultRouter()
employeesRoute.register("",employeesData,basename='employees')

branchRoute= routers.DefaultRouter();
branchRoute.register("",branchData,base_name='branch')

serviceRoute= routers.DefaultRouter();
serviceRoute.register("",ServiceView,base_name='service')

packageRoute = routers.DefaultRouter();
packageRoute.register("",PackageView);

priceRoute = routers.DefaultRouter();
priceRoute.register("",PriceView)
# admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include(clientsRoute.urls)),
    path('employees/', include(employeesRoute.urls)),
    path('memberships/', ListAndCreateMemberships.as_view()),
    path('test/', testPost.as_view()),
    path('memberships/<pk>/', RetiveAndUpdateMemberships.as_view()),
    path('memberships-payments/', ListAndCreateMembershipsPayments.as_view()),
    path('memberships-payments/<pk>/', RetiveAndUpdateMembershipsPayments.as_view()),
    # path('users/', listUser.as_view()),
    path('gyms/<pk>/', listGym.as_view()),
    path('branches/', include(branchRoute.urls)),
    path('services/', include(serviceRoute.urls)),
    path('packages/',include(packageRoute.urls)),
    path('prices/',include(priceRoute.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('apis-documention', schema_view),
]
