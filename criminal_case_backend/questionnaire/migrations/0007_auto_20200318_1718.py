# Generated by Django 2.2 on 2020-03-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_auto_20200318_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionnairetype',
            options={'verbose_name_plural': 'Questionnaire Type'},
        ),
        migrations.AlterField(
            model_name='quesanswer',
            name='answer',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='answer',
            field=models.CharField(help_text='Yes/No', max_length=120),
        ),
    ]
