# Generated by Django 2.2.5 on 2019-10-06 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20190928_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
        ),
    ]
