# Generated by Django 5.0.13 on 2025-03-16 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'permissions': [('advance', 'Advanced Pro Plan'), ('pro', 'Pro Perm'), ('basic', 'Basic Perm'), ('basic_ai', 'Basic AI Perm')]},
        ),
    ]
