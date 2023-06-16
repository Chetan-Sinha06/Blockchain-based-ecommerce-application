# Generated by Django 2.0.13 on 2020-10-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerCropCartModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyerusername', models.CharField(max_length=100)),
                ('buyeruseremail', models.CharField(max_length=100)),
                ('sellername', models.CharField(max_length=100)),
                ('cropname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100000)),
                ('price', models.FloatField()),
                ('file', models.FileField(upload_to='files/')),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'BuyerCartTable',
            },
        ),
    ]