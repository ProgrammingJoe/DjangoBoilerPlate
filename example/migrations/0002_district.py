# Generated by Django 4.1.3 on 2022-12-17 00:55

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    District = apps.get_model("example", "District")

    District.objects.create(
        name="Caribou",
        code="CARI"
    )


def reverse_func(apps, schema_editor):
    District = apps.get_model("example", "District")
    District.objects.get(name="Caribou", code="CARI").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('code', models.CharField(max_length=40)),
            ],
        ),
        migrations.RunPython(forwards_func, reverse_func)
    ]