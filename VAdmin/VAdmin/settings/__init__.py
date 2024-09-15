from VAdmin.settings.settings_base import *

environment = os.getenv('ENV', 'local')

if environment == 'prod':
  from VAdmin.settings.settings_prod import *
elif environment == 'test':
  from VAdmin.settings.settings_test import *
else:
  from VAdmin.settings.settings_local import *