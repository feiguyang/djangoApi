# Generated by Django 2.1.4 on 2018-12-31 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181228_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TaskModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='taskModule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TaskModule'),
        ),
    ]
