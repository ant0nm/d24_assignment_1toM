# Generated by Django 2.1.7 on 2019-03-07 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_founded', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_founded', models.IntegerField()),
                ('national_animal', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_founded', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provinces', to='OneToMany2.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('year_built', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residences', to='OneToMany2.City')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='residence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='OneToMany2.Residence'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='OneToMany2.Province'),
        ),
    ]
