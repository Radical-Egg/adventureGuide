# Generated by Django 3.1.3 on 2020-11-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('questTitle', models.CharField(max_length=200, verbose_name='Quest Title')),
                ('questContent', models.TextField(verbose_name='Quest Content')),
            ],
            options={
                'ordering': ['createdOn'],
            },
        ),
    ]