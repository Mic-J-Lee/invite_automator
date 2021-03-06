# Generated by Django 2.2.2 on 2019-06-18 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('successful', models.BooleanField()),
                ('github_handle', models.CharField(max_length=200)),
                ('zapier_payload', models.TextField()),
                ('github_response', models.TextField()),
            ],
        ),
    ]
