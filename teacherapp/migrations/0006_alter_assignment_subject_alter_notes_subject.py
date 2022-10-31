# Generated by Django 4.1 on 2022-10-31 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0005_alter_attendence_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacherapp.subject'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacherapp.subject'),
        ),
    ]
