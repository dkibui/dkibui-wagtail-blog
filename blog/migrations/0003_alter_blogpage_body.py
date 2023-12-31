# Generated by Django 4.2.6 on 2023-10-10 16:27

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_blogpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("heading", wagtail.blocks.CharBlock()),
                    ("text", wagtail.blocks.RichTextBlock()),
                    (
                        "image_carousel",
                        wagtail.blocks.ListBlock(
                            wagtail.images.blocks.ImageChooserBlock()
                        ),
                    ),
                    (
                        "bullet_list",
                        wagtail.blocks.ListBlock(wagtail.blocks.CharBlock()),
                    ),
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
    ]
