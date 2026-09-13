
s1 = '单引号'
s2 = "双引号"
s3 = """三引号
可以跨多行
常用于长提示词"""



"""
name = "小明"
age = 25

# 推荐：f-string
intro = f"我叫{name},今年{age}岁"
print(intro)  # 我叫小明，今年25岁

# 在提示词里嵌入变量（Agent最常见）
user_query = "北京天气"
prompt = f"请回答用户问题：{user_query}"
print(prompt)
"""


"""
tokens = 1500
print(f"消耗token：{tokens * 2}")       # 消耗token：3000
print(f"价格：{tokens * 0.0001:.2f}元") # 价格：0.15元（.2f表示保留2位小数）
"""


"""
text = "  Hello World  "

# 去除两端空白
print(text.strip())        # "Hello World"
print(text.lstrip())       # 去左边
print(text.rstrip())       # 去右边

# 大小写
print("hello".upper())     # "HELLO"
print("HELLO".lower())     # "hello"

# 替换
print("cat".replace("c", "b"))  # "bat"

# 查找
print("hello".find("l"))   # 2（返回索引，找不到返回-1）

# 判断开头/结尾
print("test.py".startswith("test"))  # True
print("test.py".endswith(".py"))     # True

# 分割（Agent解析输出常用）
text = "苹果,香蕉,橘子"
fruits = text.split(",")   # ['苹果', '香蕉', '橘子']
print(fruits)
# 合并
result = "-".join(fruits)  # "苹果-香蕉-橘子"
print(result)
"""


"""
text = "Hello World"
print(text[0])      # H
print(text[-1])     # d
print(text[0:5])    # Hello
print(text[:5])     # Hello（省略起点，从0开始）
print(text[6:])     # World（省略终点，到最后）

# Agent场景：截断过长的文本
long_text = "..." * 1000
safe_text = long_text[:500]  # 只取前500个字符
print(safe_text)
"""