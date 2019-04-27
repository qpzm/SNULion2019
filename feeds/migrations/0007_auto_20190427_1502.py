# Generated by Django 2.2 on 2019-04-27 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0006_auto_20190427_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_follows', to=settings.AUTH_USER_MODEL),
        ),
    ]
