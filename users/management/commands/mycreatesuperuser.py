from users.models import User
import os
from django.core.management import BaseCommand

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		user = User.objects.create(
			email=os.getenv('ADMIN_EMAIL'),
			is_staff=True,
			is_superuser=True
		)
		user.set_password(os.getenv('ADMIN_PASSWORD'))
		user.save()