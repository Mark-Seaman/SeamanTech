
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'data/SeamanTech_development.db',  # Database file
        'USER': '',                            # Not used with sqlite3.
        'PASSWORD': '',                        # Not used with sqlite3.
        'HOST': '',                            # Set to empty string for localhost. 
        'PORT': '',                            # Set to empty string for default. 
    }
}



# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Remote server settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'django',
#         'USER': 'django',
#         'PASSWORD': '2nlRtx0NCo',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }