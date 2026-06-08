import os
from openai import OpenAI

try:

    client = OpenAI(
        # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为: api_key="sk-xxx",
        api_key="我的key",
        # 以下为华北2（北京）地域的URL，各地域的URL不同。
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    content = """你是一个意图分类器。根据用户的输入，判断意图属于以下两类之一：
1. 场景理解（scene_understanding）：想了解整体环境、布局、发生了什么。
2. 寻找物体（target_searching）：想找某个具体的物体/人/东西在哪里。

请严格遵守以下输出格式要求，不要输出任何多余的解释或前缀：
- 如果属于场景理解，直接且仅输出：场景理解
- 如果属于寻找物体，直接且仅输出：target=物体名称
"""
    text = input()
    completion = client.chat.completions.create(
        model="qwen-plus",  # 模型列表: https://help.aliyun.com/model-studio/getting-started/models
        messages=[
            {'role': 'system', 'content': content},
            {'role': 'user', 'content': text}
        ]
    )
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"错误信息：{e}")
    print("请参考文档：https://help.aliyun.com/model-studio/developer-reference/error-code")
