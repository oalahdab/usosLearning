# Generated by Django 4.2.5 on 2023-10-03 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usosLearning', '0013_instructor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='subject',
            new_name='subjectId',
        ),
    ]
