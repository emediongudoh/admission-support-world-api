# Generated by Django 4.0.6 on 2022-08-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_course_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('query', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '8. ReplyContact',
            },
        ),
    ]
