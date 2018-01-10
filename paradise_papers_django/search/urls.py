from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    Index,
    ResultPage,
    NodeDetail,
)


urlpatterns = [
                  url(r'^$', Index.as_view(), name='index'),
                  url('lookup', ResultPage.as_view(), name='lookup'),
                  url(r'^(?P<slug>[\w-]+)/(?P<node_id>[0-9]+)$', NodeDetail.as_view(), name='nodes'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
