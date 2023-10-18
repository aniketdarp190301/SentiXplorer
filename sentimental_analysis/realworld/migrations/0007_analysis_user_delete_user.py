# Generated by Django 4.2 on 2023-10-17 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realworld', '0006_remove_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='analysis', related_query_name='analysis', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]