# Generated by Django 4.2.5 on 2024-01-22 17:50

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(blank=True, max_length=100, verbose_name='Page Title')),
                ('page_text', models.TextField(blank=True, max_length=250, verbose_name='Page Text')),
                ('page_title_image', models.ImageField(blank=True, upload_to='photos/about_page/', verbose_name='Page Title Image')),
                ('page_title_image_alt_text', models.CharField(blank=True, max_length=150, verbose_name='Page Title Image Alt Text')),
                ('section_image', models.ImageField(blank=True, upload_to='photos/about_page/', verbose_name='Section Image')),
                ('section_image_alt_text', models.CharField(blank=True, max_length=150, verbose_name='Section Image Alt Text')),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('award_title', models.CharField(blank=True, max_length=250, verbose_name='Award Title')),
                ('award_description', models.TextField(blank=True, max_length=250, verbose_name='Award Description')),
                ('section_heading', models.TextField(blank=True, max_length=500, verbose_name='Section Heading')),
                ('section_text', models.TextField(blank=True, max_length=500, verbose_name='Section Text')),
                ('our_mission', ckeditor.fields.RichTextField(blank=True, max_length=500, verbose_name='Our Mission')),
                ('our_vision', ckeditor.fields.RichTextField(blank=True, max_length=500, verbose_name='Our Vision')),
                ('our_value', ckeditor.fields.RichTextField(blank=True, max_length=500, verbose_name='Our Value')),
            ],
            options={
                'verbose_name': 'About Page',
                'verbose_name_plural': 'About Page',
            },
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(blank=True, max_length=100, verbose_name='Page Title')),
                ('page_text', models.TextField(blank=True, max_length=250, verbose_name='Page Text')),
                ('section_heading', models.TextField(blank=True, max_length=500, verbose_name='Heading')),
                ('section_text', models.TextField(blank=True, max_length=500, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Contact Page',
                'verbose_name_plural': 'Contact Page',
            },
        ),
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_section_heading', models.TextField(blank=True, max_length=500, verbose_name='Heading')),
                ('about_section_text', models.TextField(blank=True, max_length=500, verbose_name='Text')),
                ('about_section_image', models.ImageField(blank=True, upload_to='photos/index_page/', verbose_name='Image')),
                ('about_section_image_alt_text', models.CharField(blank=True, max_length=150, verbose_name='Image Alt Text')),
                ('services_section_heading', models.TextField(blank=True, max_length=500, verbose_name='Heading')),
                ('features_section_title', models.TextField(blank=True, max_length=250, verbose_name='Title')),
                ('features_section_heading', models.TextField(blank=True, max_length=500, verbose_name='Heading')),
                ('features_section_image', models.ImageField(blank=True, upload_to='photos/index_page/', verbose_name='Image')),
                ('features_section_image_alt_text', models.CharField(blank=True, max_length=150, verbose_name='Image Alt Text')),
                ('feature_bullet_1', models.TextField(blank=True, max_length=500, verbose_name='Bullet One')),
                ('feature_bullet_2', models.TextField(blank=True, max_length=500, verbose_name='Bullet Two')),
                ('feature_bullet_3', models.TextField(blank=True, max_length=500, verbose_name='Bullet Three')),
                ('best_services_section_text', models.TextField(blank=True, max_length=500, verbose_name='Section Text')),
                ('best_service_1_font_awesome_icon', models.CharField(blank=True, max_length=100, verbose_name='Service One Font Awesome Icon Tag')),
                ('best_service_1_heading', models.CharField(blank=True, max_length=100, verbose_name='Service One Heading')),
                ('best_service_1_text', models.TextField(blank=True, max_length=250, verbose_name='Service One Text')),
                ('best_service_1_page_link', models.CharField(blank=True, max_length=100, verbose_name='Service One Page Link')),
                ('best_service_2_font_awesome_icon', models.CharField(blank=True, max_length=100, verbose_name='Service Two Font Awesome Icon Tag')),
                ('best_service_2_heading', models.CharField(blank=True, max_length=100, verbose_name='Service Two Heading')),
                ('best_service_2_text', models.TextField(blank=True, max_length=250, verbose_name='Service Two Text')),
                ('best_service_2_page_link', models.CharField(blank=True, max_length=100, verbose_name='Service Two Page Link')),
                ('best_service_3_font_awesome_icon', models.CharField(blank=True, max_length=100, verbose_name='Service Three Font Awesome Icon Tag')),
                ('best_service_3_heading', models.CharField(blank=True, max_length=100, verbose_name='Service Three Heading')),
                ('best_service_3_text', models.TextField(blank=True, max_length=250, verbose_name='Service Three Text')),
                ('best_service_3_page_link', models.CharField(blank=True, max_length=100, verbose_name='Service Three Page Link')),
                ('our_company_section_title', models.TextField(blank=True, max_length=250, verbose_name='Title')),
                ('our_company_section_heading', models.TextField(blank=True, max_length=250, verbose_name='Heading')),
                ('our_company_section_text', models.TextField(blank=True, max_length=500, verbose_name='Text')),
                ('our_company_section_image', models.ImageField(blank=True, upload_to='photos/index_page/', verbose_name='Image')),
                ('our_company_section_image_alt_text', models.CharField(blank=True, max_length=150, verbose_name='Image Alt Text')),
                ('our_company_bullet_1', models.CharField(blank=True, max_length=500, verbose_name='Bullet One')),
                ('our_company_bullet_2', models.CharField(blank=True, max_length=500, verbose_name='Bullet Twp')),
                ('our_company_bullet_3', models.CharField(blank=True, max_length=500, verbose_name='Bullet Three')),
                ('our_company_bullet_4', models.CharField(blank=True, max_length=500, verbose_name='Bullet Four')),
                ('our_company_bullet_5', models.CharField(blank=True, max_length=500, verbose_name='Bullet Five')),
                ('counter_section_text', models.CharField(blank=True, max_length=250, verbose_name='Section Text')),
                ('counter_1_title', models.CharField(blank=True, max_length=100, verbose_name='Counter One Title')),
                ('counter_1_progress', models.IntegerField(blank=True, null=True, verbose_name='Counter One Progress')),
                ('counter_2_title', models.CharField(blank=True, max_length=100, verbose_name='Counter Two Title')),
                ('counter_2_progress', models.IntegerField(blank=True, null=True, verbose_name='Counter Two Progress')),
                ('counter_3_title', models.CharField(blank=True, max_length=100, verbose_name='Counter Three Title')),
                ('counter_3_progress', models.IntegerField(blank=True, null=True, verbose_name='Counter Three Progress')),
                ('counter_4_title', models.CharField(blank=True, max_length=100, verbose_name='Counter Four Title')),
                ('counter_4_progress', models.IntegerField(blank=True, null=True, verbose_name='Counter Four Progress')),
                ('our_skills_heading', models.TextField(blank=True, max_length=500, verbose_name='Heading')),
                ('our_skills_text', models.TextField(blank=True, max_length=500, verbose_name='Text')),
                ('our_skills_image', models.ImageField(blank=True, upload_to='photos/index_page/', verbose_name='Image')),
                ('our_skills_image_alt_text', models.CharField(blank=True, max_length=150, verbose_name='Image Alt Text')),
                ('our_skill_1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill One')),
                ('our_skill_1_progress', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Skill One Progress')),
                ('our_skill_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill Two')),
                ('our_skill_2_progress', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Skill Two Progress')),
                ('our_skill_3', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill Three')),
                ('our_skill_3_progress', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Skill Three Progress')),
                ('our_skill_4', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill Four')),
                ('our_skill_4_progress', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Skill Four Progress')),
                ('our_skill_5', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill Five')),
                ('our_skill_5_progress', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Skill Five Progress')),
                ('our_skill_6', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill Six')),
                ('our_skill_6_progress', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Skill Six Progress')),
                ('our_skill_7', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill Seven')),
                ('our_skill_7_progress', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Skill Seven Progress')),
                ('our_skill_8', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill Eight')),
                ('our_skill_8_progress', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Skill Eight Progress')),
                ('our_skill_9', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill Nine')),
                ('our_skill_9_progress', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Skill Nine Progress')),
                ('our_skill_10', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill Ten')),
                ('our_skill_10_progress', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Skill Ten Progress')),
            ],
            options={
                'verbose_name': 'Index Page',
                'verbose_name_plural': 'Index Page',
            },
        ),
        migrations.CreateModel(
            name='ServicesPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(blank=True, max_length=100, verbose_name='Page Title')),
                ('page_text', models.TextField(blank=True, max_length=250, verbose_name='Page Text')),
                ('section_heading', models.TextField(blank=True, max_length=500, verbose_name='Section Heading')),
                ('section_text', models.TextField(blank=True, max_length=500, verbose_name='Section Text')),
            ],
            options={
                'verbose_name': 'Services Page',
                'verbose_name_plural': 'Services Page',
            },
        ),
        migrations.CreateModel(
            name='TeamPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(blank=True, max_length=100, verbose_name='Page Title')),
                ('page_text', models.TextField(blank=True, max_length=250, verbose_name='Page Text')),
            ],
            options={
                'verbose_name': 'Team Page',
                'verbose_name_plural': 'Team Page',
            },
        ),
        migrations.CreateModel(
            name='WebsiteDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=100, verbose_name='Site Name')),
                ('site_description', ckeditor.fields.RichTextField(blank=True, max_length=500, verbose_name='Site Description')),
                ('logo_black', models.ImageField(blank=True, upload_to='photos/website/', verbose_name='Logo Black')),
                ('logo_black_alt_text', models.CharField(blank=True, max_length=100, verbose_name='Logo Black Alt Text')),
                ('logo_white', models.ImageField(blank=True, upload_to='photos/website/', verbose_name='Logo White')),
                ('logo_white_alt_text', models.CharField(blank=True, max_length=100, verbose_name='Logo White Alt Text')),
                ('favicon', models.ImageField(blank=True, upload_to='photos/website/')),
                ('phone_1', models.CharField(blank=True, max_length=50, verbose_name='Phone One')),
                ('phone_2', models.CharField(blank=True, max_length=50, verbose_name='Phone Two')),
                ('email_1', models.EmailField(blank=True, max_length=254, verbose_name='Email One')),
                ('email_2', models.EmailField(blank=True, max_length=254, verbose_name='Email Two')),
                ('address', models.CharField(blank=True, max_length=250)),
                ('google_map_location', models.TextField(blank=True, verbose_name='Google Maps API')),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('pinterest', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('whatsapp', models.URLField(blank=True)),
                ('skype', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Website Details',
            },
        ),
    ]
