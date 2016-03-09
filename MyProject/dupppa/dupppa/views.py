from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('dupppa')


def my_view(request):
    return {'project': 'dupppa'}
