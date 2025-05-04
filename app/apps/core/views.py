# app/apps/core/views.py
from django.http import JsonResponse
from django.views import View
from .models import Item

class HealthCheckView(View):
    def get(self, request):
        # Simple healthcheck endpoint that also verifies DB connection
        item_count = Item.objects.count()
        return JsonResponse({
            'status': 'healthy',
            'database': 'connected',
            'item_count': item_count
        })