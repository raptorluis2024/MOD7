from django.test import TestCase
import datetime as dt

from django.utils import timezone
# Create your tests here.


now = timezone.now()
current_date = dt.date.today()
print(current_date, now)