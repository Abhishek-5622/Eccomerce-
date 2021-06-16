# Generated by Django 3.0.8 on 2020-08-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=1000)),
                ('pub_date', models.DateField()),
                ('prize', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]