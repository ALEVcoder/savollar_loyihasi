# Generated by Django 3.2.9 on 2022-03-12 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish', models.CharField(max_length=256)),
                ('fani', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('options_number', models.SmallIntegerField(default=0)),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.teacher')),
            ],
            options={
                'verbose_name': 'Savol',
                'verbose_name_plural': 'Savollar',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=245)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.question')),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variantlar',
            },
        ),
    ]
