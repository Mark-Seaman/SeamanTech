#!/usr/bin/env python
# Run all of the system tests

from os.path    import join
from os         import system, environ

from files import do_command, write_file, read_file
from store import save, recall
from diff  import diff_string


#-----------------------------------------------------------------------------
# One Test

# Run the requested test as a shell script
def run(testname):
    print 'Running %-15s'%testname, tname(testname)+'.tst'
    text = do_command(tname(testname)+'.tst')
    save(tname(testname)+'.out', text)
    diff(testname)


# Return the output from the last run
def output(testname):
    tname = join(environ['pt'],testname)      
    return recall(tname(testname)+'.out')
    

# Lookup the correct output for the test
def correct(testname):
    print recall(tname(testname)+'.correct')
    return
    

# Accept these test results        
def like(testname):
    text = recall(tname(testname)+'.out')
    save(tname(testname)+'.correct', text)
    return
    

# Calculate the difference from what was expected
def diff(testname):
    t1 = recall(tname(testname)+'.out')
    t2 = recall(tname(testname)+'.correct')
    if not t2:
        save(tname(testname)+'.correct',t1)
        t2 = t1
    if t1!=t2:
        print '\n_____________________________________________________\n'
        print 'FAIL:  %-35s'%testname, len(t1), len(t2)
        print '_____________________________________________________'

        print diff_string(t1,t2)
    else:
        pass #print 'PASS'
    return

        
#-----------------------------------------------------------------------------
# Test Files

# Form the path to the test
def tname(testname):
    return join(environ['pt'],testname)

# Save this test code
def save_code(testname, code):
    save(tname(testname)+'.tst', code)


# Recall the test code
def get_code(testname):
    return write_file(tname(testname)+'.tst', recall(tname(testname)+'.tst'))


# Enumerate Tests
def tests():
    return '''
content
control
data
docs
files
git
mkcode
projects
python
records
scripts
src
update
           '''.split('\n')[1:-1]

# Run all Tests
def run_tests():
    for t in tests():
        run (t)

# Show Tests Results
def tests_results():
    for t in tests():
        diff (t)
