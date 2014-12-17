import urllib2

from django.conf import settings


auth_user = getattr(settings, 'FALLBACK_STATIC_URL_USER', None)
auth_pass = getattr(settings, 'FALLBACK_STATIC_URL_PASS', None)
fallback_server = settings.FALLBACK_STATIC_URL
user_agent = getattr(settings, 'FALLBACK_USER_AGENT', 'Python-urllib/2.7')


def fetch(url):
    handlers = []
    if auth_user or auth_pass:
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, fallback_server, auth_user, auth_pass)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        handlers.append(authhandler)
    opener = urllib2.build_opener(*handlers)
    opener.addheaders = [('User-Agent', user_agent),]
    return opener.open(url).read()
