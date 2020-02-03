# Generated by Django 2.1.1 on 2020-02-01 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField()),
                ('date_lastupdated', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=20)),
                ('status_descriptian', models.TextField()),
                ('deal_source', models.CharField(max_length=50)),
                ('third_party', models.CharField(max_length=50)),
                ('project', models.CharField(max_length=50)),
                ('margin_type', models.CharField(max_length=50)),
                ('new_renew', models.CharField(max_length=10)),
                ('sub_perpcual', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='deal_app.Customer')),
            ],
        ),
    ]