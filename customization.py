#!/usr/bin/python
# -*- coding: utf-8  -*-

#default_language='en'
currency=u'€'
share_price=10
max_shares=3001

# from c3smembership.presentation.i18n import _
from translationstring import TranslationStringFactory
_ = TranslationStringFactory('c3smembership')

normal_member={
    'name':'normal',
    'description': _(u'FULL member. Full members have to be natural '
                     u'persons who register at least three works they '
                     u'created themselves with C3S. This applies to '
                     u'composers, lyricists and remixers. They get a '
                     u'vote.')
    }

membership_types=[normal_member]

# feature flag enabling collecting societies. If you're not c3s you want to set this False
enable_colsoc_association = False

locale_country_mapping = {
    'de': 'DE',
    'en': 'GB',
}

entry_fee = True
# convention: the last is free_form, value is minimum but can be adjusted
# regularly fee, type_identifier, type_description, entry_fee
membership_fees = [
    (5,'individual', _(u'Individual (5 €/mon)'),0),
    (20, 'small_com', _(u'Freelancer or small companie ( < 10 employees, 20 €/mon)'),90),
    (50, 'big_com', _(u'Companies (>= 10 employees) and high-income freelancers (50 €/mon)'),90),
    (100, 'sustaining',_(u'Sustaining member: You want to help our cause generously'),0)
]

company_types = ['small_com', 'big_com']

# if this is a number, the user can set his own
membership_fee_custom_min=100
membership_fee_custom_description=_(u'Sustaining member - support pEp Cooperative with a minimum of 100 €/mon')

payment_methods = { 'sdd': _(u'SEPA Direct Debit'),
                   'transfer': _(u'Bank Transfer') }

translations = set(('de','en',))

# todo accountant mail

# _() translation does not work for the mail body for some reason, so here:
address_confirmation_mail={ 'de': u'''
Hallo {} {}!

bitte benutze diesen Link um deine E-Mail-Adresse zu bestätigen
und dein PDF herunterzuladen:

   {}/verify/{}/{}

Danke!

Dein pEp-coop Team
            ''',
'en': u'''
Hello {} {}!

please use this link to verify your email address
and download your personalised PDF:

   {}/verify/{}/{}

thanks!

Your pEp-coop team
            '''
            }
