
import redis

r = redis.Redis(
    host='hostname',
    port=6379, 
    password='10574')



# open a connection to Redis
 
r.set('foo', 'bar')
value = r.get('foo')
print(value)
