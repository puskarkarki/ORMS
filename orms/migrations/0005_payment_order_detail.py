# Generated by Django 3.2 on 2021-04-09 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orms', '0004_alter_orderdetail_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orms.orderdetail'),
        ),
    ]
