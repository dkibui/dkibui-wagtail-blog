# Generated by Django 4.2.6 on 2023-10-22 09:47

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_blogpage_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="blog_title",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
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
                    (
                        "image_with_caption",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    (
                                        "image1",
                                        wagtail.images.blocks.ImageChooserBlock(),
                                    ),
                                    ("caption1", wagtail.blocks.CharBlock()),
                                    (
                                        "image2",
                                        wagtail.images.blocks.ImageChooserBlock(),
                                    ),
                                    ("caption2", wagtail.blocks.CharBlock()),
                                ]
                            )
                        ),
                    ),
                    (
                        "quote",
                        wagtail.blocks.StructBlock(
                            [
                                ("quote_by", wagtail.blocks.CharBlock()),
                                ("quotes", wagtail.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
    ]
