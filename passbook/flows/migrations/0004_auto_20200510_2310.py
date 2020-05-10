# Generated by Django 3.0.5 on 2020-05-10 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passbook_flows', '0003_auto_20200509_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='designation',
            field=models.CharField(choices=[('authentication', 'Authentication'), ('enrollment', 'Enrollment'), ('recovery', 'Recovery'), ('password_change', 'Password Change'), ('invalidation', 'Invalidation')], max_length=100),
        ),
    ]
