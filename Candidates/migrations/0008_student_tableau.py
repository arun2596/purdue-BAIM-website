# Generated by Django 3.0.4 on 2020-03-26 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0007_auto_20200326_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='tableau',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
    ]
