# Generated by Django 2.2.2 on 2019-06-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190612_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='course',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
