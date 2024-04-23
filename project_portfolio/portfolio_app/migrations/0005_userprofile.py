# Generated by Django 5.0.4 on 2024-04-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_alter_projectdetailmodel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
