# Generated by Django 3.1.3 on 2020-11-16 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20201116_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_owner', to='customers.customer'),
        ),
    ]
