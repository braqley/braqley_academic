# Generated by Django 2.2.2 on 2019-06-20 15:12

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20190618_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='aj101fall19post',
            name='coauthors',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AJ User8', 'AJ User8'), ('AJ User11', 'AJ User11'), ('AJ User7', 'AJ User7')], default='', max_length=27),
        ),
    ]
