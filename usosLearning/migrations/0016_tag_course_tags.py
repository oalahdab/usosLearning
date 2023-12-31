# Generated by Django 4.2.5 on 2023-10-05 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usosLearning', '0015_alter_course_imageurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(to='usosLearning.tag'),
        ),
    ]
