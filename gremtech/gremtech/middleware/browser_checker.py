import re

from django.shortcuts import redirect


class BrowserCheckerMiddleware():

    IE_PATTERN = '(?i)msie [2-9]'

    def __init__(self, target_view=False):
        self._target_view = target_view

    def process_request(self, request):
        if request.method == 'GET' and not request.is_ajax():
            old_ie_match = re.search(
                self.IE_PATTERN, request.META['HTTP_USER_AGENT']
            )

            if old_ie_match and not self._target_view:
                # browser match, not browsers page
                return redirect('website:old_browser')
            elif not old_ie_match and self._target_view:
                # browsers don't match, browsers page
                return redirect('website:index')
