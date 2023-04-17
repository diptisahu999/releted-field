# Generated by Django 4.1.7 on 2023-04-03 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_salary_job_delete_employee_delete_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=4)),
                ('last_name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='DeptEmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
                ('emp_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
        ),
    ]
