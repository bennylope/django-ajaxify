Django Ajaxify
==============

A few little helpers.

Instead of this::

    def view(request):
        context_dict = {'items': MyModel.objects.all()}
        return render(request, "template.html", context_dict)

Use this::

    from ajaxify import render_ajax

    def view(request):
        context_dict = {'items': MyModel.objects.all()}
        return render_ajax(request, "template.html", template_fragment.html", context_dict)

Now if your view is responding to AJAX requests it will respond with only the
generated fragment.
