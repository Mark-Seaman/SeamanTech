
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3'
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'data/SeamanTech_development.db',  # Database file
        'USER': '',                            # Not used with sqlite3.
        'PASSWORD': '',                        # Not used with sqlite3.
        'HOST': '',                            # Set to empty string for localhost. 
        'PORT': '',                            # Set to empty string for default. 
    }
}
