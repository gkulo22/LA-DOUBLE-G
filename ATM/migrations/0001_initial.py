# Generated by Django 5.1.2 on 2024-10-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ATM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('five_gel_amount', models.IntegerField()),
                ('ten_gel_amount', models.IntegerField()),
                ('twenty_gel_amount', models.IntegerField()),
                ('fifty_gel_amount', models.IntegerField()),
                ('hundred_gel_amount', models.IntegerField()),
                ('two_hundred_gel_amount', models.IntegerField()),
            ],
        ),
    ]
