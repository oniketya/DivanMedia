# Generated by Django 2.2.5 on 2019-10-08 02:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yazilar', '0013_auto_20191008_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazi',
            name='icerik2',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='contents'),
        ),
    ]
