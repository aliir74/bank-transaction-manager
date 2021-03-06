# Generated by Django 4.0.1 on 2022-01-17 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankAccounts', '0004_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='to_user',
        ),
        migrations.AddField(
            model_name='account',
            name='passport_id',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='from_account_id',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_transactions', to='bankAccounts.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='to_account_id',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_transactions', to='bankAccounts.account'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
