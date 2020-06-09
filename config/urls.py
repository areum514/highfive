"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from descriptions import views as des_views
from members import views as mem_views
from equipments import views as equ_views
from researches import views as res_views
from publications import views as pub_views
urlpatterns = [
    path('', include("core.urls", namespace="core")),
    path('people/', mem_views.member_page, name="people"),
    path('research/', res_views.research_page, name="research"),
    path('publication/', pub_views.publication_page, name="publication"),
    path('equitment/', equ_views.equitment_page, name="equitment"),


    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
