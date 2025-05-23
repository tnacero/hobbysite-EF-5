# Generated by Django 5.1.6 on 2025-05-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0003_product_owner_product_status_product_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('On sale', 'On sale'), ('Out of Stock', 'Out of stock')], default='Available', max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
