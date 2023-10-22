# Generated by Django 4.2.5 on 2023-10-20 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alynas', '0008_order_status_alter_orderline_order_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=4000, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='alynas.beer', verbose_name='beer')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beer_reviews', to=settings.AUTH_USER_MODEL, verbose_name='reviewer')),
            ],
            options={
                'verbose_name': 'beer review',
                'verbose_name_plural': 'beer reviews',
                'ordering': ['-created_at'],
            },
        ),
    ]