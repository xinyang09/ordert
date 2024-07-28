# Generated by Django 3.2 on 2024-06-03 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.SmallIntegerField(choices=[(1, '激活'), (2, '删除')], default=1, verbose_name='状态')),
                ('username', models.CharField(db_index=True, max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('mobile', models.CharField(db_index=True, max_length=11, verbose_name='手机号')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.SmallIntegerField(choices=[(1, '激活'), (2, '删除')], default=1, verbose_name='状态')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('percent', models.IntegerField(verbose_name='折扣')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.SmallIntegerField(choices=[(1, '激活'), (2, '删除')], default=1, verbose_name='状态')),
                ('username', models.CharField(db_index=True, max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('mobile', models.CharField(db_index=True, max_length=11, verbose_name='手机号')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='账户余额')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.administrator', verbose_name='创建者')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.level', verbose_name='级别')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
