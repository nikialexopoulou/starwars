# Generated by Django 5.2.3 on 2025-06-28 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('rotation_period', models.CharField(blank=True, max_length=50, null=True)),
                ('orbital_period', models.CharField(blank=True, max_length=50, null=True)),
                ('diameter', models.CharField(blank=True, max_length=50, null=True)),
                ('climate', models.CharField(blank=True, max_length=100, null=True)),
                ('gravity', models.CharField(blank=True, max_length=100, null=True)),
                ('terrain', models.CharField(blank=True, max_length=100, null=True)),
                ('surface_water', models.CharField(blank=True, max_length=50, null=True)),
                ('population', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('height', models.CharField(blank=True, max_length=10, null=True)),
                ('mass', models.CharField(blank=True, max_length=10, null=True)),
                ('hair_color', models.CharField(blank=True, max_length=50, null=True)),
                ('skin_color', models.CharField(blank=True, max_length=50, null=True)),
                ('eye_color', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_year', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('homeworld', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='residents', to='starwars_api.planet')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('classification', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('average_height', models.IntegerField(blank=True, null=True)),
                ('skin_colors', models.CharField(blank=True, max_length=255, null=True)),
                ('hair_colors', models.CharField(blank=True, max_length=255, null=True)),
                ('eye_colors', models.CharField(blank=True, max_length=255, null=True)),
                ('average_lifespan', models.IntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('homeworld', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='species_planet', to='starwars_api.planet')),
                ('people', models.ManyToManyField(blank=True, to='starwars_api.character')),
            ],
        ),
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=200, null=True)),
                ('cost_in_credits', models.CharField(blank=True, max_length=50, null=True)),
                ('length', models.CharField(blank=True, max_length=50, null=True)),
                ('max_atmosphering_speed', models.CharField(blank=True, max_length=50, null=True)),
                ('crew', models.CharField(blank=True, max_length=50, null=True)),
                ('passengers', models.CharField(blank=True, max_length=50, null=True)),
                ('cargo_capacity', models.CharField(blank=True, max_length=50, null=True)),
                ('consumables', models.CharField(blank=True, max_length=50, null=True)),
                ('hyperdrive_rating', models.CharField(blank=True, max_length=10, null=True)),
                ('MGLT', models.CharField(blank=True, max_length=10, null=True)),
                ('starship_class', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('pilots', models.ManyToManyField(blank=True, related_name='starships', to='starwars_api.character')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=200, null=True)),
                ('cost_in_credits', models.CharField(blank=True, max_length=50, null=True)),
                ('length', models.CharField(blank=True, max_length=50, null=True)),
                ('max_atmosphering_speed', models.CharField(blank=True, max_length=50, null=True)),
                ('crew', models.CharField(blank=True, max_length=50, null=True)),
                ('passengers', models.CharField(blank=True, max_length=50, null=True)),
                ('cargo_capacity', models.CharField(blank=True, max_length=50, null=True)),
                ('consumables', models.CharField(blank=True, max_length=50, null=True)),
                ('vehicle_class', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('pilots', models.ManyToManyField(blank=True, related_name='vehicles_piloted', to='starwars_api.character')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('episode_id', models.IntegerField(blank=True, null=True)),
                ('opening_crawl', models.TextField(blank=True, null=True)),
                ('director', models.CharField(blank=True, max_length=100, null=True)),
                ('producer', models.CharField(blank=True, max_length=200, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('characters', models.ManyToManyField(blank=True, related_name='films', to='starwars_api.character')),
                ('planets', models.ManyToManyField(blank=True, related_name='films', to='starwars_api.planet')),
                ('species', models.ManyToManyField(blank=True, related_name='films', to='starwars_api.species')),
                ('starships', models.ManyToManyField(blank=True, related_name='films', to='starwars_api.starship')),
                ('vehicles', models.ManyToManyField(blank=True, related_name='films', to='starwars_api.vehicle')),
            ],
        ),
    ]
