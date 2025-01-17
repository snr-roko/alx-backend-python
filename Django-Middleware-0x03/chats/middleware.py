import logging
from datetime import datetime

logging.basicConfig(filename='requests.log', level=logging.INFO, format='%(message)s', filemode='a')
logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', 'Anonymous')
        message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logger.info(message)
        response = self.get_response(request)
        return response