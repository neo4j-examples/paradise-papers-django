from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url('lookup', views.lookup, name='lookup'),
                  url(r'^(?P<node_id>[0-9]+)$', views.nodes, name='nodes'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
