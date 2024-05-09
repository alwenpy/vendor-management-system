from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder
from django.db.models import Avg
from vendor_management.models import Vendor
from vendor_management import models


@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, created, **kwargs):
    vendor = instance.vendor
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    acknowledged_pos = completed_pos.filter(acknowledgment_date__isnull=False)
    fulfilled_pos = completed_pos.filter(quality_rating__isnull=False)

    on_time_delivery_rate = (completed_pos.filter(delivery_date__lte=models.F('delivery_date')).count() / completed_pos.count()) * 100
    vendor.on_time_delivery_rate = on_time_delivery_rate

    quality_rating_avg = fulfilled_pos.aggregate(Avg('quality_rating'))['quality_rating__avg']
    vendor.quality_rating_avg = quality_rating_avg if quality_rating_avg is not None else 0

    average_response_time = acknowledged_pos.aggregate(Avg(models.F('acknowledgment_date') - models.F('issue_date')))['acknowledgment_date__avg']
    vendor.average_response_time = average_response_time.total_seconds() / 3600 if average_response_time is not None else 0

    fulfillment_rate = (fulfilled_pos.count() / completed_pos.count()) * 100
    vendor.fulfillment_rate = fulfillment_rate

    vendor.save()