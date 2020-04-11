# Generated by Django 3.0.4 on 2020-03-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0004_auto_20200326_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='automotive',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='aws',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='azure',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='c',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='consulting',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='consumer_products',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='cplex',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='django',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='energy',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='entertainment',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='excel',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='git',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='google_cloud',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='gurobi',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='healthcare',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='hive',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='java',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='julia',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='manufacturing',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='ms_project',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='non_profit',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='nosql',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='other',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='plsql_tsql',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='powerbi',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='python',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='r',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='retail',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='sas',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='sasEM',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='spark',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='sports',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='sql',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='technology',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='vba',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='INFORM_CAP_aCAP',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='NVIDIA_deep_learning_with_NLP',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='Oracle_SQL',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='SAS_base_programmer',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='SAS_statistical_business_analyst',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='Tableau',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='business_analyst',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='consultant',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='data_analyst',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='data_scientist',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='developer',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='international',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='mid_atlantic',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='midwest',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='northeast',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='pacific_northwest',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='south',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='southeast',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='southwest',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='west',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='within_US',
            field=models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], default=0),
        ),
    ]
