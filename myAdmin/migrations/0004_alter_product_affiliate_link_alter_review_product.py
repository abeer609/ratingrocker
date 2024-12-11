# Generated by Django 4.2.4 on 2024-12-09 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myAdmin', '0003_remove_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='affiliate_link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='myAdmin.product'),
        ),
    ]