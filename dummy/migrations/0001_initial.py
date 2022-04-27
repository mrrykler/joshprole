# Generated by Django 4.0.4 on 2022-04-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('itemcount', models.IntegerField()),
                ('cost', models.FloatField()),
                ('slot', models.IntegerField()),
                ('odate', models.DateField()),
                ('purchase', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=1)),
                ('price', models.FloatField()),
            ],
        ),
    ]