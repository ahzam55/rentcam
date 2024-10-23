# Generated by Django 5.1.1 on 2024-10-18 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guest', '0004_rename_district_id_user_district_and_more'),
        ('rentholder', '0002_rename_brand_id_product_brand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rentholder_id', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('requested_date', models.DateField()),
                ('bill_id', models.IntegerField()),
                ('booking_status', models.CharField(max_length=50)),
                ('login', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guest.login')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentholder.product')),
            ],
        ),
        migrations.CreateModel(
            name='bookingmaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('booking_date', models.DateField()),
                ('booking_status', models.CharField(max_length=50)),
                ('rentholder_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guest.login')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rentholder_id', models.IntegerField()),
                ('payment_date', models.DateField()),
                ('adv_amount', models.FloatField()),
                ('bal_amount', models.FloatField()),
                ('bill_no', models.IntegerField()),
                ('payment_status', models.CharField(max_length=50)),
                ('login_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guest.login')),
            ],
        ),
    ]