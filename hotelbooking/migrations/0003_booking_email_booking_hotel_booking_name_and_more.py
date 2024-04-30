# Generated by Django 4.2.11 on 2024-04-12 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0002_alter_room_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookhotel', to='hotelbooking.hotel'),
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookroom', to='hotelbooking.room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='specialrequest',
            field=models.CharField(default='', max_length=200),
        ),
    ]
