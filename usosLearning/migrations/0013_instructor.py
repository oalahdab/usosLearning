# Generated by Django 4.2.5 on 2023-10-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usosLearning', '0012_alter_course_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('imageURL', models.CharField(max_length=255)),
                ('socialMediaLink1', models.CharField(max_length=255)),
                ('socialMediaLink2', models.CharField(max_length=255)),
            ],
        ),
    ]
