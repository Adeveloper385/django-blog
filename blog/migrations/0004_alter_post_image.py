# Generated by Django 3.2.7 on 2021-09-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(max_length=1000, verbose_name='Image'),
        ),
    ]
