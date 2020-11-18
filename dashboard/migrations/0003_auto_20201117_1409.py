# Generated by Django 3.0.7 on 2020-11-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20201029_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coviddata',
            name='ec',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='fs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='gp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='kzn',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='lp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='mp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='nc',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='nw',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='unknown',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='wc',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reproductionnum',
            name='adj',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reproductionnum',
            name='high',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='reproductionnum',
            name='infect',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='reproductionnum',
            name='low',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
