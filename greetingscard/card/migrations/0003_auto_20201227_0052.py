# Generated by Django 3.0.5 on 2020-12-27 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_cardinfo_machine_learning_generated_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardinfo',
            name='Machine_Learning_Generated_Message',
        ),
        migrations.RemoveField(
            model_name='cardinfo',
            name='Short_Message',
        ),
    ]