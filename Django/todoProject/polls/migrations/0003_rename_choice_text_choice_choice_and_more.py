# Generated by Django 4.2.3 on 2023-08-02 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_rename_choice_choice_choice_text_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="choice",
            old_name="choice_text",
            new_name="choice",
        ),
        migrations.RenameField(
            model_name="choice",
            old_name="question_text",
            new_name="question",
        ),
        migrations.RenameField(
            model_name="question",
            old_name="question_text",
            new_name="question",
        ),
    ]