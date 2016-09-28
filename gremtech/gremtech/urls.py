from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin

from .admin import gremtech_admin_site

handler400 = 'website.views.handler400'
handler403 = 'website.views.handler403'
handler404 = 'website.views.handler404'
handler500 = 'website.views.handler500'

urlpatterns = [
    url(r'^deus_ex_machina/', gremtech_admin_site.urls),
]

urlpatterns += i18n_patterns(
    url(r'', include('website.urls')),
    prefix_default_language=False
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
