from django import template

register = template.Library()

@register.filter(name='cut_words')
def cut_words(value, arg):
	"""
	This removes all the arg from the string
	"""
	return value.replace(arg, '')
# register.filter('cut_words', cut_words)