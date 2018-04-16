from django.conf import settings
from django.conf.urls import patterns

from lazydoc.views import *

urlpatterns = patterns('',
    # functional API
    (r'^hi$', hi),
    (r'^meetingrecord/new$', new_record),

    # static files
    (r'^pdf/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PDF_PATH}),
    (r'^rst/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.RST_PATH}),
    (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.TEMPLATE_IMG_PATH})
)
