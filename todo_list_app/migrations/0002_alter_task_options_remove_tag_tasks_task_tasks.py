# Generated by Django 4.1.3 on 2022-11-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_list_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["task_status", "-datetime"]},
        ),
        migrations.RemoveField(
            model_name="tag",
            name="tasks",
        ),
        migrations.AddField(
            model_name="task",
            name="tasks",
            field=models.ManyToManyField(related_name="tasks", to="todo_list_app.tag"),
        ),
    ]