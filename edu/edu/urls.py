"""edu_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.views.generic.base import TemplateView
import xadmin
from rest_framework.documentation import include_docs_urls

from rest_framework.routers import DefaultRouter
from comment.views import InfopackfromViewset,TableViewset,Table3View,Table4View,Table5View
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from users.views import UserViewset

router = DefaultRouter()
# router.register(r'table2',TableViewset)
router.register(r'register',UserViewset)

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^',include(router.urls)),
    url(r'^index/$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^login/',obtain_jwt_token),
    url(r'^auth/refresh/',refresh_jwt_token),
    url(r'^table/',TableViewset.as_view()),
    url(r'^table3/',Table3View.as_view()),
    url(r'^table4/',Table4View.as_view()),
    url(r'^table5/',Table5View.as_view())
]
