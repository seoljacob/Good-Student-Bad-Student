# Generated by Django 4.1 on 2023-04-06 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_mymodel_age_remove_mymodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='q2',
            field=models.IntegerField(choices=[(1, 'Not Guilty'), (2, ''), (3, ''), (4, ''), (5, 'Very Guilty')], default=3, verbose_name='Question 2'),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='q1',
            field=models.IntegerField(choices=[(1, 'Not Guilty'), (2, ''), (3, ''), (4, ''), (5, 'Very Guilty')], default=3, verbose_name='Question 1'),
        ),
    ]