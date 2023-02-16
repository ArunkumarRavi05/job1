# Generated by Django 4.1.6 on 2023-02-07 08:52

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('skills_req', models.CharField(max_length=200)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship'), ('Remote', 'Remote')], default='Full Time', max_length=30, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Selected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_applicant', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_job', to='recruiters.job')),
            ],
        ),
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='recruiters.job')),
            ],
        ),
    ]
