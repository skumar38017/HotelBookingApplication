# Generated by Django 4.2.11 on 2024-04-09 12:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(default='', max_length=200)),
                ('dob', models.DateField(max_length=10)),
                ('status', models.IntegerField(default=0)),
                ('role', models.CharField(default='customer', max_length=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_img', models.CharField(max_length=100)),
                ('hotel_city', models.CharField(max_length=100)),
                ('hotel_address', models.CharField(max_length=100)),
                ('hotel_rating', models.IntegerField(default=3)),
                ('hotel_price', models.FloatField(max_length=15)),
                ('hotel_discount', models.FloatField(max_length=15)),
                ('hotel_old_price', models.FloatField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=100)),
                ('room_img', models.CharField(max_length=100)),
                ('room_price', models.FloatField(max_length=15)),
                ('room_bed', models.IntegerField(default=0)),
                ('room_bath', models.IntegerField(default=0)),
                ('room_wifi', models.CharField(max_length=5)),
                ('room_description', models.CharField(max_length=200)),
                ('room_rating', models.IntegerField(default=2)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='hotelbooking.customer')),
                ('hotel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='hotelbooking.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('checkin', models.DateTimeField(verbose_name='checkin time')),
                ('checkout', models.DateTimeField(verbose_name='checkout time')),
                ('adult', models.IntegerField(default=0)),
                ('child', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='hotelbooking.customer')),
            ],
        ),
    ]
