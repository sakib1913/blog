# Generated by Django 2.2.5 on 2020-09-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_auto_20200912_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]
