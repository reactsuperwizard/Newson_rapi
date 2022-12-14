# Generated by Django 3.2 on 2022-07-18 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20220718_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='connection_requests_per_day_from',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='connection_requests_per_day_to',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='emails_per_day_from',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='emails_per_day_to',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='inmails_per_day_from',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='inmails_per_day_to',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='messages_per_day_from',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='messages_per_day_to',
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='connection_requests_per_day_from',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='connection_requests_per_day_to',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='emails_per_day_from',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='emails_per_day_to',
            field=models.IntegerField(default=15),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='inmails_per_day_from',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='inmails_per_day_to',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='messages_per_day_from',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='messages_per_day_to',
            field=models.IntegerField(default=15),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='has_permission_to_change_linkedin_account_limits',
            field=models.BooleanField(default=True),
        ),
    ]
