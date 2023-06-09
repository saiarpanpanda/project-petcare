# Generated by Django 4.1.2 on 2023-04-13 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodReport',
            fields=[
                ('registration_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=100)),
                ('blood_type', models.CharField(max_length=10)),
                ('hemoglobin_level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Thyroid', models.CharField(max_length=100)),
                ('LFT', models.CharField(max_length=100)),
                ('Lipid_Profile', models.CharField(max_length=100)),
                ('KFT', models.CharField(max_length=100)),
                ('urine_cultune', models.CharField(max_length=100)),
                ('Anbiotic_Sensitivity_Test', models.CharField(max_length=100)),
                ('Glucose', models.CharField(max_length=100)),
                ('Skin_CULTURE', models.CharField(max_length=100)),
                ('STOOL_TEST', models.CharField(max_length=100)),
                ('PHYSICAL_EXAMINATION_OF_URINE', models.CharField(max_length=100)),
                ('Pancreatic_Enzyymes', models.CharField(max_length=100)),
                ('Inflammation', models.CharField(max_length=100)),
                ('Complete_Blood_Count', models.CharField(max_length=100)),
                ('Blood_Protozoa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DogPatient',
            fields=[
                ('registration_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gender', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('owner_phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
