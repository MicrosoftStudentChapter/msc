from import_export import resources
from .models import event_registration

class EventResource(resources.ModelResource):
    class Meta:
        model = event_registration
