# Generated by Django 4.0.6 on 2022-08-06 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_teacher_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='student_profile_imgs/'),
        ),
    ]