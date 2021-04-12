# Generated by Django 3.2 on 2021-04-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orms', '0006_alter_payment_order_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order_detail',
        ),
        migrations.AddField(
            model_name='payment',
            name='order_detail',
            field=models.ManyToManyField(to='orms.OrderDetail'),
        ),
    ]
