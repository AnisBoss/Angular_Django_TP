"""notable_django URL Configuration

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
from django.contrib import admin
from api.resources import NoteResource,TabletResource,SmartphoneResource,ProductsRessource,UserResource,SalesDetailsRessource
note_resource = NoteResource()
tablet_resource = TabletResource()
smartphone_resource=SmartphoneResource()
products_resource=ProductsRessource()
user_ressource=UserResource()
sales_ressource=SalesDetailsRessource()
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^api/',include(note_resource.urls)),
	url(r'^api/', include(tablet_resource.urls)),
        url(r'^api/',include(smartphone_resource.urls)),
	url(r'^api/',include(products_resource.urls)),
	url(r'^api/',include(user_ressource.urls)),
	url(r'^api/',include(sales_ressource.urls)),
]
