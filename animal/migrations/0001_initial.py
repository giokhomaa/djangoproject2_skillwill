# Generated by Django 4.2.1 on 2023-09-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(default='animal', max_length=50)),
                ('kind', models.CharField(default='kind', max_length=50)),
                ('color', models.CharField(default='color', max_length=50)),
            ],
        ),
    ]
