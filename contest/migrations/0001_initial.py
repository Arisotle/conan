# Generated by Django 2.1.4 on 2019-03-11 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0011_problem_is_display'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('duration', models.TimeField()),
                ('contest_name', models.CharField(max_length=50)),
                ('is_official', models.BooleanField(default=False)),
                ('is_finish', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '竞赛',
                'verbose_name_plural': '竞赛',
                'db_table': 'contest',
            },
        ),
        migrations.CreateModel(
            name='contest_grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('time_cost', models.TimeField(default=(1900, 1, 1, 0, 0, 0, 0, 1, -1))),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContestCommitRecord',
            fields=[
                ('commitrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problem.CommitRecord')),
                ('cid', models.IntegerField(verbose_name='比赛编号')),
            ],
            options={
                'verbose_name': '竞赛提交记录',
                'verbose_name_plural': '竞赛提交记录',
                'db_table': 'contest_commit_record',
            },
            bases=('problem.commitrecord',),
        ),
        migrations.CreateModel(
            name='ContestQuestion',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problem.Problem')),
                ('value', models.IntegerField(default=10, verbose_name='题目分值')),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
            ],
            options={
                'verbose_name': '竞赛题目',
                'verbose_name_plural': '竞赛题目',
                'db_table': 'contest_question',
            },
            bases=('problem.problem',),
        ),
    ]