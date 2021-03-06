# Generated by Django 2.2.1 on 2019-11-07 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price_expected', models.IntegerField()),
                ('old', models.IntegerField()),
                ('post_date_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
