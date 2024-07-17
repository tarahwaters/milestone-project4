from django.db import models

# code for bespoke model adapted from https://katie-harte-art.onrender.com/commissions/
GIFT_RECIPIENT_CHOICES = (
    ('', 'Is this a gift for yourself or someone else? *'),
    ('1', 'Myself'),
    ('2', 'Someone else')
)

OCCASION_CHOICES = (
    ('', 'What sort of occasion is the collage for?*'),
    ('Birthday', 'Birthday'),
    ('Significant Milestone', 'Significant Milestone'),
    ('New Home', 'New Home'),
    ('Anniversary', 'Anniversary'),
    ('Wedding', 'Wedding'),
    ('Retirement', 'Retirement'),
    ('Not sure', 'Not sure'),
    ('Other', 'Other - details in comments below'),
)

WISHES_CHOICES = (
    ('', 'How many wishes would you like (all 30 x 30cm)?*'),
    ('1', '1'),
    ('4', '4'),
    ('6', '6'),
    ('9', '9')
)

class Bespoke(models.Model):
    class Meta:
        verbose_name_plural = 'Bespoke Collages'

    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, null=False, blank=False)
    gift_recipient = models.CharField(max_length=30, choices=GIFT_RECIPIENT_CHOICES,
                                      default='Is this a gift for yourself or someone else?*')
    occasion = models.CharField(max_length=30, choices=OCCASION_CHOICES,
                                default='What sort of occasion is the collage for?*')
    wishes = models.CharField(max_length=40, choices=WISHES_CHOICES,
                              default='How many wishes would you like (all 30 x 30cm)?*')
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email