# Generated by Django 4.0.6 on 2022-07-19 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_tag', models.CharField(max_length=50)),
                ('uid', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_main', models.CharField(max_length=50)),
                ('characters_obtained', models.IntegerField()),
                ('days_played', models.IntegerField()),
            ],
        ),
    ]