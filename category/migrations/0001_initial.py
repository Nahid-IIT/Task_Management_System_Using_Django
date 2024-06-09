# Generated by Django 5.0.6 on 2024-06-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('task', models.ManyToManyField(to='task.task')),
            ],
        ),
    ]
