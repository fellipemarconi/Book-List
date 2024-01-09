# Generated by Django 5.0.1 on 2024-01-09 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=30)),
            ],
        ),
    ]
