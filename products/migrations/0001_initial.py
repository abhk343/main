# Generated by Django 4.2.9 on 2024-02-20 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_remove_product_item_remove_product_supplier_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('Item_id', models.AutoField(primary_key=True, serialize=False)),
                ('Item_Name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Item',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('Supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('Supplier_Name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Supplier',
            },
        ),
        migrations.CreateModel(
            name='Stock_out',
            fields=[
                ('Stock_out_id', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity_given', models.IntegerField()),
                ('Date_given', models.DateField()),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employee')),
                ('Item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.item')),
            ],
            options={
                'db_table': 'Stock_out',
            },
        ),
        migrations.CreateModel(
            name='Stock_in',
            fields=[
                ('Stock_in_id', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity_available', models.IntegerField()),
                ('Date_added', models.DateField()),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.item')),
            ],
            options={
                'db_table': 'Stock_in',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_id', models.AutoField(primary_key=True, serialize=False)),
                ('Product_name', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Purchase_Date', models.DateField()),
                ('Invoice_Number', models.DateField()),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.item')),
                ('Supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.supplier')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
