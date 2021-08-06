from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "This command help you to know gender count inside db."

    def add_arguments(self, parser):
        parser.add_argument("--gender", help="input gender")

    def handle(self, *args, **options):
        gender = options.get("gender")
        self.stdout.write(
            self.style.SUCCESS(User.objects.filter(gender=f"{gender}").count())
        )
