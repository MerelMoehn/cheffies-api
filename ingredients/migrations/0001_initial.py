# Generated by Django 4.1.6 on 2023-02-08 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient_needed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_required', models.IntegerField(blank=True)),
                ('measure_unit', models.CharField(choices=[('cup', 'cup(s)'), ('g', 'gram'), ('tablespoon', 'tablespoon(s)'), ('item', 'item'), ('ml', 'ml'), ('l', 'L'), ('kg', 'kg'), ('ounce', 'ounce')], default='g', max_length=25)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients_needed', to='ingredients.ingredient')),
            ],
        ),
    ]
