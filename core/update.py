#!/usr/bin/env python
# https://t.me/unk9vvn
# AVI
from core.social_menu import *
from core.start import cls


dir = '/usr/share/AndTroj'

def updater():
    global checker, state
    __version__ = '2.0.0'
    last_ver = 'https://raw.githubusercontent.com/unk9vvn/AndTroj/master/others/version'

    state = 0
    try:
        checker = urlopen(last_ver).read()
        checker = checker.rsplit()[0]
    except:
        print"Connection Error!"
        state = 1

    updater = 'https://github.com/unk9vvn/AndTroj/archive/{0}.tar.gz'.format(checker)
    if state is 0:
        update = True
        if str(checker) == str(__version__):
            update = False

        if update is True:
            print "Download new version: AndTroj-{0}.tar.gz".format(checker)
            cls()
            try:
                subprocess.call(
                    'rm -r /usr/share/AndTroj && mkdir /usr/share/AndTroj',
                    shell=True)
                subprocess.call(
                    'wget ' + updater + ' -O /tmp/atj_update.tar.gz',
                    shell=True)
                subprocess.call(
                    'tar -xvf /tmp/atj_update.tar.gz && cd /tmp/AndTroj-' + checker + ' && cp -r * /usr/share/AndTroj/',
                    shell=True)
                subprocess.call(
                    'rm /tmp/atj_update.tar.gz && rm -r /tmp/AndTroj-' + checker,
                    shell=True)
                print "Updated: new version {0}".format(checker)
            except:
                print "Connection Error!\n\n"
