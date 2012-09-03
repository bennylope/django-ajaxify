from django.shortcuts import render


def render_ajax(request, template_name, fragment_name, **kwargs):
    """Shortcut function to render one of two templates based on request type

    Takes the same arguments as Django's `render` shortcut function with an
    added `fragment_name` argument. This secondary template will be rendered if
    the request was made by an AJAX call.

    If you use a JSON template for AJAX requests be sure to specify the correct
    mimetype in your kwargs.

    """
    if request.is_ajax():
        return render(request, fragment_name)
    return render(request, template_name)
