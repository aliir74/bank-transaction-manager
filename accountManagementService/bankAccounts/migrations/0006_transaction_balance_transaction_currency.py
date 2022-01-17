# Generated by Django 4.0.1 on 2022-01-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankAccounts', '0005_remove_account_user_remove_transaction_from_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR')], default='USD', max_length=5),
        ),
    ]