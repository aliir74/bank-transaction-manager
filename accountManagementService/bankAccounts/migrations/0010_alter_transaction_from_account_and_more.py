# Generated by Django 4.0.1 on 2022-01-19 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankAccounts', '0009_alter_transaction_from_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='from_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_transactions', to='bankAccounts.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='to_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_transactions', to='bankAccounts.account'),
        ),
    ]