# Generated by Django 2.0.7 on 2018-08-01 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20180801_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programmer',
            name='language',
        ),
        migrations.AlterField(
            model_name='programmer',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.Language'),
        ),
    ]
