# Generated by Django 3.2.3 on 2021-05-28 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='customer name')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('subscription_type', models.CharField(choices=[('free', 'Free'), ('plus', 'Plus'), ('pro', 'Pro')], default='free', max_length=8, verbose_name='subscription type')),
            ],
        ),
    ]