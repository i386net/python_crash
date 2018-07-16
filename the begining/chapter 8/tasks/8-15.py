#import printing_functions as pf
#from printing_functions import print_models as pm
#from printing_functions import show_completed_models as sm
from printing_functions import *

unprinted_designs = [
    'case', 'robot', 'watch'
]
completed_models = []

#pm(unprinted_designs, completed_models)
#sm(completed_models)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


