import logging
from datetime import datetime

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