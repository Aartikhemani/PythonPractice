# Generated by Django 4.1.1 on 2023-06-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_pythonmeaning_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqlquestions',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
