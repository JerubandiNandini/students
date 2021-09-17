# Generated by Django 3.2.6 on 2021-09-09 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('rollnumber', models.AutoField(primary_key=True, serialize=False)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='student', to='students.college')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
                ('mark', models.IntegerField(max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mark', to='students.student')),
            ],
        ),
    ]