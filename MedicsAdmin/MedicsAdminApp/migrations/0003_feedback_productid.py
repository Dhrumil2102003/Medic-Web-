# Generated by Django 4.1.1 on 2023-03-27 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedicsAdminApp', '0002_alter_payment_paymentdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='ProductId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MedicsAdminApp.product'),
            preserve_default=False,
        ),
    ]
