# Generated by Django 5.0.1 on 2024-03-18 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_alter_article_options_alter_article_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name='دسته\u200cبندی'),
        ),
    ]
