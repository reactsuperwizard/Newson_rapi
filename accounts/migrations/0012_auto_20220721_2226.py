# Generated by Django 3.2 on 2022-07-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_importlinkedinaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkedinaccount',
            name='endorse_top_5_skills_per_day_from',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='endorse_top_5_skills_per_day_to',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='follow_per_day_from',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='follow_per_day_to',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='like_3_posts_per_day_from',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='linkedinaccount',
            name='like_3_posts_per_day_to',
            field=models.IntegerField(default=20),
        ),
    ]
