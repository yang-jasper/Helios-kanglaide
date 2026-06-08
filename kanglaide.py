# 简单的语音输入与意图识别模拟

test

# 定义关键词
find_words = ["找", "寻找", "帮我找"]  # 找物体意图
cancel_words = ["取消", "停止", "算了"]  # 取消意图
detail_words = ["详细", "细节", "具体"]  # 详细描述意图
# 其他输入默认为 analyze_scene

# 可识别的物体
objects = ["水杯", "钥匙", "手机", "门"]


def recognize_intent(text):
    """识别意图"""
    # 检查取消
    for word in cancel_words:
        if word in text:
            return "cancel", None

    # 检查找物体
    for word in find_words:
        if word in text:
            # 提取目标物体
            for obj in objects:
                if obj in text:
                    return "find_object", obj
            return "find_object", None  # 没找到具体物体

    # 检查详细描述
    for word in detail_words:
        if word in text:
            return "detail", None

    # 默认场景分析
    return "analyze_scene", None


def get_reply(intent, target):

    if intent == "analyze_scene":
        return "开始分析周围环境。"
    elif intent == "find_object":
        if target:
            return f"开始帮你找{target}。"
        else:
            return "请说具体找什么（水杯、钥匙、手机、门）。"
    elif intent == "detail":
        return "正在获取详细信息。"
    elif intent == "cancel":
        return "已取消任务。"
    return "请重新说一遍。"


# 主程序
print("=== Helios 语音助手模拟 ===")
print("试试说：帮我找水杯、分析场景、详细、取消")
print()

while True:
    # 模拟语音输入（用文字代替）
    text = input("你说: ").strip()

    if text in ["退出", "exit", "quit"]:
        print("再见！")
        break

    # 识别意图
    intent, target = recognize_intent(text)

    # 生成回复
    reply = get_reply(intent, target)

    # 输出结果
    if target:
        print(f"输出: intent={intent}, target={target}, reply={reply}")
    else:
        print(f"输出: intent={intent}, reply={reply}")
    print()
