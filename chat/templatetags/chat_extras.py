# ./chat/templatetags/chat_extras.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Get an item from a dictionary using a key.
    Usage in template: {{ dictionary|get_item:key }}
    """
    try:
        # Ensure the key is an integer, as user IDs are integers
        return dictionary.get(int(key))
    except (ValueError, TypeError):
        # Return None or a default value if key conversion fails or item not found
        return None