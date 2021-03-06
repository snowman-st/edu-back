# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-23 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info_grade',
            fields=[
                ('grade_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '年级',
                'verbose_name_plural': '年级',
            },
        ),
        migrations.CreateModel(
            name='info_package_from',
            fields=[
                ('package_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('package_from', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '资源包来源',
                'verbose_name_plural': '资源包来源',
            },
        ),
        migrations.CreateModel(
            name='info_package_link',
            fields=[
                ('linkid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('package_to', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '资源包链接',
                'verbose_name_plural': '资源包链接',
            },
        ),
        migrations.CreateModel(
            name='info_period',
            fields=[
                ('period_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('period', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '学段',
                'verbose_name_plural': '学段',
            },
        ),
        migrations.CreateModel(
            name='info_school',
            fields=[
                ('school_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=20)),
                ('school_type', models.CharField(max_length=20)),
                ('school_location', models.CharField(max_length=20)),
                ('is_key', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': '学校',
                'verbose_name_plural': '学校',
            },
        ),
        migrations.CreateModel(
            name='info_school_type',
            fields=[
                ('school_type_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('school_type', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '学校类型',
                'verbose_name_plural': '学校类型',
            },
        ),
        migrations.CreateModel(
            name='info_subject',
            fields=[
                ('subject_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '学科',
                'verbose_name_plural': '学科',
            },
        ),
        migrations.CreateModel(
            name='info_teacher',
            fields=[
                ('teacher_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=20)),
                ('teacher_user_name', models.CharField(max_length=20)),
                ('is_key', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
            },
        ),
        migrations.CreateModel(
            name='info_version',
            fields=[
                ('version_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('version', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '教科书版本',
                'verbose_name_plural': '教科书版本',
            },
        ),
        migrations.CreateModel(
            name='rec_course',
            fields=[
                ('lession_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('chapter_id', models.SmallIntegerField()),
                ('section_id', models.SmallIntegerField()),
                ('lesson_name', models.CharField(blank=True, max_length=30, null=True)),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.info_grade')),
                ('period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.info_period')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.info_subject')),
                ('version', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.info_version')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='rec_package',
            fields=[
                ('package_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('update_time', models.DateField(blank=True, null=True)),
                ('view_count', models.BigIntegerField()),
                ('comment_count', models.BigIntegerField()),
                ('score', models.PositiveIntegerField()),
                ('edu_design_id', models.CharField(max_length=20)),
                ('edu_video_id', models.CharField(max_length=20)),
                ('edu_resource', models.CharField(max_length=20)),
                ('good_level', models.SmallIntegerField()),
                ('lession_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.rec_course')),
                ('package_from_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.info_package_from')),
                ('updata_school_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.info_school')),
                ('update_teacher_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.info_teacher')),
            ],
            options={
                'verbose_name': '资源包',
                'verbose_name_plural': '资源包',
            },
        ),
        migrations.CreateModel(
            name='rec_package_comment',
            fields=[
                ('package_comment_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=20)),
                ('comment_user_id', models.CharField(max_length=20)),
                ('comment_time', models.DateTimeField()),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.rec_package')),
            ],
            options={
                'verbose_name': '资源包评论',
                'verbose_name_plural': '资源包评论',
            },
        ),
        migrations.CreateModel(
            name='rec_package_score',
            fields=[
                ('package_score_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('score', models.SmallIntegerField()),
                ('score_user_id', models.CharField(max_length=20)),
                ('score_time', models.DateTimeField()),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.rec_package')),
            ],
            options={
                'verbose_name': '资源包点评',
                'verbose_name_plural': '资源包点评',
            },
        ),
        migrations.CreateModel(
            name='rec_package_view',
            fields=[
                ('package_view_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('view_user_id', models.CharField(max_length=20)),
                ('view_time', models.DateTimeField()),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.rec_package')),
            ],
            options={
                'verbose_name': '资源包访问',
                'verbose_name_plural': '资源包访问',
            },
        ),
        migrations.AddField(
            model_name='info_school',
            name='school_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.info_school_type'),
        ),
        migrations.AddField(
            model_name='info_package_link',
            name='package_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.rec_package'),
        ),
    ]
