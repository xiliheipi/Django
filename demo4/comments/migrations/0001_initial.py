# Generated by Django 2.2.1 on 2019-05-29 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gametest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('subject', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=500)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('heroIntro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gametest.HeroIntro')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
