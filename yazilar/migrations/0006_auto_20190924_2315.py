# Generated by Django 2.2.5 on 2019-09-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yazilar', '0005_yazi_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazi',
            name='kategori',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('K', 'Kose Yazisi')], max_length=1),
        ),
    ]