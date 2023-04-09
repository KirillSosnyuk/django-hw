# Generated by Django 4.1.6 on 2023-02-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.URLField(default=None)),
                ('price', models.IntegerField(default=None)),
                ('release_date', models.DateField(default=None)),
                ('lte_exists', models.BooleanField(default=None)),
                ('slug', models.SlugField(default=None)),
            ],
        ),
    ]