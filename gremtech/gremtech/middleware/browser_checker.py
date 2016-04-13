import re

from django.shortcuts import redirect


class BrowserCheckerMiddleware():

    IE_PATTERN = '(?i)msie [2-9]'

    def process_request(self, request):
        if request.method == 'GET' and not request.is_ajax():
            old_ie_match = re.search(
                self.IE_PATTERN, request.META['HTTP_USER_AGENT']
            )

            if old_ie_match:
                return redirect('website:old_browser')
