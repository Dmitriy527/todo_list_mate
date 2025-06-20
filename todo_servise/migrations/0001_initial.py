# Generated by Django 5.2.3 on 2025-06-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('ded_line', models.DateTimeField(blank=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(related_name='tags', to='todo_servise.tag')),
            ],
            options={
                'ordering': ['done', '-datetime'],
            },
        ),
    ]
