"""
# 语法：变量名 = 值
model_name = "gpt-4"
max_tokens = 2000
temperature = 0.7
is_streaming = True

# 字符串 str —— 文本
prompt = "请翻译成中文"

# 整数 int —— 没有小数点的数字
retry_count = 3

# 浮点数 float —— 有小数点的数字
temperature = 0.7

# 布尔值 bool —— 只有 True 和 False
is_valid = True

print(type(prompt))       # <class 'str'>
print(type(retry_count))  # <class 'int'>
print(type(temperature))  # <class 'float'>
print(type(is_valid))     # <class 'bool'>
"""



"""
# 字符串转整数
num_str = "100"
num = int(num_str)        # 100
print(num)
print(type(num))          # <class 'int'>

## 整数转字符串
text = str(100)           # "100"
print(text)
print(type(text))         # <class 'str'>

## 字符串转浮点
price = float("9.9")      # 9.9
print(price)
print(type(price))        # <class 'float'>

# 转布尔（空字符串、0、None 都是 False）
print(bool(""))           # False
print(bool("hello"))      # True
print(bool(0))            # False
print(bool(None))         # False
"""