[TOC]

集合可以用来保存不重复的元素。从形式上看，集合和字典类似，使用`{}`将元素括起来。
并且元素的个数没有限制。

从内容上看，在同一个集合中，只能存储不可变数据类型，包括Number，String和Tuple，否则会会抛出TypeError错误。
~~~python
a = {1,2,[3]}
print(a)
---------------------
Traceback (most recent call last):
  File "D:\Nothing\Nothing.py", line 1, in <module>
    a = {1,2,3,[12]}
TypeError: unhashable type: 'list'
~~~

set分为两种类型分别为set和frozenset，区别是set可以做添加、删除元素操作，而frozenset不可以。

# 创建set

1. 使用{}
2. 使用set

```python
setname = set(iteration)
```

> + iteration表示可迭代，这里简单理解为除Number之外的数据类型
>
> + range()属于可迭代
>
> + 判断是否可迭代
>
>   ```python
>   from typing import *
>   
>   a = range(1, 10)
>   print(isinstance(a,Iterable))
>   ```
>
>   

# 访问set元素

由于set是无序的，所以索引访问失效。在Python中，通常使用循环结构，将集合中的元素逐一读取。

# 删除set

使用del()语句即可。

# set基本操作(添、删、交、并、差)

1. 添加元素

```
setname.add(element)
```

只能添加不可变数据类型，否则保报错。

```python
a = set(range(1, 4))
a.add("0")

print(a)
-------------------
{'0', 1, 2, 3}
```

2. 删除元素

~~~python
setname.remove(element)
~~~

只能删除存在于集合中的元素，否则报错(KeyError)。

~~~python
setname.discad(element)
~~~

这个方法和.remove()的区别只在于，.discard()删除不存在于集合的元素时不会报错。

1. 交并差集运算

