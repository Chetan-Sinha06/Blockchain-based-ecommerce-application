# Generated by Django 2.0.13 on 2020-10-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0002_buyercropcartmodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockChainTransactionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_index', models.CharField(max_length=100)),
                ('c_timestamp', models.CharField(max_length=100)),
                ('c_sender', models.CharField(max_length=100)),
                ('c_recipient', models.CharField(max_length=100)),
                ('c_amount', models.CharField(max_length=100)),
                ('c_proof', models.CharField(max_length=100)),
                ('c_previous_hash', models.CharField(max_length=100)),
                ('p_index', models.CharField(max_length=100)),
                ('p_timestamp', models.CharField(max_length=100)),
                ('p_sender', models.CharField(max_length=100)),
                ('p_recipient', models.CharField(max_length=100)),
                ('p_amount', models.CharField(max_length=100)),
                ('p_proof', models.CharField(max_length=100)),
                ('p_previous_hash', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'BlockChainTransactiontable',
            },
        ),
        migrations.CreateModel(
            name='BuyerTransactionModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyername', models.CharField(max_length=100)),
                ('totalamount', models.FloatField()),
                ('recipientname', models.CharField(max_length=100)),
                ('cradnumber', models.IntegerField()),
                ('nameoncard', models.CharField(max_length=100)),
                ('cvv', models.IntegerField()),
                ('cardexpiry', models.CharField(max_length=200)),
                ('trnx_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'BuyerTransactionTable',
            },
        ),
    ]
