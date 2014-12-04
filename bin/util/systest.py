#!/usr/bin/env python
# Run all of the system tests

from datetime import datetime
from genericpath import exists
from os.path  import join, isfile, splitext, basename
from os       import system, environ, chmod
from glob     import glob
from socket   import gethostname

from files import do_command, write_file, read_text
from store import save, recall, expire, expiration
from diff  import diff_string


#-----------------------------------------------------------------------------
# One Test

# Check to see if the cache is still good
def is_cached(testname):
    cache = tname(testname)+'.cache'
    if expiration(cache):
        print "Used Cached results for %s seconds"%(expiration(cache))
        return True
    else:
        return False


# Clear the cache for all tests
def clear_cache(testname):
    expire(tname(testname)+'.cache',1)


# Execute the test and save the results
def execute_test(testname):
    if not is_cached(testname) or diff(testname):
        start = datetime.now()
        #print 'Execute shell command', tname(testname)+'.tst'
        if not exists(tname(testname)+'.tst'):
            print 'error: Missing command',tname(testname)+'.tst'
        text = do_command('sh '+tname(testname)+'.tst')
        end   = datetime.now()
        t     = end-start
        print "%d.%1d seconds"%(t.seconds, t.microseconds/100000)

        #print 'OUTPUT: \n   ',tname(testname)+'.out', '\n   ',recall(tname(testname)+'.out'), '\n',
        save(tname(testname)+'.out', text)

        save(tname(testname)+'.cache', text)
        expire(tname(testname)+'.cache', 10+t.seconds*100)
        #print "Cache results for %d seconds"%(10+t.seconds*100)
    #else:
        #print 'Using cached results:', testname


# Run the requested test as a shell script
def run(testname):
    print 'Running %-15s %-50s'%(testname, tname(testname)+'.tst'),
    execute_test(testname)
    diff(testname)


# Run all tests
def run_test(testname):
    f = join(environ['pt'],t+'.py')
    #print "\n\nTEST:",t, f, join(environ['pt'],t+'.py')
    if exists(f):
        print "py_run(",t,")",t
        run(t)
    else:
        print "sh_run(",t,")",t
        run(t)

# Return the output from the last run
def output(testname):
    return recall(tname(testname)+'.out')
    

# Lookup the correct output for the test
def correct(testname):
    correct_text = recall(tname(testname)+'.correct')
    if correct_text:
        write_file(join(environ['pt'],gethostname(),testname), [correct_text])
    return correct_text


# Correct load from Git repo
def correct_load(testname, host):
    correct_text = read_text(join(environ['pt'],host,testname))[:-1]
    save(tname(testname)+'.correct', correct_text)



# Accept these test results        
def like(testname):
    text = recall(tname(testname)+'.out')
    save(tname(testname)+'.correct', text)


# Calculate the difference from what was expected
def diff(testname):
    t1 = output(testname)
    t2 = correct(testname)
    if not t2:
        save(tname(testname)+'.correct',t1)
        t2 = t1
    if t1!=t2:
        print '\n_____________________________________________________\n'
        print 'FAIL:  %-35s'%testname, len(t1), len(t2)
        print '_____________________________________________________'

        print diff_string(t1,t2)
        return True
    else:
        return False


        
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
    files = glob(join(environ['pt'],"*.tst"))
    files = [splitext(basename(f))[0] for f in files]
    return sorted(files)


# Run all Tests
def run_tests():
    list_python_tests()
    for t in tests():
        run (t)


# Show Tests Results
def tests_results():
    for t in tests():
        diff (t)


# Clear all of the test cached results
def reset_cache():
    for t in tests():
        clear_cache(t)


# Create one tst file to execute nose on a py file
def create_test(t):
    code = 'tpyrun '+t.replace(environ['p'],'$p')+' \n'
    test = join(environ['pt'],basename(t.replace('_test',''))+'.tst')
    f = open(test,'w')
    f.write(code)
    f.close()
    chmod (test, 0755)
    #print 'Create %-40s \n   %s'%(test,code)


# Translate from python tests into shell tests
def build_dir_tests(d):
    files = sorted(glob(join(d,"*_test.py")))
    files = [ join(d,f) for f in files ]
    files = filter(isfile, files)
    files = [ f.replace('.py','') for f in files ]
    for t in files:
        create_test(t)


# Run all system tests when requested
if __name__ == '__main__':
    build_dir_tests(join(environ['pt']))
    build_dir_tests(join(environ['pb'],'util'))
    for t in tests():
        run(t)

