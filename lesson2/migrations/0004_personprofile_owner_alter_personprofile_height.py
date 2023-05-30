# Generated by Django 4.2.1 on 2023-05-30 13:53

from django.db import migrations, models
import django.db.models.deletion
import lesson2.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lesson2', '0003_alter_person_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='personprofile',
            name='owner',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='lesson2.person', verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[lesson2.validators.validate_height], verbose_name='Рост(см.)'),
        ),
    ]