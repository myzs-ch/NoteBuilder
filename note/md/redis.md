# PRO
[toc]

---
## 1 介绍
**开源、c语言编写**
特点   [ans](#ans_介绍2)<a name='介绍2'></a>
redis是几线程几进程   [ans](#ans_介绍3)<a name='介绍3'></a>
数据库类型   [ans](#ans_介绍4)<a name='介绍4'></a>
数据类型   [ans](#ans_介绍5)<a name='介绍5'></a>
其他数据库   [ans](#ans_介绍6)<a name='介绍6'></a>
redis诞生为了解决什么问题   [ans](#ans_介绍7)<a name='介绍7'></a>
应用场景   [ans](#ans_介绍8)<a name='介绍8'></a>
是否区分大小写   [ans](#ans_介绍9)<a name='介绍9'></a>
Redis相关文件存放路径   [ans](#ans_介绍10)<a name='介绍10'></a>



---
### 1.1 redis附加功能

持久化   [ans](#ans_redis附加功能1)<a name='redis附加功能1'></a>
过期键功能   [ans](#ans_redis附加功能2)<a name='redis附加功能2'></a>
事务功能   [ans](#ans_redis附加功能3)<a name='redis附加功能3'></a>
主从复制   [ans](#ans_redis附加功能4)<a name='redis附加功能4'></a>
sentinel哨兵功能   [ans](#ans_redis附加功能5)<a name='redis附加功能5'></a>



---
## 2 配置

redis默认端口号   [ans](#ans_配置1)<a name='配置1'></a>
ubuntu中配置文件路径(mysql)   [ans](#ans_配置2)<a name='配置2'></a>
（配置文件设置）   [ans](#ans_配置3)<a name='配置3'></a>
> 设置密码   [ans](#ans_配置4)<a name='配置4'></a>
> 设置允许远程连接数据库   [ans](#ans_配置5)<a name='配置5'></a>
配置文件执行后重启redis才能生效   [ans](#ans_配置6)<a name='配置6'></a>



---
## 3 基础命令

切换库   [ans](#ans_基础命令1)<a name='基础命令1'></a>
查看键   [ans](#ans_基础命令2)<a name='基础命令2'></a>
键是否存在   [ans](#ans_基础命令3)<a name='基础命令3'></a>
删除键   [ans](#ans_基础命令4)<a name='基础命令4'></a>
键重命名   [ans](#ans_基础命令5)<a name='基础命令5'></a>
(一般公司都会禁掉下两条命令)   [ans](#ans_基础命令6)<a name='基础命令6'></a>
清除当前库中所有数据   [ans](#ans_基础命令7)<a name='基础命令7'></a>
清除所有库中所有数据   [ans](#ans_基础命令8)<a name='基础命令8'></a>
连接客户端   [ans](#ans_基础命令9)<a name='基础命令9'></a>



---
## 4 数据类型




---
### 4.1 字符串

存储特点   [ans](#ans_字符串1)<a name='字符串1'></a>
设置key-value（3）   [ans](#ans_字符串2)<a name='字符串2'></a>
获取key的值（2）   [ans](#ans_字符串3)<a name='字符串3'></a>
为键设置过期时间(2)   [ans](#ans_字符串4)<a name='字符串4'></a>
获取长度   [ans](#ans_字符串5)<a name='字符串5'></a>
获取指定范围切片内容   [ans](#ans_字符串6)<a name='字符串6'></a>
从某处开始替换内容   [ans](#ans_字符串7)<a name='字符串7'></a>
整数加减(4)   [ans](#ans_字符串8)<a name='字符串8'></a>
浮点数加减   [ans](#ans_字符串9)<a name='字符串9'></a>
查看key存活时间   [ans](#ans_字符串10)<a name='字符串10'></a>
删除过期   [ans](#ans_字符串11)<a name='字符串11'></a>
string 命名   [ans](#ans_字符串12)<a name='字符串12'></a>
string的值的大小范围   [ans](#ans_字符串13)<a name='字符串13'></a>



---
### 4.2 列表




---
#### 4.2.1 列表特点

列表的元素是什么类型   [ans](#ans_列表特点1)<a name='列表特点1'></a>
元素是否可重复   [ans](#ans_列表特点2)<a name='列表特点2'></a>
最大容量   [ans](#ans_列表特点3)<a name='列表特点3'></a>
列表与什么数据结构类似   [ans](#ans_列表特点4)<a name='列表特点4'></a>
列表头尾在哪   [ans](#ans_列表特点5)<a name='列表特点5'></a>
常用添加和弹出位置   [ans](#ans_列表特点6)<a name='列表特点6'></a>
列表索引与python一致（-1代表最后一位）   [ans](#ans_列表特点7)<a name='列表特点7'></a>



---
#### 4.2.2 列表常用命令

创建列表   [ans](#ans_列表常用命令1)<a name='列表常用命令1'></a>
从列表头部压入元素   [ans](#ans_列表常用命令2)<a name='列表常用命令2'></a>
从列表尾部压入元素   [ans](#ans_列表常用命令3)<a name='列表常用命令3'></a>
从列表src尾部弹出1个元素，并压入到列表dst的头部   [ans](#ans_列表常用命令4)<a name='列表常用命令4'></a>
在列表指定元素后/前插入元素   [ans](#ans_列表常用命令5)<a name='列表常用命令5'></a>
查看列表中元素   [ans](#ans_列表常用命令6)<a name='列表常用命令6'></a>
获取列表长度   [ans](#ans_列表常用命令7)<a name='列表常用命令7'></a>
从列表头部/尾部弹出1个元素   [ans](#ans_列表常用命令8)<a name='列表常用命令8'></a>
阻塞弹出   [ans](#ans_列表常用命令9)<a name='列表常用命令9'></a>
删除指定元素   [ans](#ans_列表常用命令10)<a name='列表常用命令10'></a>
保留指定范围内的元素   [ans](#ans_列表常用命令11)<a name='列表常用命令11'></a>
将列表key下表为index的元素设置为value   [ans](#ans_列表常用命令12)<a name='列表常用命令12'></a>



---
## python 交互redis

需要模块   [ans](#ans_交互redis1)<a name='交互redis1'></a>
创建redis对象   [ans](#ans_交互redis2)<a name='交互redis2'></a>
常用命令   [ans](#ans_交互redis3)<a name='交互redis3'></a>



---
## 5 位图操作bitmap

redis位上限   [ans](#ans_位图操作bitmap1)<a name='位图操作bitmap1'></a>



---
### 5.1 常用命令

设置某位置上的二进制位   [ans](#ans_常用命令1)<a name='常用命令1'></a>
获取某位置上的二进制位   [ans](#ans_常用命令2)<a name='常用命令2'></a>
统计键所对应的值中有多少个1   [ans](#ans_常用命令3)<a name='常用命令3'></a>



---
## 6 Hash散列数据类型

redis数据库内存储的是键值对，因此redis数据库可以看成是一个大字典，redis的Hash类型就像是大字典内部的小字典   [ans](#ans_Hash散列数据类型1)<a name='Hash散列数据类型1'></a>



---
### 6.1 常用命令

设置字段（3）   [ans](#ans_常用命令1)<a name='常用命令1'></a>
返回键的字段个数   [ans](#ans_常用命令2)<a name='常用命令2'></a>
判断字段是否存在   [ans](#ans_常用命令3)<a name='常用命令3'></a>
获取字段值   [ans](#ans_常用命令4)<a name='常用命令4'></a>
返回所有键值对   [ans](#ans_常用命令5)<a name='常用命令5'></a>
返回所有字段名   [ans](#ans_常用命令6)<a name='常用命令6'></a>
返回所有值   [ans](#ans_常用命令7)<a name='常用命令7'></a>
删除指定字段   [ans](#ans_常用命令8)<a name='常用命令8'></a>
在字段对应值上进行整数增量运算   [ans](#ans_常用命令9)<a name='常用命令9'></a>
在字段对应值上进行浮点数增量运算   [ans](#ans_常用命令10)<a name='常用命令10'></a>



---
## 7 set集合数据类型

集合的特点   [ans](#ans_set集合数据类型1)<a name='set集合数据类型1'></a>



---
### 7.1 基本命令

增加元素到集合   [ans](#ans_基本命令1)<a name='基本命令1'></a>
查看集合中所有元素   [ans](#ans_基本命令2)<a name='基本命令2'></a>
删除一个或者多个元素   [ans](#ans_基本命令3)<a name='基本命令3'></a>
元素是否存在   [ans](#ans_基本命令4)<a name='基本命令4'></a>
随机返回集合中指定个数的元素   [ans](#ans_基本命令5)<a name='基本命令5'></a>
弹出成员   [ans](#ans_基本命令6)<a name='基本命令6'></a>
返回集合中元素的个(是否为遍历返回？)   [ans](#ans_基本命令7)<a name='基本命令7'></a>
把元素从源集合移动到目标集合   [ans](#ans_基本命令8)<a name='基本命令8'></a>
差集   [ans](#ans_基本命令9)<a name='基本命令9'></a>
将差集保存到另一个集合中   [ans](#ans_基本命令10)<a name='基本命令10'></a>
交集   [ans](#ans_基本命令11)<a name='基本命令11'></a>
并集   [ans](#ans_基本命令12)<a name='基本命令12'></a>



---
## 8 有序集合sortedset

特点   [ans](#ans_有序集合sortedset1)<a name='有序集合sortedset1'></a>
有序的原理   [ans](#ans_有序集合sortedset2)<a name='有序集合sortedset2'></a>



---
### 8.1 基本命令

添加   [ans](#ans_基本命令1)<a name='基本命令1'></a>
查看指定区间的元素   [ans](#ans_基本命令2)<a name='基本命令2'></a>
查看指定元素的分值   [ans](#ans_基本命令3)<a name='基本命令3'></a>
返回指定区间的元素   [ans](#ans_基本命令4)<a name='基本命令4'></a>
删除成员   [ans](#ans_基本命令5)<a name='基本命令5'></a>
增加或者减少分值   [ans](#ans_基本命令6)<a name='基本命令6'></a>
返回元素排名   [ans](#ans_基本命令7)<a name='基本命令7'></a>
返回元素逆序排名   [ans](#ans_基本命令8)<a name='基本命令8'></a>
删除指定区间内的元素   [ans](#ans_基本命令9)<a name='基本命令9'></a>
返回集合中元素个数   [ans](#ans_基本命令10)<a name='基本命令10'></a>
返回指定范围中元素的个数   [ans](#ans_基本命令11)<a name='基本命令11'></a>
并集   [ans](#ans_基本命令12)<a name='基本命令12'></a>
交集   [ans](#ans_基本命令13)<a name='基本命令13'></a>



---
## 9 事务

mysql数据库中事务四个特征   [ans](#ans_事务1)<a name='事务1'></a>
redis事务的特点（2）   [ans](#ans_事务2)<a name='事务2'></a>
事务命令流程   [ans](#ans_事务3)<a name='事务3'></a>
redis事务执行流程   [ans](#ans_事务4)<a name='事务4'></a>
redis事务中命令错误处理   [ans](#ans_事务5)<a name='事务5'></a>



---
### 9.1 pipeline流水线

含义   [ans](#ans_pipeline流水线1)<a name='pipeline流水线1'></a>
意义   [ans](#ans_pipeline流水线2)<a name='pipeline流水线2'></a>



---
### 9.2 watch乐观锁

作用   [ans](#ans_watch乐观锁1)<a name='watch乐观锁1'></a>
watch命令   [ans](#ans_watch乐观锁2)<a name='watch乐观锁2'></a>



---
## 10 数据持久化

redis持久化定义   [ans](#ans_数据持久化1)<a name='数据持久化1'></a>
**redis使用两个模式来提供数据持久化的功能，永久性存储需要把数据以二进制形式存储到硬盘里，因此两种模式的执行都会产生对应的文件**
RDB模式（默认开启）原理   [ans](#ans_数据持久化3)<a name='数据持久化3'></a>
RDB模式默认存储位置   [ans](#ans_数据持久化4)<a name='数据持久化4'></a>
- rdb的缺点（2）   [ans](#ans_数据持久化5)<a name='数据持久化5'></a>
- 创建rdb文件为什么不能过于频繁   [ans](#ans_数据持久化6)<a name='数据持久化6'></a>
AOF（AppendOnlyFile）模式（默认情况下不开启）原理   [ans](#ans_数据持久化7)<a name='数据持久化7'></a>
开启AOF模式（redis配置文件）   [ans](#ans_数据持久化8)<a name='数据持久化8'></a>
AOF默认存储位置   [ans](#ans_数据持久化9)<a name='数据持久化9'></a>
- AOF的优点（相对与rdb的优势）   [ans](#ans_数据持久化10)<a name='数据持久化10'></a>
- AOF的缺点   [ans](#ans_数据持久化11)<a name='数据持久化11'></a>
AOF丢失数据的原因   [ans](#ans_数据持久化12)<a name='数据持久化12'></a>
配置文件设置刷新缓冲区时间(3)   [ans](#ans_数据持久化13)<a name='数据持久化13'></a>
**一个项目可以开启多个redis服务，不同业务使用不同级别的持久化**
三种缓冲区相关设置特点   [ans](#ans_数据持久化15)<a name='数据持久化15'></a>
RDB和AOF持久化对比   [ans](#ans_数据持久化16)<a name='数据持久化16'></a>
AOF和RBA文件哪个占空间更大   [ans](#ans_数据持久化17)<a name='数据持久化17'></a>
AOF重写的意义   [ans](#ans_数据持久化18)<a name='数据持久化18'></a>
AOF重写的原理：合并冗余命令，删除无意义命令，存储命令的最终修改。   [ans](#ans_数据持久化19)<a name='数据持久化19'></a>
**AOF重写期间，服务器不会被阻塞**
AOF重写方式-命令行（客户端）发送命令   [ans](#ans_数据持久化21)<a name='数据持久化21'></a>
AOF重写方式-修改配置文件让服务器自动执行   [ans](#ans_数据持久化22)<a name='数据持久化22'></a>
增量备份和全量备份   [ans](#ans_数据持久化23)<a name='数据持久化23'></a>
数据库恢复优先使用哪个文件   [ans](#ans_数据持久化24)<a name='数据持久化24'></a>
**当使用redis和mysql当做数据库时，更多使用rdb模式；单独使用redis时，更多使用AOF模式，减少数据丢失**



---
### 10.1 创建rdb文件的两种方式

终端中使用命令保存（2）   [ans](#ans_创建rdb文件的两种方式1)<a name='创建rdb文件的两种方式1'></a>
- SAVE命令的特点   [ans](#ans_创建rdb文件的两种方式2)<a name='创建rdb文件的两种方式2'></a>
- BGSAVE的执行过程   [ans](#ans_创建rdb文件的两种方式3)<a name='创建rdb文件的两种方式3'></a>
- 两条命令的比较   [ans](#ans_创建rdb文件的两种方式4)<a name='创建rdb文件的两种方式4'></a>
设置配置文件条件，满足时自动保存（使用最多）（redis配置文件）   [ans](#ans_创建rdb文件的两种方式5)<a name='创建rdb文件的两种方式5'></a>
- 在redis命令行中配置rdb自动保存   [ans](#ans_创建rdb文件的两种方式6)<a name='创建rdb文件的两种方式6'></a>



---
### 10.2 Redis主从复制

Redis主从结构   [ans](#ans_Redis主从复制1)<a name='Redis主从复制1'></a>
**master会一直将自己的数据更新同步给slaves，保持主从同步**
master，slave，只读？只写？	master可以执行读写命令，slave只能执行读命令   [ans](#ans_Redis主从复制3)<a name='Redis主从复制3'></a>
主从复制的意义   [ans](#ans_Redis主从复制4)<a name='Redis主从复制4'></a>
原理   [ans](#ans_Redis主从复制5)<a name='Redis主从复制5'></a>



---
#### 10.2.1 主从复制的实现




---
##### 10.2.1.1 Linux命令行实现

开启slave服务端   [ans](#ans_Linux命令行实现1)<a name='Linux命令行实现1'></a>
开启slave客户端   [ans](#ans_Linux命令行实现2)<a name='Linux命令行实现2'></a>
**复制了主端的所有数据，但是只能读数据**
**一个master可以有多个slaves**



---
##### 10.2.1.2 Redis命令行实现

redis数据库启动顺序   [ans](#ans_Redis命令行实现1)<a name='Redis命令行实现1'></a>
当前服务端成为从   [ans](#ans_Redis命令行实现2)<a name='Redis命令行实现2'></a>
当前服务端（从）切换为主（不是从）   [ans](#ans_Redis命令行实现3)<a name='Redis命令行实现3'></a>



---
##### 10.2.1.3 利用配置文件实现

**每个redis服务都有一个和他对应的配置文件，可以用配置文件来启动redis服务**
自建配置文件的位置和名称（规范）   [ans](#ans_利用配置文件实现2)<a name='利用配置文件实现2'></a>
配置内容   [ans](#ans_利用配置文件实现3)<a name='利用配置文件实现3'></a>
用配置文件启动redis服务   [ans](#ans_利用配置文件实现4)<a name='利用配置文件实现4'></a>



---
#### 10.2.2 master挂了的处理方法

master和slaves下线的影响   [ans](#ans_master挂了的处理方法1)<a name='master挂了的处理方法1'></a>
master下线的解决原理   [ans](#ans_master挂了的处理方法2)<a name='master挂了的处理方法2'></a>



---
#### 10.2.3 Sentinel哨兵

**Sentinel会不断检查master和slaves是否正常，每一个sentinel可以监控任意多个master和该master下的slaves**
哨兵的启动文件位置   [ans](#ans_Sentinel哨兵2)<a name='Sentinel哨兵2'></a>
**- 使用配置文件搭建哨兵**
> 配置文件名   [ans](#ans_Sentinel哨兵4)<a name='Sentinel哨兵4'></a>
> 配置内容   [ans](#ans_Sentinel哨兵5)<a name='Sentinel哨兵5'></a>
> 使用配置文件启动sentinel   [ans](#ans_Sentinel哨兵6)<a name='Sentinel哨兵6'></a>
> sentinel默认监听端口   [ans](#ans_Sentinel哨兵7)<a name='Sentinel哨兵7'></a>
> sentinel.conf详细配置内容   [ans](#ans_Sentinel哨兵8)<a name='Sentinel哨兵8'></a>
sentinel工作原理   [ans](#ans_Sentinel哨兵9)<a name='Sentinel哨兵9'></a>
解决sentinel误判master死亡问题   [ans](#ans_Sentinel哨兵10)<a name='Sentinel哨兵10'></a>
sentinel设置数量   [ans](#ans_Sentinel哨兵11)<a name='Sentinel哨兵11'></a>



---
#### 10.2.4 python获取master

模块   [ans](#ans_python获取master1)<a name='python获取master1'></a>
哨兵连接   [ans](#ans_python获取master2)<a name='python获取master2'></a>
初始化master连接（获取主从服务器对象）   [ans](#ans_python获取master3)<a name='python获取master3'></a>



---
## 11 python3的redis模块

建立redis数据库连接   [ans](#ans_python3的redis模块1)<a name='python3的redis模块1'></a>
调用redis命令   [ans](#ans_python3的redis模块2)<a name='python3的redis模块2'></a>
建立流水线对象   [ans](#ans_python3的redis模块3)<a name='python3的redis模块3'></a>
创建使用连接池   [ans](#ans_python3的redis模块4)<a name='python3的redis模块4'></a>
用with开启事务   [ans](#ans_python3的redis模块5)<a name='python3的redis模块5'></a>



---
## 12 其他




---
### 12.1 redis的删除规则

1.主动出击   [ans](#ans_redis的删除规则1)<a name='redis的删除规则1'></a>
主动出击中，每隔多少秒扫描过期字典   [ans](#ans_redis的删除规则2)<a name='redis的删除规则2'></a>
最多有多少时间用于扫描删除   [ans](#ans_redis的删除规则3)<a name='redis的删除规则3'></a>
2.惰性删除   [ans](#ans_redis的删除规则4)<a name='redis的删除规则4'></a>
3.暴力淘汰   [ans](#ans_redis的删除规则5)<a name='redis的删除规则5'></a>
暴力淘汰的三种原则   [ans](#ans_redis的删除规则6)<a name='redis的删除规则6'></a>
如何判断低使用频率   [ans](#ans_redis的删除规则7)<a name='redis的删除规则7'></a>



---
### 12.2 池化技术

池化技术（数据库连接池）   [ans](#ans_池化技术1)<a name='池化技术1'></a>
意义   [ans](#ans_池化技术2)<a name='池化技术2'></a>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
---
---
# ANS

---
## 1 介绍
****
<a name='ans_介绍2'></a>
基于内存且支持持久化，支持多种编程语言   [back](#介绍2)
<a name='ans_介绍3'></a>
单线程单进程   [back](#介绍3)
<a name='ans_介绍4'></a>
k-v,内存型   [back](#介绍4)
<a name='ans_介绍5'></a>
字符串strings，散列hashes，列表lists，集合sets，有序集合sorted sets，等   [back](#介绍5)
<a name='ans_介绍6'></a>
mysql 关系型数据库，表格，基于磁盘，慢
MongoDB 键值对文档型数据库，值为类似JSON文档，数据结构相对单一   [back](#介绍6)
<a name='ans_介绍7'></a>
解决硬盘IO带来的性能瓶颈   [back](#介绍7)
<a name='ans_介绍8'></a>
缓存，并发计数，排行榜，生产者消费者模型   [back](#介绍8)
<a name='ans_介绍9'></a>
命令不区分，键值对会区分   [back](#介绍9)
<a name='ans_介绍10'></a>
1.配置文件：/etc/redis/redis.conf
2.备份文件:/var/lib/redis/*.rdb|*.aof
3.日志文件:/var/log/redis/redis-server.log
4启动文件:/etc/init.d/redis-server
# /etc/下存放配置文件
# /etc/init.d/下存放服务启动文件   [back](#介绍10)



---
### 1.1 redis附加功能

<a name='ans_redis附加功能1'></a>
   [back](#redis附加功能1)
<a name='ans_redis附加功能2'></a>
   [back](#redis附加功能2)
<a name='ans_redis附加功能3'></a>
对事务支持非常弱   [back](#redis附加功能3)
<a name='ans_redis附加功能4'></a>
   [back](#redis附加功能4)
<a name='ans_redis附加功能5'></a>
监控redis集群服务   [back](#redis附加功能5)



---
## 2 配置

<a name='ans_配置1'></a>
6379   [back](#配置1)
<a name='ans_配置2'></a>
```
redis:/etc/redis/redis.conf 
mysql:/etc/mysql/mysql.conf.d/mysqld.cnf
```
   [back](#配置2)
<a name='ans_配置3'></a>
暂无资料   [back](#配置3)
<a name='ans_配置4'></a>
配置文件下第500行：`requirepass 密码`   [back](#配置4)
<a name='ans_配置5'></a>
69行，注释掉本地IP地址绑定，`bind 127.0.0.1 ::1`
88行，关闭保护模式（yes改为no） `protected-mode no`   [back](#配置5)
<a name='ans_配置6'></a>
`sudo /etc/init.d/redis-server restart`   [back](#配置6)



---
## 3 基础命令

<a name='ans_基础命令1'></a>
`select number`
number值在0~15之间，db0~db15   [back](#基础命令1)
<a name='ans_基础命令2'></a>
`keys 表达式` 例如 `keys *`   [back](#基础命令2)
<a name='ans_基础命令3'></a>
`exists key`   [back](#基础命令3)
<a name='ans_基础命令4'></a>
`del key`   [back](#基础命令4)
<a name='ans_基础命令5'></a>
`rename key newkey`   [back](#基础命令5)
<a name='ans_基础命令6'></a>
暂无资料   [back](#基础命令6)
<a name='ans_基础命令7'></a>
`flushdb`   [back](#基础命令7)
<a name='ans_基础命令8'></a>
`flushall`   [back](#基础命令8)
<a name='ans_基础命令9'></a>
`redis-cli -h 127.0.0.1 -p 6379 -a 密码`   [back](#基础命令9)



---
## 4 数据类型




---
### 4.1 字符串

<a name='ans_字符串1'></a>
字符串和数字都会转为字符串来存储，并且以二进制的方式存储在内存中   [back](#字符串1)
<a name='ans_字符串2'></a>
`set key value`：为key赋值，不存在则创建key
`set key value nx`：当key不存在时创建key，key已经存在则返回（nil），nx（not exists）
`mset key1 value1 [nx/(ex seconds)] key2 value2...`：同时设置多个k-v   [back](#字符串2)
<a name='ans_字符串3'></a>
`get key`
`mget key1 key2...`   [back](#字符串3)
<a name='ans_字符串4'></a>
`set key value ex seconds`：创建时设置
```
set key value
expire key second 秒
pexpire key second 毫秒
```
为已有kv设置   [back](#字符串4)
<a name='ans_字符串5'></a>
`strlen key`：返回值为（integer）num，将value视为字符串，返回字符串长度   [back](#字符串5)
<a name='ans_字符串6'></a>
`getrange key start stop` 闭区间，start<=stop,否则为空，stop可以大于strlen key，stop不能省略   [back](#字符串6)
<a name='ans_字符串7'></a>
`setrange key index value`：从索引值开始   [back](#字符串7)
<a name='ans_字符串8'></a>
`incrby key num` :将key的值增加num
`incr key` :默认将key值加1
`decrby key num`:将key值减少num
`decr key`：默认将key值减1
num可以为负数
可以创建新key   [back](#字符串8)
<a name='ans_字符串9'></a>
`incrbyfloat key num`:将浮点型的key增加num   [back](#字符串9)
<a name='ans_字符串10'></a>
`ttl key`   [back](#字符串10)
<a name='ans_字符串11'></a>
`persist key`   [back](#字符串11)
<a name='ans_字符串12'></a>
可以使用‘-’，‘：’,key值不宜过长，会消耗内存，且增加在数据中查找的计算成本高;不宜过短，可读性差   [back](#字符串12)
<a name='ans_字符串13'></a>
最多能存储512M 2^32   [back](#字符串13)



---
### 4.2 列表




---
#### 4.2.1 列表特点

<a name='ans_列表特点1'></a>
字符串   [back](#列表特点1)
<a name='ans_列表特点2'></a>
可   [back](#列表特点2)
<a name='ans_列表特点3'></a>
2^32-1   [back](#列表特点3)
<a name='ans_列表特点4'></a>
队列,但是读取方向可以自己设定，感觉某些命令的更像栈   [back](#列表特点4)
<a name='ans_列表特点5'></a>
左头右尾   [back](#列表特点5)
<a name='ans_列表特点6'></a>
lpush，brpop左进右出   [back](#列表特点6)
<a name='ans_列表特点7'></a>
暂无资料   [back](#列表特点7)



---
#### 4.2.2 列表常用命令

<a name='ans_列表常用命令1'></a>
`LPUSH key v1 v2....`：即压入元素（头尾压入都可）   [back](#列表常用命令1)
<a name='ans_列表常用命令2'></a>
`LPUSH key v1 v2....`: 返回list长度，如果参数为多个，则一个一个地压入   [back](#列表常用命令2)
<a name='ans_列表常用命令3'></a>
`RPUSH key v1 v2....`:    [back](#列表常用命令3)
<a name='ans_列表常用命令4'></a>
`PROPLPUSH src dst`: 返回被弹出的元素   [back](#列表常用命令4)
<a name='ans_列表常用命令5'></a>
`LINSERT key after|before value newvalue`:没有RINSERT命令，左before右after
返回值：
- 如果执行成功，返回列表长度
如果没有找到pivot（支点;上面命令中的value），返回-1
如果key不存在或为空列表返回0   [back](#列表常用命令5)
<a name='ans_列表常用命令6'></a>
`LRANGE key start stop`： 按照从头部（L）依次弹出的顺序输出
不存在RRANGE或者RANGE   [back](#列表常用命令6)
<a name='ans_列表常用命令7'></a>
`LLEN key`   [back](#列表常用命令7)
<a name='ans_列表常用命令8'></a>
`LPOP key`：头部
`RPOP key`：尾部   [back](#列表常用命令8)
<a name='ans_列表常用命令9'></a>
`BLPOP key timeout`
`BRPOP key timeout`
列表为空或不存在时阻塞，FIFS（service）（FIFO），如果超时时间设置为0，就是永久阻塞，直到有数据可以弹出   [back](#列表常用命令9)
<a name='ans_列表常用命令10'></a>
`LREM key count value`：（left rem[ove]）删除count个与value相等的元素，返回被移除元素的值
count>0:表示从头搜索
count<0:表示从尾搜索
count=0表示移除所有   [back](#列表常用命令10)
<a name='ans_列表常用命令11'></a>
`LTRIM key start stop` 返回ok,删除范围外的元素   [back](#列表常用命令11)
<a name='ans_列表常用命令12'></a>
`LSET key index newvalue`   [back](#列表常用命令12)



---
## python 交互redis

<a name='ans_交互redis1'></a>
redis   [back](#交互redis1)
<a name='ans_交互redis2'></a>
`r=redis.Redis(host=,port=,db=,password=)`   [back](#交互redis2)
<a name='ans_交互redis3'></a>
r对象具有与radis命令同名的函数，（mset需要用字典传参）   [back](#交互redis3)



---
## 5 位图操作bitmap

<a name='ans_位图操作bitmap1'></a>
一个字符串类型的值最多能存储512M字节的内容，512M=2^9×2^10×2^10*2^3=2^32   [back](#位图操作bitmap1)



---
### 5.1 常用命令

<a name='ans_常用命令1'></a>
`SETBIT key offset value`:将key的值的字节串，从左起第offset位，变成value(0/1)值，返回值为offset处原本的值   [back](#常用命令1)
<a name='ans_常用命令2'></a>
`GETBIT key offset`   [back](#常用命令2)
<a name='ans_常用命令3'></a>
`BITCOUNT key start end`:start和end代表的是字节索引，例如n代表第n个字节，只能按字节为单位（字节是计算机寻址的最小单位）   [back](#常用命令3)



---
## 6 Hash散列数据类型

<a name='ans_Hash散列数据类型1'></a>
暂无资料   [back](#Hash散列数据类型1)



---
### 6.1 常用命令

<a name='ans_常用命令1'></a>
设置单个字段：
`HSET key field value`
`HSETNX key field value`
设置多个字段:
`HMSET key field value field value`
不存在则创建，存在则覆盖,存在key则增加field   [back](#常用命令1)
<a name='ans_常用命令2'></a>
`HLEN key`   [back](#常用命令2)
<a name='ans_常用命令3'></a>
`HEXISTS key field`:不存在则返回0   [back](#常用命令3)
<a name='ans_常用命令4'></a>
`HGET key field`：获取单个字段
`HMGET key field1 filed2 ...`：获取多个字段   [back](#常用命令4)
<a name='ans_常用命令5'></a>
`HGETALL key`   [back](#常用命令5)
<a name='ans_常用命令6'></a>
`HKEYS key`   [back](#常用命令6)
<a name='ans_常用命令7'></a>
`HVALS key`   [back](#常用命令7)
<a name='ans_常用命令8'></a>
`HDEL key field`   [back](#常用命令8)
<a name='ans_常用命令9'></a>
`HINCRBY key field increment`   [back](#常用命令9)
<a name='ans_常用命令10'></a>
`HINCRBYFLOAT key field increment`   [back](#常用命令10)



---
## 7 set集合数据类型

<a name='ans_set集合数据类型1'></a>
无序，去重   [back](#set集合数据类型1)



---
### 7.1 基本命令

<a name='ans_基本命令1'></a>
`SADD key member1 member2 ...` 增加一个或者多个元素，自动去重，返回成功插入到集合的元素格式   [back](#基本命令1)
<a name='ans_基本命令2'></a>
`SMEMBERS key`   [back](#基本命令2)
<a name='ans_基本命令3'></a>
`SREM key member1 member2` 元素不存在时自动忽略   [back](#基本命令3)
<a name='ans_基本命令4'></a>
`SISMEMBER key member`   [back](#基本命令4)
<a name='ans_基本命令5'></a>
`SRANDMEMBER key [count]` 默认为1   [back](#基本命令5)
<a name='ans_基本命令6'></a>
`SPOP key [count]`   [back](#基本命令6)
<a name='ans_基本命令7'></a>
`SCARD key` 不会遍历整个集合，结果值被存储在键中   [back](#基本命令7)
<a name='ans_基本命令8'></a>
`SMOVE source destination member`   [back](#基本命令8)
<a name='ans_基本命令9'></a>
`SDIFF key1 key2` key1有key2无   [back](#基本命令9)
<a name='ans_基本命令10'></a>
`SDIFFSTORE destination key1 key2` 如果destination为空，则创建   [back](#基本命令10)
<a name='ans_基本命令11'></a>
`SINTER key1 key2`
`SINTERSTORE destination key1 key2`   [back](#基本命令11)
<a name='ans_基本命令12'></a>
`SUNION key1 key2`
`SUNIONSTORE destination key1 key2`   [back](#基本命令12)



---
## 8 有序集合sortedset

<a name='ans_有序集合sortedset1'></a>
有序、去重   [back](#有序集合sortedset1)
<a name='ans_有序集合sortedset2'></a>
每个元素都关联一个浮点数分值（score），并且按照分值从小到大的顺序排列集合中的元素（分值可以相同）   [back](#有序集合sortedset2)



---
### 8.1 基本命令

<a name='ans_基本命令1'></a>
`ZADD key score member` 返回成功插入的个数,score可以相同，member相同则覆盖，   [back](#基本命令1)
<a name='ans_基本命令2'></a>
`zrange key start stop [withscores]`升序
`zrevrange key start stop [withscores]`降序   [back](#基本命令2)
<a name='ans_基本命令3'></a>
`zscore key member`   [back](#基本命令3)
<a name='ans_基本命令4'></a>
`zrangebyscore key min max [withscores][limit offset count]`
min和max为分值的值，默认为闭区间，在值前加上(可以表示开区间
limit为关键字，offset为省略元素个数，count为展示个数   [back](#基本命令4)
<a name='ans_基本命令5'></a>
`zrem key member`   [back](#基本命令5)
<a name='ans_基本命令6'></a>
`zincrby key increment member`
increment 为加减值   [back](#基本命令6)
<a name='ans_基本命令7'></a>
`zrank key member`   [back](#基本命令7)
<a name='ans_基本命令8'></a>
`zrevrank key member`   [back](#基本命令8)
<a name='ans_基本命令9'></a>
`zremrangebyscore key min max`   [back](#基本命令9)
<a name='ans_基本命令10'></a>
`zcard key`   [back](#基本命令10)
<a name='ans_基本命令11'></a>
`zcount key min max`   [back](#基本命令11)
<a name='ans_基本命令12'></a>
`zunionstore destination numkeys key [weights 权重值] [AGGREGATE SUM|MIN|MAX]`
numkeys: 操作集合的数量
aggregate: 聚合   [back](#基本命令12)
<a name='ans_基本命令13'></a>
`zinterstore destination numkeys key1 key2 weights weight AGGREGATE SUM(默认）|MIN|MAX`   [back](#基本命令13)



---
## 9 事务

<a name='ans_事务1'></a>
原子性 一致性 隔离性 持久性   [back](#事务1)
<a name='ans_事务2'></a>
1.单独的隔离操作：事务中的所有命令都会被序列化、按顺序执行，在执行过程中不会被其他客户端发来的命令打断
2.不保证原子性：redis中一个事务如果存在命令执行失败，那么其他命令依然会被执行，没有回滚机制   [back](#事务2)
<a name='ans_事务3'></a>
1.MULTI # 开启事务	mysql begin
2.命令1 # 执行命令
3.命令2...
4.EXEC # 提交到数据库执行	mysql commit
5.DISCARD # 取消事务 mysql 'rollback'   [back](#事务3)
<a name='ans_事务4'></a>
MULTI命令开启事务后，输入的每一条命令都会入列（QUEUED），直到EXEC命令，同一依序执行；或者DISCARD命令，取消事务（回滚）   [back](#事务4)
<a name='ans_事务5'></a>
1.命令语法错误，命令入队失败，直接自动执行discard退出事务
2.命令语法正确，但是类型操作有误，（比如对set类型的数据使用sort类型的命令进行操作），操作有误的命令不执行，其他命令正常执行   [back](#事务5)



---
### 9.1 pipeline流水线

<a name='ans_pipeline流水线1'></a>
在客户端使用redis事务，将命令批量发送给服务端，达到一次通信处理多条命令的效果   [back](#pipeline流水线1)
<a name='ans_pipeline流水线2'></a>
减少通信io   [back](#pipeline流水线2)



---
### 9.2 watch乐观锁

<a name='ans_watch乐观锁1'></a>
事务过程中，可以对指定key进行监听，命令提交时，若被监听key对应的值未被修改时，事务才可以提交成功，否则失败。   [back](#watch乐观锁1)
<a name='ans_watch乐观锁2'></a>
`watch key`:watch设置好后开启事务，如果在事务提交后，对应的key值发生了改变，则事务提交失败，可能是别的客户端在提交之前对key进行了修改   [back](#watch乐观锁2)



---
## 10 数据持久化

<a name='ans_数据持久化1'></a>
将数据从掉电易失的内存放到永久存储的设备上   [back](#数据持久化1)
****
<a name='ans_数据持久化3'></a>
全量备份，将数据库的数据备份到特定的二进制文件里   [back](#数据持久化3)
<a name='ans_数据持久化4'></a>
/var/lib/redis/dump.rdb(需要管理员权限)   [back](#数据持久化4)
<a name='ans_数据持久化5'></a>
1.创建RDB文件需要将服务器所有的数据库数据都保存起来，这是非常消耗资源和时间的操作
可能会丢失数据（三个save条件都没满足）   [back](#数据持久化5)
<a name='ans_数据持久化6'></a>
创建RDB文件需要将服务器所有的数据库的数据都保存起来，非常消耗时间和资源，执行过于频繁会严重影响服务器的性能   [back](#数据持久化6)
<a name='ans_数据持久化7'></a>
增量备份，每当修改数据库的命令被执行时，就把该命令存入AOF文件里。服务器重新执行一遍AOF文件里包含的所有命令，就可以推演出数据库当前数据。   [back](#数据持久化7)
<a name='ans_数据持久化8'></a>
在redis配置文件中开启
1./etc/redis/redis.conf
672行：appendonly yes #把no改为yes
676行：appendfilename "appendonly.aof"
设置好之后重启服务
`sudo /etc/init.d/redis-server restart`   [back](#数据持久化8)
<a name='ans_数据持久化9'></a>
/var/lib/redis/appendonly.aof   [back](#数据持久化9)
<a name='ans_数据持久化10'></a>
用户可以根据自己的需要对AOF持久化进行调整，让Redis在遭遇意外停机时不丢失任何数据，或者只丢失一秒中的数据，丢失概率远小于rdb   [back](#数据持久化10)
<a name='ans_数据持久化11'></a>
相对RDB耗时长，对硬盘损耗大   [back](#数据持久化11)
<a name='ans_数据持久化12'></a>
常见的操作系统中，执行系统调用write函数写内容到文件时，为了提高效率，通常把内容放入一个内存缓存区（buffer）里，等到缓冲区被填满时从将缓冲区的内容真正写入到硬盘中，所以，当一条命令真正被写入到硬盘时，这条命令才不会因为停机而意外丢失。   [back](#数据持久化12)
<a name='ans_数据持久化13'></a>
1.701行：appendfsync always
	服务器每写入一条命令，就将缓冲区的命令写入到硬盘里面，服务器就算意外停机也不会丢失任何成功执行的命令数据
2.702行：appendfsync everysec(默认)
	服务器每一秒将缓冲区里的命令写入到硬盘里，这种模式下，最多值丢失1秒的数据
703行：appendfsync no
	服务器不主动将命令希尔硬盘，由操作系统绝对何时将缓冲区里的命令写入到硬盘里，   [back](#数据持久化13)
****
<a name='ans_数据持久化15'></a>
always：速度慢，但是及其稳定，但对硬盘损耗大
everysec和no都很快，但是no可能会丢失较大的数据   [back](#数据持久化15)
<a name='ans_数据持久化16'></a>
|RDB|AOF|
|:-|:-|
|全量备份，一次保存整个数据库(快照备份)|增量备份，一次保存一个修改数据库的命令|
|保存的间隔较长|保存的间隔默认为一秒钟|
|数据还原快|数据还原速度一般，冗余命令多，还原速度慢|
|执行SAVE命令时会组摄服务器，BGSAVE不会|不会阻塞服务器|   [back](#数据持久化16)
<a name='ans_数据持久化17'></a>
AOF，存命令+数据   [back](#数据持久化17)
<a name='ans_数据持久化18'></a>
AOF文件记录命令+数据，可能会占用大量存储空间，还原速度慢。因此redis提供了AOF重写功能，来为AOF文件瘦身。   [back](#数据持久化18)
<a name='ans_数据持久化19'></a>
暂无资料   [back](#数据持久化19)
****
<a name='ans_数据持久化21'></a>
BGREWRITEAOF   [back](#数据持久化21)
<a name='ans_数据持久化22'></a>
743行:auto-aof-rewrite-percentage 100
744行：auto-aof-rewrite-min-size 64mb
（默认）
当AOF文件增量大于100%时才进行重写，也就是大于原文件一倍时。第一次新增64m时重写，之后每次新增2^(n-1)*64m才重写   [back](#数据持久化22)
<a name='ans_数据持久化23'></a>
RDB是全量，AOF是增量
增量备份的是对数据进行修改的命令   [back](#数据持久化23)
<a name='ans_数据持久化24'></a>
appendonly.aof   [back](#数据持久化24)
****



---
### 10.1 创建rdb文件的两种方式

<a name='ans_创建rdb文件的两种方式1'></a>
`SAVE`
`BGSAVE`   [back](#创建rdb文件的两种方式1)
<a name='ans_创建rdb文件的两种方式2'></a>
执行SAVE命令过程中，redis服务器将被阻塞，直到SAVE执行完毕后，服务器才会重新开始处理客户端发送的命令请求
如果RDB文件已经存在，则覆盖   [back](#创建rdb文件的两种方式2)
<a name='ans_创建rdb文件的两种方式3'></a>
1.客户端发送BGSAVE给服务器
2.服务器马上返回Background saving start给客户端
3.服务器fork()子进程处理save
4.服务器继续提供服务
子进程创建RDB文件后告知Redis服务器   [back](#创建rdb文件的两种方式3)
<a name='ans_创建rdb文件的两种方式4'></a>
Save更快，但BGSAVE更常用   [back](#创建rdb文件的两种方式4)
<a name='ans_创建rdb文件的两种方式5'></a>
# redis配置文件默认
218行：save 900 1
219行：save 300 10
表示如果距离上一次创建RDB文件已经过去了300秒，并且服务器的所有数据库总共已经发生了不少于10次修改，那么自动执行BGSAVE命令
200行：save 60 10000
1.（上述三行）只要三个条件中的任意一个被满足时，服务器就会自动执行BGSAVE
2.每次创建RDB文件后，服务器为实现自动持久化而设置的时间计数器和次数计数器就会被清零，并重新开始计数，所有多个保存条件的效果不会叠加   [back](#创建rdb文件的两种方式5)
<a name='ans_创建rdb文件的两种方式6'></a>
（不推荐）redis>save 60 10000(在命令行中打开redis，直接输入设置值)   [back](#创建rdb文件的两种方式6)



---
### 10.2 Redis主从复制

<a name='ans_Redis主从复制1'></a>
一个Redis服务可以有多个该服务的复制品，这个Redis服务成为master，其他复制品成为slaves   [back](#Redis主从复制1)
****
<a name='ans_Redis主从复制3'></a>
暂无资料   [back](#Redis主从复制3)
<a name='ans_Redis主从复制4'></a>
分担了读的压力（高并发时）   [back](#Redis主从复制4)
<a name='ans_Redis主从复制5'></a>
从服务器执行客户端发送的读命令，客户端可以连接slaves执行读请求来降低master的读压力   [back](#Redis主从复制5)



---
#### 10.2.1 主从复制的实现




---
##### 10.2.1.1 Linux命令行实现

<a name='ans_Linux命令行实现1'></a>
`redis-server --port 从服务端的端口号 --slaveof 主端的ip 主端端口号`	开启后，当前命令行窗口持续更新slave信息，**服务端**   [back](#Linux命令行实现1)
<a name='ans_Linux命令行实现2'></a>
`redis-cli -p keys *`	   [back](#Linux命令行实现2)
****
****



---
##### 10.2.1.2 Redis命令行实现

<a name='ans_Redis命令行实现1'></a>
`redis-server --port 端口号`:启动服务端，redis默认启动了6379端口号的服务端
`redis-cli -p -h -a`:启动客户端   [back](#Redis命令行实现1)
<a name='ans_Redis命令行实现2'></a>
`slaveof 主IP 主PORT`   [back](#Redis命令行实现2)
<a name='ans_Redis命令行实现3'></a>
`slaveof no one`   [back](#Redis命令行实现3)



---
##### 10.2.1.3 利用配置文件实现

****
<a name='ans_利用配置文件实现2'></a>
主目录/redis_端口号.conf   [back](#利用配置文件实现2)
<a name='ans_利用配置文件实现3'></a>
`slaveof 主host 从port` 设置主从关系
`port 端口号` 设置端口号   [back](#利用配置文件实现3)
<a name='ans_利用配置文件实现4'></a>
`redis-server redis_端口号.conf`   [back](#利用配置文件实现4)



---
#### 10.2.2 master挂了的处理方法

<a name='ans_master挂了的处理方法1'></a>
一个master可以有多个slaves，slaves下线只是读请求的处理下降
master下线将无法执行写请求   [back](#master挂了的处理方法1)
<a name='ans_master挂了的处理方法2'></a>
其中一台slave使用slaveof no one成为master，其他slaves执行slaveof指向新的master，从它这里同步数据   [back](#master挂了的处理方法2)



---
#### 10.2.3 Sentinel哨兵

****
<a name='ans_Sentinel哨兵2'></a>
`/etc/init.d/redis-sentinel` start|stop|restart   [back](#Sentinel哨兵2)
****
<a name='ans_Sentinel哨兵4'></a>
`sentinel.conf`，随意.conf   [back](#Sentinel哨兵4)
<a name='ans_Sentinel哨兵5'></a>
`port 端口号` 设置哨兵端口号（默认26379）
`sentinel monitor 哨兵名字 主host 主端口`设置哨兵监控的master   [back](#Sentinel哨兵5)
<a name='ans_Sentinel哨兵6'></a>
```
方式一 redis-sentinel sentinel.conf
redis-server sentinel.conf --sentinel
```
   [back](#Sentinel哨兵6)
<a name='ans_Sentinel哨兵7'></a>
26379   [back](#Sentinel哨兵7)
<a name='ans_Sentinel哨兵8'></a>
```
# sentinel监听端口，默认是26379，可以修改
port 26379
# 告诉sentinel去监听地址为ip:port的一个master，这里的master-name可以自定义，quorum是一个数字，指明当有多少个sentinel认为一个master失效时，master才算真正失效
sentinel monitor <master-name> <ip> <redis-port> <quorum>
#如果master有密码，则需要添加该配置
sentinel auth-pass <master-name> <password>
#master多久失联才认为是不可用了，默认是30秒
sentinel down-after-milliseconds <master-name> <milliseconds> 
```
   [back](#Sentinel哨兵8)
<a name='ans_Sentinel哨兵9'></a>
先与master连接，再与slaves连接，然后不停与连接对象发送心跳包，收不到master的响应时，会呼叫master（默认30秒），仍然没有收到响应则认为master挂了，然后切换master（与手动切换步骤一致）   [back](#Sentinel哨兵9)
<a name='ans_Sentinel哨兵10'></a>
使用多个sentinel进行监控   [back](#Sentinel哨兵10)
<a name='ans_Sentinel哨兵11'></a>
必须为奇数，因为sentinel会投票   [back](#Sentinel哨兵11)



---
#### 10.2.4 python获取master

<a name='ans_python获取master1'></a>
`from redis.sentinel import Sentinel`   [back](#python获取master1)
<a name='ans_python获取master2'></a>
`sentinel=Sentinel([('localhost',26379)],socket_timeout=0.1)`   [back](#python获取master2)
<a name='ans_python获取master3'></a>
```
master=sentinel.master_for('tedu',socket_time=0.1,db=1)
slave=sentinel.slave_foe('tedu',socket_timeout=0.1,db=1)
```
   [back](#python获取master3)



---
## 11 python3的redis模块

<a name='ans_python3的redis模块1'></a>
`r=redis.Redis(host,db,port,password....)`参数中host默认127.0.0.1,port=6379,db=0,password为数据库密码   [back](#python3的redis模块1)
<a name='ans_python3的redis模块2'></a>
Redis模块中的命令函数与redis命令（小写）同名   [back](#python3的redis模块2)
<a name='ans_python3的redis模块3'></a>
Redis模块中的pipeline()函数返回流水线对象（），使用流水线对象处理redis命令，流水线对象调用execute（），集中提交命令，   [back](#python3的redis模块3)
<a name='ans_python3的redis模块4'></a>
`pool=redis.ConnectionPool(host,db,port,password)`
`r=redis.Redis(connection_pool=pool)`   [back](#python3的redis模块4)
<a name='ans_python3的redis模块5'></a>
```
with r.pipline(transaction=true) as pipe ... values=pipe.execute()
```
   [back](#python3的redis模块5)



---
## 12 其他




---
### 12.1 redis的删除规则

<a name='ans_redis的删除规则1'></a>
所有带过期时间属性的key放在一个字典中
（1）在该字典中随机选择20个key
（2）检测并删除过期key
（3）如果过期的key的比例超过1/4，重复（1）-（3）
默认超时25ms(redis每隔100ms主动扫描一次)，则暂时停止，优先为用户提供服务（避免因为扫描而卡死）   [back](#redis的删除规则1)
<a name='ans_redis的删除规则2'></a>
100ms   [back](#redis的删除规则2)
<a name='ans_redis的删除规则3'></a>
25ms   [back](#redis的删除规则3)
<a name='ans_redis的删除规则4'></a>
get根据键获取某个值时，该值过期，则删除   [back](#redis的删除规则4)
<a name='ans_redis的删除规则5'></a>
set检查内存使用超过maxmemory就开启   [back](#redis的删除规则5)
<a name='ans_redis的删除规则6'></a>
noeviction：收到set命令，拒绝写服务，只提供读服务
nvolatile-lru:尝试删除带国旗时间的key，使用最少使用原则。
allkeys-lru:针对所有键按最少使用原则删除   [back](#redis的删除规则6)
<a name='ans_redis的删除规则7'></a>
设置一个数组存储数据，新set或者使用到的数据放最上面，一段时间后，最下面的数据定为使用频率最低的   [back](#redis的删除规则7)



---
### 12.2 池化技术

<a name='ans_池化技术1'></a>
当执行代码时，创建一个容器，容器中放置多个连接。
如果操作数据库时，没有连接，则创建并操作；操作完成后，连接不会释放，会放到容器中，以备下一次客户端连接服务器使用   [back](#池化技术1)
<a name='ans_池化技术2'></a>
省去创建和连接的时间   [back](#池化技术2)
