# Generated by Django 4.0.5 on 2022-08-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('attachment', models.FileField(upload_to='photovideos')),
                ('caption', models.TextField(max_length=1000)),
                ('likes', models.CharField(default=0, max_length=1000)),
            ],
        ),
    ]