# Generated by Django 5.1.7 on 2025-04-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='contracts/')),
                ('raw_text', models.TextField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('key_info', models.TextField(blank=True)),
                ('red_flags', models.TextField(blank=True)),
            ],
        ),
    ]
