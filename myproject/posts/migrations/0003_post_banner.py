# Generated by Django 5.1.6 on 2025-02-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_data_post_published_date_alter_post_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]
