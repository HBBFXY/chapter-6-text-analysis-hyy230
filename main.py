# main.py

def analyze_text(text):
    """
    分析字符串中字符的出现频率，按降序返回字符列表
    注：仅统计字母（含中文字符），忽略数字、符号、空格
    """
    # 统计字符频率
    freq_dict = {}
    for char in text:
        # 仅保留字母（含中文）
        if char.isalpha():
            char_lower = char.lower()  # 统一小写（英文不区分大小写）
            freq_dict[char_lower] = freq_dict.get(char_lower, 0) + 1
    
    # 按频率降序排序（频率相同则按字符顺序）
    sorted_chars = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    # 返回排序后的字符列表
    return [char for char, _ in sorted_chars]


# 主程序：交互逻辑 + 输出要求文本
if __name__ == "__main__":
    # 输出要求的提示语
    print("文本字符频率分析器")
    print("请输入一段文本：")
    print("字符频率降序排列")
    print("提示：尝试输入中英文文章片段")
    
    # 获取用户输入
    user_input = input("\n请输入文本：")
    
    # 调用分析函数
    result = analyze_text(user_input)
    
    # 输出分析结果
    print("\n字符频率降序排列结果：")
    if result:
        print("、".join(result))
    else:
        print("未检测到有效字符")
