# Generated by Django 3.0 on 2019-12-18 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_transacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
