# Generated by Django 2.2.2 on 2019-06-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190619_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='course',
            field=models.CharField(choices=[('AJ101 Fall 2019', 'AJ101 Fall 2019'), ('PS324 Fall 2019', 'PS324 Fall 2019')], default='', max_length=255),
        ),
    ]
