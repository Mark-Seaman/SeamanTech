# Test the storage of Key-Value pairs

from time import sleep

from store import save, recall, expire, expiration


# Save and restore values
def redis_test():
    #assert(recall('test_redis/name')=='Eric')
    assert(save  ('test_redis/name','Mark')==None)
    assert(recall('test_redis/name')=='Mark')
    assert(save  ('test_redis/name','Eric')==None)
    assert(recall('test_redis/name')=='Eric')


# Set and check the expiration dates
def redis_expiration_test():
    save  ('test_redis/expiration','Yeah')
    expire('test_redis/expiration',10)
    assert(expiration('test_redis/expiration')==10)
    sleep(1)    
    assert(expiration('test_redis/expiration')==9)


# Get missing values
def redis_missing_test():
    assert(recall('test_redis/missing')==None)
    assert(recall('test_redis/name')!=None)


# Run all tests
print 'Testing Store for Redis Variables'
redis_test()
redis_expiration_test()
redis_missing_test()
