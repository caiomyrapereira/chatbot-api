# Generated by Django 4.0.3 on 2023-10-31 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_api', '0004_alter_data_description_alter_data_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pergunta',
        ),
        migrations.DeleteModel(
            name='Resposta',
        ),
    ]
