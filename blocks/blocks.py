from wagtail.blocks import (
    CharBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class ImageWithCaptionBlock(StructBlock):
    image1 = ImageChooserBlock()
    caption1 = CharBlock()
    image2 = ImageChooserBlock()
    caption2 = CharBlock()


class QuoteBlock(StructBlock):
    quote_by = CharBlock()
    quotes = RichTextBlock()

    class Meta:
        template = "blocks/quote_block.html"


class CodeBlock(StructBlock):
    code = TextBlock()

    class Meta:
        template = "blocks/code_block.html"


class BodyBlock(StreamBlock):
    text = RichTextBlock()
    image_carousel = ListBlock(ImageChooserBlock())
    bullet_list = ListBlock(CharBlock())
    image_with_caption = ListBlock(ImageWithCaptionBlock())
    code = CodeBlock()
    quote = QuoteBlock()
