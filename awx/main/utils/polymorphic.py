
from django.contrib.contenttypes.models import ContentType


def build_polymorphic_ctypes_map(cls):
    # {'1': 'unified_job', '2': 'Job', '3': 'project_update', ...}
    mapping = {}
    for ct in ContentType.objects.filter(app_label='main'):
        ct_model_class = ct.model_class()
        if ct_model_class and issubclass(ct_model_class, cls):
            mapping[ct.id] = ct_model_class._camel_to_underscore(ct_model_class.__name__)
    return mapping
