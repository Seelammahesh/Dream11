# Generated by Django 4.2.7 on 2023-11-21 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_user_alter_team_captain_name_alter_team_name'),
        ('matches', '0006_alter_match_team1_alter_match_team2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='teams.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='teams.team'),
        ),
    ]
