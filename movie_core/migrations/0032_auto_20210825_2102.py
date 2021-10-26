# Generated by Django 3.1.3 on 2021-08-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_core', '0031_auto_20210825_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.FloatField(choices=[(1.1, 1.1), (1.2000000000000002, 1.2), (1.3000000000000003, 1.3), (1.4000000000000004, 1.4), (1.5000000000000004, 1.5), (1.6000000000000005, 1.6), (1.7000000000000006, 1.7), (1.8000000000000007, 1.8), (1.9000000000000008, 1.9), (2.000000000000001, 2.0), (2.100000000000001, 2.1), (2.200000000000001, 2.2), (2.300000000000001, 2.3), (2.4000000000000012, 2.4), (2.5000000000000013, 2.5), (2.6000000000000014, 2.6), (2.7000000000000015, 2.7), (2.8000000000000016, 2.8), (2.9000000000000017, 2.9), (3.0000000000000018, 3.0), (3.100000000000002, 3.1), (3.200000000000002, 3.2), (3.300000000000002, 3.3), (3.400000000000002, 3.4), (3.500000000000002, 3.5), (3.6000000000000023, 3.6), (3.7000000000000024, 3.7), (3.8000000000000025, 3.8), (3.9000000000000026, 3.9), (4.000000000000003, 4.0), (4.100000000000003, 4.1), (4.200000000000003, 4.2), (4.3000000000000025, 4.3), (4.400000000000003, 4.4), (4.5000000000000036, 4.5), (4.600000000000003, 4.6), (4.700000000000003, 4.7), (4.800000000000003, 4.8), (4.900000000000004, 4.9), (5.0000000000000036, 5.0), (5.100000000000003, 5.1), (5.200000000000003, 5.2), (5.300000000000004, 5.3), (5.400000000000004, 5.4), (5.5000000000000036, 5.5), (5.600000000000003, 5.6), (5.700000000000005, 5.7), (5.800000000000004, 5.8), (5.900000000000004, 5.9), (6.0000000000000036, 6.0), (6.100000000000005, 6.1), (6.200000000000005, 6.2), (6.300000000000004, 6.3), (6.400000000000004, 6.4), (6.500000000000005, 6.5), (6.600000000000005, 6.6), (6.700000000000005, 6.7), (6.800000000000004, 6.8), (6.900000000000006, 6.9), (7.000000000000005, 7.0), (7.100000000000005, 7.1), (7.200000000000005, 7.2), (7.300000000000006, 7.3), (7.400000000000006, 7.4), (7.500000000000005, 7.5), (7.600000000000005, 7.6), (7.700000000000006, 7.7), (7.800000000000006, 7.8), (7.900000000000006, 7.9), (8.000000000000005, 8.0), (8.100000000000007, 8.1), (8.200000000000006, 8.2), (8.300000000000006, 8.3), (8.400000000000006, 8.4), (8.500000000000007, 8.5), (8.600000000000007, 8.6), (8.700000000000006, 8.7), (8.800000000000006, 8.8), (8.900000000000007, 8.9), (9.000000000000007, 9.0), (9.100000000000007, 9.1), (9.200000000000006, 9.2), (9.300000000000006, 9.3), (9.400000000000007, 9.4), (9.500000000000007, 9.5), (9.600000000000007, 9.6), (9.700000000000008, 9.7), (9.800000000000008, 9.8), (9.900000000000007, 9.9), (10.000000000000007, 10.0)]),
        ),
    ]
