# Generated by Django 3.2 on 2022-09-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_alter_campaignsequence_wait_for_connection_request_to_be_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='color',
            field=models.CharField(default='#2A83EC', max_length=7),
        ),
        migrations.AddField(
            model_name='label',
            name='default_label',
            field=models.BooleanField(default=False),
        ),
    ]
