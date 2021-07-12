# Generated by Django 3.1.2 on 2020-11-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20201024_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_updated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productreport',
            name='last_updated',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='productreport',
            name='timestamp',
            field=models.DateField(null=True),
        ),
    ]
