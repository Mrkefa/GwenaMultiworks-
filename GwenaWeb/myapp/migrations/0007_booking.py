# Generated by Django 4.0 on 2024-12-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_imagemodel_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_info', models.CharField(max_length=200)),
                ('service_date', models.DateField()),
                ('service_type', models.CharField(max_length=100)),
                ('budget', models.CharField(max_length=100)),
            ],
        ),
    ]
