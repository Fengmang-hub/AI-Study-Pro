"""
tools = ["搜索","计算器","翻译"]

# 索引访问（从0开始）
print(tools[0])    # 搜索
print(tools[2])    # 翻译
print(tools[-1])   # 翻译（最后一个）

# 越界会报错
# print(tools[5])  # IndexError
"""


"""
tools = ["搜索", "计算器"]

# 追加到末尾
tools.append("翻译")
print(tools)  # ['搜索', '计算器', '翻译']

# 插入到指定位置
tools.insert(1, "画图")
print(tools)  # ['搜索', '画图', '计算器', '翻译']

# 删除
tools.remove("画图")   # 按值删除
last = tools.pop()     # 删除并返回最后一个
print(last)  # 翻译
print(tools)           # ['搜索', '计算器']

# 修改
tools[0] = "网页搜索"
print(tools)           # ['网页搜索', '计算器']
"""



"""
tools = ["搜索", "计算器", "翻译"]

# 方式1：直接遍历元素
for t in tools:
    print(t)

# 方式2：带索引遍历
for i, t in enumerate(tools):
    print(f"{i}: {t}")
# 0: 搜索
# 1: 计算器
# 2: 翻译

# enumerate()函数：同时获取索引和元素，常用在循环中，可以指定起始编号
print("\n")
for i,t in enumerate(tools,start=1):
    print(f"{i}:{t}")
# 1: 搜索
# 2: 计算器
# 3: 翻译
"""


"""
# 普通写法
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n * n)
print(squares)  # [1, 4, 9, 16, 25]

# 推导式写法（一行搞定）
squares = [n * n for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# 带条件
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4]

# Agent场景：从消息列表提取所有用户消息
messages = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好呀"},
    {"role": "user", "content": "再见"},
]
user_msgs = [m["content"] for m in messages if m["role"].startswith("user")]
print(user_msgs)  # ['你好', '再见']
"""




nums = [3, 1, 4, 1, 5]

print(len(nums))       # 5（长度）
print(sum(nums))       # 14（求和）
print(max(nums))       # 5（最大值）
print(min(nums))       # 1（最小值）
print(sorted(nums))    # [1, 1, 3, 4, 5]（返回新列表，原列表不变）
print(nums.count(1))   # 2（统计出现次数）
print(1 in nums)       # True（成员判断）