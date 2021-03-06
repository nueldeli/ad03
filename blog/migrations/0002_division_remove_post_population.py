# Generated by Django 4.0.5 on 2022-07-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div_name', models.CharField(choices=[('KUCHING', 'Kuching'), ('SRI AMAN', 'Sri Aman'), ('SARIKEI', 'Sarikei'), ('KAPIT', 'Kapit'), ('SIBU', 'Sibu'), ('BINTULU', 'Bintulu'), ('MIRI', 'Miri'), ('LIMBANG', 'Limbang'), ('LAWAS', 'Lawas')], default='KUCHING', max_length=100)),
                ('population', models.IntegerField()),
            ],
            options={
                'ordering': ['population'],
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='population',
        ),
    ]
