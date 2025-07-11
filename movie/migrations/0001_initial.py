# Generated by Django 5.2.3 on 2025-07-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=50)),
                ('movie_actor', models.CharField(max_length=50)),
                ('movie_release_year', models.DateField()),
                ('movie_status', models.CharField(choices=[('Hit', 'Hit'), ('Average', 'Average'), ('Flop', 'Flop')], max_length=20)),
            ],
        ),
    ]
