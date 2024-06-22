def calculate_bytes(s):
    total_bytes = 0
    for char in s:
        if ord(char) <= 0x7F:
            # ASCII文字および半角カタカナのチェック
            total_bytes += 1
        elif 0xFF61 <= ord(char) <= 0xFF9F:
            # 半角カタカナのチェック
            total_bytes += 1
        else:
            # 全角文字（漢字、全角カタカナ、全角ひらがななど）のチェック
            total_bytes += 2
    return total_bytes
