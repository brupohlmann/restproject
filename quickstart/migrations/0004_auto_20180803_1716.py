# Generated by Django 2.0.7 on 2018-08-03 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20180801_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ceo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='ceo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quickstart.Ceo'),
            preserve_default=False,
        ),
    ]
