# Generated by Django 2.1.1 on 2018-11-12 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0006_auto_20181112_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Gender',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F')], max_length=1),
        ),
    ]
