import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_try.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from item.models import item
from account.models import UserLoginDetails
from faker import Faker

fakegen=Faker()

def populate(N=10):
    fake_category_list=[
    "Music Item","Books","Cars","Laptop","Furniture"
    ]
    fake_user_name_list=UserLoginDetails.objects.order_by('user_name')
    for i in range(N):
        fake_user_name=random.choice(fake_user_name_list)
        fake_description=fakegen.text()
        fake_name=fakegen.name()
        fake_category=random.choice(fake_category_list)
        fake_old=10
        fake_price_expected=100

        itm=item.objects.get_or_create(
                                        user_name=fake_user_name,
                                        description=fake_description[:100],
                                        name=fake_name,
                                        catagory=fake_category,
                                        old=fake_old,
                                        price_expected=fake_price_expected
                                    )

if __name__=='__main__':
    print('populating script!')
    populate()
    print('populating complete!')
