# Generated by Django 4.2.5 on 2023-09-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usosLearning', '0011_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.IntegerField(),
        ),
    ]
