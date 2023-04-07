# Generated by Django 4.1 on 2023-04-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='option3',
        ),
        migrations.AddField(
            model_name='mymodel',
            name='age',
            field=models.IntegerField(default=32),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='name',
            field=models.CharField(default=3, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='q1',
            field=models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='q2',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('maybe', 'Maybe')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='q3',
            field=models.CharField(choices=[('cat', 'Cat'), ('dog', 'Dog'), ('bird', 'Bird')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='q4',
            field=models.CharField(choices=[('coffee', 'Coffee'), ('tea', 'Tea'), ('juice', 'Juice')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='q5',
            field=models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]