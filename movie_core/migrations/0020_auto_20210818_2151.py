# Generated by Django 3.1.3 on 2021-08-18 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_core', '0019_auto_20210818_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(choices=[(1.1, 1.1), (1.2000000000000002, 1.2000000000000002), (1.3000000000000003, 1.3000000000000003), (1.4000000000000004, 1.4000000000000004), (1.5000000000000004, 1.5000000000000004), (1.6000000000000005, 1.6000000000000005), (1.7000000000000006, 1.7000000000000006), (1.8000000000000007, 1.8000000000000007), (1.9000000000000008, 1.9000000000000008), (2.000000000000001, 2.000000000000001), (2.100000000000001, 2.100000000000001), (2.200000000000001, 2.200000000000001), (2.300000000000001, 2.300000000000001), (2.4000000000000012, 2.4000000000000012), (2.5000000000000013, 2.5000000000000013), (2.6000000000000014, 2.6000000000000014), (2.7000000000000015, 2.7000000000000015), (2.8000000000000016, 2.8000000000000016), (2.9000000000000017, 2.9000000000000017), (3.0000000000000018, 3.0000000000000018), (3.100000000000002, 3.100000000000002), (3.200000000000002, 3.200000000000002), (3.300000000000002, 3.300000000000002), (3.400000000000002, 3.400000000000002), (3.500000000000002, 3.500000000000002), (3.6000000000000023, 3.6000000000000023), (3.7000000000000024, 3.7000000000000024), (3.8000000000000025, 3.8000000000000025), (3.9000000000000026, 3.9000000000000026), (4.000000000000003, 4.000000000000003), (4.100000000000003, 4.100000000000003), (4.200000000000003, 4.200000000000003), (4.3000000000000025, 4.3000000000000025), (4.400000000000003, 4.400000000000003), (4.5000000000000036, 4.5000000000000036), (4.600000000000003, 4.600000000000003), (4.700000000000003, 4.700000000000003), (4.800000000000003, 4.800000000000003), (4.900000000000004, 4.900000000000004), (5.0000000000000036, 5.0000000000000036), (5.100000000000003, 5.100000000000003), (5.200000000000003, 5.200000000000003), (5.300000000000004, 5.300000000000004), (5.400000000000004, 5.400000000000004), (5.5000000000000036, 5.5000000000000036), (5.600000000000003, 5.600000000000003), (5.700000000000005, 5.700000000000005), (5.800000000000004, 5.800000000000004), (5.900000000000004, 5.900000000000004), (6.0000000000000036, 6.0000000000000036), (6.100000000000005, 6.100000000000005), (6.200000000000005, 6.200000000000005), (6.300000000000004, 6.300000000000004), (6.400000000000004, 6.400000000000004), (6.500000000000005, 6.500000000000005), (6.600000000000005, 6.600000000000005), (6.700000000000005, 6.700000000000005), (6.800000000000004, 6.800000000000004), (6.900000000000006, 6.900000000000006), (7.000000000000005, 7.000000000000005), (7.100000000000005, 7.100000000000005), (7.200000000000005, 7.200000000000005), (7.300000000000006, 7.300000000000006), (7.400000000000006, 7.400000000000006), (7.500000000000005, 7.500000000000005), (7.600000000000005, 7.600000000000005), (7.700000000000006, 7.700000000000006), (7.800000000000006, 7.800000000000006), (7.900000000000006, 7.900000000000006), (8.000000000000005, 8.000000000000005), (8.100000000000007, 8.100000000000007), (8.200000000000006, 8.200000000000006), (8.300000000000006, 8.300000000000006), (8.400000000000006, 8.400000000000006), (8.500000000000007, 8.500000000000007), (8.600000000000007, 8.600000000000007), (8.700000000000006, 8.700000000000006), (8.800000000000006, 8.800000000000006), (8.900000000000007, 8.900000000000007), (9.000000000000007, 9.000000000000007), (9.100000000000007, 9.100000000000007), (9.200000000000006, 9.200000000000006), (9.300000000000006, 9.300000000000006), (9.400000000000007, 9.400000000000007), (9.500000000000007, 9.500000000000007), (9.600000000000007, 9.600000000000007), (9.700000000000008, 9.700000000000008), (9.800000000000008, 9.800000000000008), (9.900000000000007, 9.900000000000007)], default=1950),
        ),
    ]