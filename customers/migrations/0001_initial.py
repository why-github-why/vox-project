# Generated by Django 3.2.5 on 2021-07-28 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('company_name', models.CharField(max_length=50)),
                ('customer_email', models.CharField(max_length=50)),
                ('customer_phone', models.CharField(blank=True, max_length=25)),
                ('customer_creation', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
