# Generated by Django 3.1.4 on 2020-12-13 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.CharField(choices=[('BACH', 'Bachelor'), ('MAST', 'Master'), ('DOCT', 'Doctorate')], default='BACH', max_length=4),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
