# Generated by Django 5.1.1 on 2024-10-11 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0004_brand'),
        ('guest', '0003_rentholder'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('rent_price_perday', models.FloatField()),
                ('remarks', models.CharField(max_length=50)),
                ('product_status', models.CharField(max_length=50)),
                ('brand_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.brand')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.categories')),
                ('login_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guest.login')),
            ],
        ),
    ]
