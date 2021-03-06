# Generated by Django 2.1.7 on 2019-02-26 16:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chromosome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('change', models.CharField(max_length=200)),
                ('pathogenic', models.NullBooleanField()),
                ('submitter', models.CharField(default='unknown', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('chromosome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='var_db.Chromosome')),
            ],
        ),
    ]
