import os
import json

def makedir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def make_html_safe(s):
    return s.replace("<", "&lt;").replace(">", "&gt;")

# Make sure CNN/DM is preprocessed and decompressed
if not os.path.exists('finished_files'):
    print("Error: run 'make_datafiles.py' first.")
    exit(1)
if not os.path.exists('finished_files/test'):
    print("Error: decompress 'test.tar' first.")

# Make directory structure to save lead-3 results
makedir('lead_3')
makedir('lead_3/ref')
makedir('lead_3/summa')

# Check size of test split
test_split = os.listdir('finished_files/test')
test_size = len(test_split)
print("%d data found in test split." % test_size)

# Process json data into txt files of references and lead-3.
for i, fname in enumerate(test_split, start=1):
    ind = fname.split('.')[0]
    
    # Read test data in json
    with open('finished_files/test/%s' % fname) as f:
        data = json.loads(f.read())
    ref = '\n'.join(data['abstract'])
    lead_3 = '\n'.join(data['article'][:3])


    # Make strings html-safe since ROUGE1.5.5 converts raw textfiles into html
    ref = make_html_safe(ref)
    lead_3 = make_html_safe(lead_3)

    # Write reference and lead-3.
    with open('lead_3/ref/%s.ref' % ind, mode='w') as f:
        f.write(ref)
    with open('lead_3/summa/%s.summa' % ind, mode='w') as f:
        f.write(lead_3)

# Everyone loves progress bar :)
    print("Processing %d/%d ..." % (i, test_size), end='\r')
print("Processing %d/%d done!" % (test_size, test_size))

# Verifying data size
assert(len(os.listdir('lead_3/ref')) == test_size)
assert(len(os.listdir('lead_3/summa')) == test_size)