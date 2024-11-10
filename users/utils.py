import json
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def load_json(request):
    """
    Helper untuk memuat JSON dari request body.
    Mengembalikan tuple (data, error).
    Jika JSON valid, error akan None, dan jika invalid, error berisi JsonResponse.
    """
    try:
        logger.info(request.body)
        data = json.loads(request.body)
        return data, None
    except json.JSONDecodeError as e:
        return None, JsonResponse({"error": f"Invalid JSON data, {e}"}, status=400)
