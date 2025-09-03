from os import environ, path
from dotenv import load_dotenv

if path.exists('.env'):
    load_dotenv('.env')

SESSION_CONFIGS = [
    dict(
        name='cft',
        display_name='Cloudflare Turnstile',
        app_sequence=['cloudflare_turnstile'],
        num_demo_participants=1,
    ),
    dict(
        name='grc2',
        display_name='Google reCAPTCHA v2',
        app_sequence=['google_recaptcha_v2'],
        num_demo_participants=1,
    ),
    dict(
        name='grc2i',
        display_name='Google reCAPTCHA v2 invisible',
        app_sequence=['google_recaptcha_v2_invisible'],
        num_demo_participants=1,
    ),
    dict(
        name='grc3',
        display_name='Google reCAPTCHA v3 score',
        app_sequence=['google_recaptcha_v3'],
        num_demo_participants=1,
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2303746385801'


# Cloudflare Turnstile settings
CF_SITE_KEY = environ.get('CF_SITE_KEY', None)
CF_SECRET_KEY = environ.get('CF_SECRET_KEY', None)

# Google v2 reCAPTCHA settings
G2_SITE_KEY = environ.get('G2_SITE_KEY', None)
G2_SECRET_KEY = environ.get('G2_SECRET_KEY', None)

# Google v3 reCAPTCHA settings
G3_SITE_KEY = environ.get('G3_SITE_KEY', None)
G3_SECRET_KEY = environ.get('G3_SECRET_KEY', None)

# Google v2 invisible reCAPTCHA settings
G4_SITE_KEY = environ.get('G4_SITE_KEY', None)
G4_SECRET_KEY = environ.get('G4_SECRET_KEY', None)


# Check if required environment variables are set
if any(key is None for key in [CF_SITE_KEY, CF_SECRET_KEY, G2_SITE_KEY, G2_SECRET_KEY, G3_SITE_KEY, G3_SECRET_KEY, G4_SITE_KEY, G4_SECRET_KEY]):
    raise ValueError("Required environment variables are not set. ")