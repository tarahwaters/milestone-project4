import json
from django.core.management.base import BaseCommand
from faqs.models import FAQ
from datetime import datetime

class Command(BaseCommand):
    help = 'Load FAQs from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The file path to the JSON file.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                created_at = datetime.fromisoformat(item['created_at'].replace('Z', '+00:00'))
                FAQ.objects.create(
                    question=item['question'],
                    answer=item['answer'],
                    category=item['category'],
                    created_at=created_at
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded FAQs'))