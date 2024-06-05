from django.db.models import Count

from hipmessageservice.models import CDA


def read_cda() -> list:

    qs = (CDA.objects.filter(is_deleted=False).order_by('value', 'firm').
          values('value', 'comment', 'firm__firm_name_short').annotate(count=Count('value')))

    return list(qs)