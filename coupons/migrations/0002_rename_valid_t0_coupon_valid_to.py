# Generated by Django 4.1.6 on 2023-02-17 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='valid_t0',
            new_name='valid_to',
        ),
    ]