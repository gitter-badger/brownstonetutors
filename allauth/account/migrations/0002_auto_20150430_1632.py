# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import allauth.account.models
import easy_thumbnails.fields
from django.conf import settings
import timezone_field.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line1', models.CharField(max_length=100)),
                ('line2', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100, choices=[('', '---------------------------------------------'), ('WF', 'Wallis and Futuna'), ('JP', 'Japan'), ('JM', 'Jamaica'), ('JO', 'Jordan'), ('WS', 'Samoa'), ('JE', 'Jersey'), ('GW', 'Guinea-Bissau'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GS', 'South Georgia and the South Sandwich Islands'), ('GR', 'Greece'), ('GQ', 'Equatorial Guinea'), ('GP', 'Guadeloupe'), ('GY', 'Guyana'), ('GG', 'Guernsey'), ('GF', 'French Guiana'), ('GE', 'Georgia'), ('GD', 'Grenada'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('GA', 'Gabon'), ('GN', 'Guinea'), ('GM', 'Gambia'), ('GL', 'Greenland'), ('GI', 'Gibraltar'), ('GH', 'Ghana'), ('PR', 'Puerto Rico'), ('PS', 'Palestine, State of'), ('PW', 'Palau'), ('PT', 'Portugal'), ('PY', 'Paraguay'), ('PA', 'Panama'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PE', 'Peru'), ('PK', 'Pakistan'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PM', 'Saint Pierre and Miquelon'), ('ZM', 'Zambia'), ('ZA', 'South Africa'), ('ZW', 'Zimbabwe'), ('ME', 'Montenegro'), ('MD', 'Moldova (the Republic of)'), ('MG', 'Madagascar'), ('MF', 'Saint Martin (French part)'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MM', 'Myanmar'), ('ML', 'Mali'), ('MO', 'Macao'), ('MN', 'Mongolia'), ('MH', 'Marshall Islands'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('MU', 'Mauritius'), ('MT', 'Malta'), ('MW', 'Malawi'), ('MV', 'Maldives'), ('MQ', 'Martinique'), ('MP', 'Northern Mariana Islands'), ('MS', 'Montserrat'), ('MR', 'Mauritania'), ('MY', 'Malaysia'), ('MX', 'Mexico'), ('MZ', 'Mozambique'), ('FR', 'France'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands  [Malvinas]'), ('FM', 'Micronesia (Federated States of)'), ('FO', 'Faroe Islands'), ('CK', 'Cook Islands'), ('CI', "C\xf4te d'Ivoire"), ('CH', 'Switzerland'), ('CO', 'Colombia'), ('CN', 'China'), ('CM', 'Cameroon'), ('CL', 'Chile'), ('CC', 'Cocos (Keeling) Islands'), ('CA', 'Canada'), ('CG', 'Congo'), ('CF', 'Central African Republic'), ('CD', 'Congo (the Democratic Republic of the)'), ('CZ', 'Czech Republic'), ('CY', 'Cyprus'), ('CX', 'Christmas Island'), ('CR', 'Costa Rica'), ('CW', 'Cura\xe7ao'), ('CV', 'Cabo Verde'), ('CU', 'Cuba'), ('SZ', 'Swaziland'), ('SY', 'Syrian Arab Republic'), ('SX', 'Sint Maarten (Dutch part)'), ('SS', 'South Sudan'), ('SR', 'Suriname'), ('SV', 'El Salvador'), ('ST', 'Sao Tome and Principe'), ('SK', 'Slovakia'), ('SJ', 'Svalbard and Jan Mayen'), ('SI', 'Slovenia'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SO', 'Somalia'), ('SN', 'Senegal'), ('SM', 'San Marino'), ('SL', 'Sierra Leone'), ('SC', 'Seychelles'), ('SB', 'Solomon Islands'), ('SA', 'Saudi Arabia'), ('SG', 'Singapore'), ('SE', 'Sweden'), ('SD', 'Sudan'), ('YE', 'Yemen'), ('YT', 'Mayotte'), ('LB', 'Lebanon'), ('LC', 'Saint Lucia'), ('LA', "Lao People's Democratic Republic"), ('LK', 'Sri Lanka'), ('LI', 'Liechtenstein'), ('LV', 'Latvia'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LR', 'Liberia'), ('LS', 'Lesotho'), ('LY', 'Libya'), ('VA', 'Holy See'), ('VC', 'Saint Vincent and the Grenadines'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('VG', 'Virgin Islands (British)'), ('IQ', 'Iraq'), ('VI', 'Virgin Islands (U.S.)'), ('IS', 'Iceland'), ('IR', 'Iran (Islamic Republic of)'), ('IT', 'Italy'), ('VN', 'Viet Nam'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IO', 'British Indian Ocean Territory'), ('IN', 'India'), ('IE', 'Ireland'), ('ID', 'Indonesia'), ('BD', 'Bangladesh'), ('BE', 'Belgium'), ('BF', 'Burkina Faso'), ('BG', 'Bulgaria'), ('BA', 'Bosnia and Herzegovina'), ('BB', 'Barbados'), ('BL', 'Saint Barth\xe9lemy'), ('BM', 'Bermuda'), ('BN', 'Brunei Darussalam'), ('BO', 'Bolivia (Plurinational State of)'), ('BH', 'Bahrain'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BR', 'Brazil'), ('BS', 'Bahamas'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('RS', 'Serbia'), ('RE', 'R\xe9union'), ('RO', 'Romania'), ('OM', 'Oman'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('HK', 'Hong Kong'), ('HN', 'Honduras'), ('HM', 'Heard Island and McDonald Islands'), ('EH', 'Western Sahara'), ('EE', 'Estonia'), ('EG', 'Egypt'), ('EC', 'Ecuador'), ('ET', 'Ethiopia'), ('ES', 'Spain'), ('ER', 'Eritrea'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('US', 'United States of America'), ('UM', 'United States Minor Outlying Islands'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('VU', 'Vanuatu'), ('NI', 'Nicaragua'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NZ', 'New Zealand'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NU', 'Niue'), ('KG', 'Kyrgyzstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KH', 'Cambodia'), ('KN', 'Saint Kitts and Nevis'), ('KM', 'Comoros'), ('KR', 'Korea (the Republic of)'), ('KP', "Korea (the Democratic People's Republic of)"), ('KW', 'Kuwait'), ('KZ', 'Kazakhstan'), ('KY', 'Cayman Islands'), ('DO', 'Dominican Republic'), ('DM', 'Dominica'), ('DJ', 'Djibouti'), ('DK', 'Denmark'), ('DE', 'Germany'), ('DZ', 'Algeria'), ('TZ', 'Tanzania, United Republic of'), ('TV', 'Tuvalu'), ('TW', 'Taiwan (Province of China)'), ('TT', 'Trinidad and Tobago'), ('TR', 'Turkey'), ('TN', 'Tunisia'), ('TO', 'Tonga'), ('TL', 'Timor-Leste'), ('TM', 'Turkmenistan'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TH', 'Thailand'), ('TF', 'French Southern Territories'), ('TG', 'Togo'), ('TD', 'Chad'), ('TC', 'Turks and Caicos Islands'), ('AE', 'United Arab Emirates'), ('AD', 'Andorra'), ('AG', 'Antigua and Barbuda'), ('AF', 'Afghanistan'), ('AI', 'Anguilla'), ('AM', 'Armenia'), ('AL', 'Albania'), ('AO', 'Angola'), ('AQ', 'Antarctica'), ('AS', 'American Samoa'), ('AR', 'Argentina'), ('AU', 'Australia'), ('AT', 'Austria'), ('AW', 'Aruba'), ('AX', '\xc5land Islands'), ('AZ', 'Azerbaijan'), ('QA', 'Qatar')])),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('phone_type', models.CharField(max_length=4, choices=[('CELL', 'Cell'), ('WORK', 'Work'), ('FAX', 'Fax'), ('HOME', 'Home')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timezone', timezone_field.fields.TimeZoneField(default='America/New_York')),
                ('last_active', models.DateTimeField(help_text='The last date that the user was active.', null=True, verbose_name='last active', blank=True)),
                ('mugshot', easy_thumbnails.fields.ThumbnailerImageField(help_text='A personal image displayed in your profile.', upload_to=allauth.account.models.upload_to_mugshot, verbose_name='mugshot', blank=True)),
                ('user', models.OneToOneField(related_name='base_profile', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='profile',
            field=models.ForeignKey(to='account.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(to='account.Profile', unique=True),
            preserve_default=True,
        ),
    ]
