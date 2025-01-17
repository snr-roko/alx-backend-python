import logging
from datetime import datetime, time
from django.http import HttpResponseForbidden
from django.utils import timezone

logging.basicConfig(
    filename='requests.log',
    level=logging.INFO,
    format='%(message)s',
    filemode='a',
)
logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = self._get_user(request)
        
        message = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - User: {user} - Path: {request.path}"
        
        logger.info(message)
        
        response = self.get_response(request)
        return response

    def _get_user(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated:
            return request.user.email
        return "Anonymous"
    

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lower_bound_time = time(9, 0, 0) 
        upper_bound_time = time(18, 0, 0)
        now = timezone.now()
        time_now = now.time()
        if time_now < lower_bound_time or time_now > upper_bound_time:
            return HttpResponseForbidden("Site not accessible")
        response = self.get_response(request)
        return response