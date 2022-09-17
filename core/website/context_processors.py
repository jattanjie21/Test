from cms.models import Contact, Footer



def contact_to_base(request):
    contact = Contact.objects.last()
    return {'contact': contact}


def footer_to_base(request):
    footer = Footer.objects.last()
    return {'footer': footer}