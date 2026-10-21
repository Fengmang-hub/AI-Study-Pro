"""
message = {
    "role": "user",
    "content": "你好"
}

# 访问
print(message["role"])       # user

# 推荐用 get（键不存在不会报错）
print(message.get("content"))       # 你好
print(message.get("score"))         # None
print(message.get("score", 0))      # 0（给默认值）
"""


"""
user = {"name": "小明", "age": 25}

# 新增
user["city"] = "北京"

# 修改
user["age"] = 26

# 删除
del user["city"]
# 或
city = user.pop("city", None)  # 安全删除

print(user)  # {'name': '小明', 'age': 26}
"""


"""
user = {"name": "小明", "age": 25, "city": "北京"}

# 遍历键
for key in user.keys():
    print(key)

# 遍历值
for value in user.values():
    print(value)

# 遍历键值对（最常用）
for key, value in user.items():
    print(f"{key}: {value}")
"""



response = {
    "id": "chatcmpl-123",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "你好！有什么可以帮你？"
            }
        }
    ],
    "usage": {
        "prompt_tokens": 10,
        "completion_tokens": 20
    }
}

# 链式取值（一定要会）
content = response["choices"][0]["message"]["content"]
print(content)  # 你好！有什么可以帮你？

# 安全写法（防报错）
content = response.get("choices", [{}])[0].get("message", {}).get("content", "")