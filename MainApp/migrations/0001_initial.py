# Generated by Django 4.2.6 on 2023-10-29 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TRF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=24)),
                ('Surname', models.CharField(max_length=24)),
                ('Surname1', models.CharField(max_length=24)),
            ],
        ),
    ]
