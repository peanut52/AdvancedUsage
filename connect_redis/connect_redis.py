import time

import redis

"""方式一：普通连接"""
r = redis.Redis(host='127.0.0.1', port=6379)
# print(r.config_get('databases'))
# print(r.info('keyspace'))
# r.set('name', 'liujing')
# print(r['name'])
# print(r.get('name'))

"""方式二：连接池的方式连接"""
config = {
    'host': '127.0.0.1',
    'port': 6379,
    'decode_responses': True,
    'retry_on_timeout': 3,
    'max_connections': 1024,
}
# pool = redis.ConnectionPool(**config)
# r = redis.Redis(connection_pool=pool)
# r.set('book', '西游记')
# print(r['book'])
# print(r.get('book'))


class OperateRedis:
    def __init__(self, number):
        self.max_retry = 20
        self.current_retry = 0
        self.db = number
        while self.current_retry <= self.max_retry:
            try:
                pool = redis.ConnectionPool(**config, db=self.db)
                r = redis.Redis(connection_pool=pool)
                break
            except:
                self.current_retry += 1
                print('连接失败')
            time.sleep(2)
            continue
if __name__ == '__main__':
    OperateRedis(2)

# 常用的redis操作：
# 获取数据库总数：
# config get databases
# 如何切换数据库？
# select 2
# 上面的代码代表切换到第3（0、1、2）个数据库，如果数据库总数返回的结果是16，那么你可以最高切换到15
# 获取当前库的所有key
# keys *
# exists key 判断某个key是否存在
# move key db_index 将某个key从当前库中移动到指定的库中
# expire key 给指定的key设置过期时间
# ttl key 查看还有多少秒过期，-1代表用不过期，-2代表已过期 过期之后这个变量不会通过keys *的方式获取得到了
# type key 查看key的数据类型


# clear清屏

# 对字符串的基本操作（基操）
# set/get/del/append/strlen添加/查询/删除/拼接/长度
# incr/decr/incrby/decrby --自增/自减/按指定值增加/按指定值减少,一定要是数字才能加减
# getrange/setrange --获取指定区间范围内的值/设置指定区间范围内的值，超过字符串长度的自动用x00补齐
# setex(set key expire value)/setnx(set if not exist) --设置key对应的值value,并设置有效期(秒)/如果不存在，则set,存在则不做任何动作
# mset/mget/msetnx --m是多（Multiple）的意思，同时设置/获取一个或多个值，msetnx 设置的key都不存在时才成功，反之则失败。
# getset key value --将给定 key 的值设为 value ，并返回 key 的旧值(old value)

# 对列表数据的操作
# redis是真正以链表为数据结构操作的
# lpush key value头插法将数据插入列表
# rpush key value尾插法将数据插入列表
# lrange key start end 获取列表中指定区间内的列表数据，如果想获得所有的数据，lrange key 0 -1
# lpop/rpop key 删除列表头部/尾部一个数据
# lindex key index 获取某个列表key的index值
# llen key 获取链表长度
# lrem key count value 删除count个value值，count>0从表头删，count<0从表尾删，count=0全删
# ltrim key start end 截取，保留值在start-end内，其他的都不要了
# lset key index value 设置列表key下标为index的位置的值
# linsert key before|after pivot value 对列表key进行插入操作，在值为pivot之前或之后插入一个value值

# 集合操作，首先集合是唯一的值，不会出现两个一样的值
# sadd key value1 value2 value3 插入或新建一个集合，插入的值数量是不固定的
# smembers key 获取集合中所有元素
# sismember key value 判断一个值是否在集合中
# scard key 返回集合中元素个数
# srem key value1 value2 value3 删除key中值为value1 value2 value3的部分
# srandmember key cnt 从集合key中随机的获取cnt个值
# spop key cnt 从集合key中随机删除cnt个元素
# smove key1 key2 value 将集合key1中的元素value移动到集合key2中
# sdiff/sinter/sunion差集（第一个集合有，但第二个集合没有的）、交集（都有的元素）、并集（所有元素）


# hash操作，hash本质还是key-value，但是value对应的值是一个键值对
# hset/hget/hmset/hmget/hgetall/hdel设置获取删除
# hlen返回hash的field数量
# hexists myhash field验证field是否存在
# hkeys/hvals返回hash的key、value


# zset 有序集合，他们不像集合一样，有序集合是一对一对的
# zadd key val val'skey 向集合key中添加val对应的key以及值val，注意先加值，后加key
# zrangebyscore/zrevrangebyscore key min max [withscores] [limit offset count] --返回有序集key中，所有score值(升序/降序排列)介于min和max之间的成员, limit参数指定返回结果的数量及区间,如mysql的limit 。
# zrem key member[member...] --移除有序集key中的一个或多个成员,不存在的成员将被忽略。
# zcard/zcount/zscore --返回集合元素的个数/返回score区间内元素数量/返回有序集key中,成员member的score值。
# zrevrank/zrank --查询member的排名降序/升序
# zrevrange/zrange key start stop [withscore] --获取指定区间内的元素(按score降序/升序排列)[score可选]

