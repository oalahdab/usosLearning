# Generated by Django 4.2.5 on 2023-09-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usosLearning', '0010_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('lessonCount', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=255)),
                ('imageURL', models.CharField(max_length=255)),
                ('lastUpdate', models.DateTimeField()),
                ('duration', models.TimeField()),
                ('enrollmentCount', models.IntegerField()),
                ('targetAudience', models.CharField(max_length=255)),
                ('videoURL', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
            ],
        ),
    ]
