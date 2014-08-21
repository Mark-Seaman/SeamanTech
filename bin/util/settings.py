from os.path import join,dirname

# Location of app directory
BASE_DIR    = dirname(dirname(__file__))
DOC_ROOT    = join(BASE_DIR,'user_doc')
LOG_DIR     = join(dirname(BASE_DIR), 'logs')
SCRIPTS_DIR = join(dirname(BASE_DIR), 'scripts')
