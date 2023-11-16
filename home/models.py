from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    """Home page model."""
    templates = "home/home_page.html"
    max_count = 1

    page_title = models.CharField(max_length=255, blank=False, null=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        FieldPanel("body"),
    ]
