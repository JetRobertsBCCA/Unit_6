"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.views import hello_view, roll_view, warmup1_view, warmup2_view, warmup3_view, warmup4_view

urlpatterns = [
    path("hello/", hello_view),
    path('admin/', admin.site.urls),
    path("roll/<int:sides>", roll_view),
    path("warmup1/<int:n>", warmup1_view),
    path("warmup2_view/<str:input_str>", warmup2_view),
    path("warmup3_view/<str:input_str>", warmup3_view),
    path("warmup4_view/<int:a>/<int:b>/<int:c>/", warmup4_view)
    #can do with more than just one. Can hame something like "roll/<int:lo>/<int:high>' and then just pass both values in to the view"
]
