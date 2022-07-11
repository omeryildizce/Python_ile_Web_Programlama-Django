# Generated by Django 4.0.6 on 2022-07-11 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(verbose_name='date created')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
    ]
