import os
from os.path import join
from pyrouge import Rouge155

# Get path of ROUGE 1.5.5
try:
    _ROUGE_PATH = os.environ['ROUGE']
except KeyError:
    print('Warning: ROUGE is not configured.')
    _ROUGE_PATH = None

# Arguments
cmd = '-c 95 -r 1000 -n 2 -a'
args = ' -e {} '.format(join(_ROUGE_PATH, 'data')) + cmd

# Configs
r = Rouge155(rouge_args=args)
r.system_dir = 'lead_3/summa'  # Lead-3
r.model_dir = 'lead_3/ref'     # Reference
r.system_filename_pattern = '(\d+).summa'
r.model_filename_pattern = '#ID#.ref'

# Write results to file
output = r.convert_and_evaluate()
print(output)
with open('lead_3.txt', mode='w') as f:
    f.write(output)