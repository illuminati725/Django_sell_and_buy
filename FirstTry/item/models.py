from django.db import models
from account.models import UserInfo
from django.contrib.auth.models import User
from django.utils.timezone import now


class item(models.Model) :
    CATEGORY_CHOICES=(
        ('E','Electronics'),
        ('C','Clothing'),
        ('F','Furniture'),
        ('A','Accessories'),
        ('a','Automobile'),
        ('S','Stationary'),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    item_name = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255,choices=CATEGORY_CHOICES)
    description = models.TextField()
    price_expected = models.IntegerField()
    old = models.IntegerField()
    post_date_time = models.DateTimeField(default = now, editable = False)
    item_image = models.ImageField(upload_to = 'item_images/',default='noitem.jpg',blank=True)


    def __str__(self):
        return self.user.username+" "+self.category
