from django import template
import cloudinary.utils

register = template.Library()

@register.filter(name='cloudinary_audio')
def cloudinary_audio(path):
    """Converts a database text path into a secure Cloudinary audio URL."""
    if not path:
        return ""
    url, _ = cloudinary.utils.cloudinary_url(str(path), resource_type="video")
    return url

@register.filter(name='cloudinary_image')
def cloudinary_image(path):
    """Converts a database text path into a secure Cloudinary image URL."""
    if not path:
        return ""
    url, _ = cloudinary.utils.cloudinary_url(str(path), resource_type="image")
    return url
