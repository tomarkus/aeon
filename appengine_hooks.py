from django.core.management import call_command


def pre_update():
    pass

def post_update():
    call_command('on_appengine', 'syncdb')
    call_command('on_appengine', 'migrate')

