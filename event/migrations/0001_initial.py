# Generated by Django 2.0 on 2020-01-19 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('provider', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(max_length=100)),
                ('discountPrice', models.CharField(max_length=100)),
                ('discountRate', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
