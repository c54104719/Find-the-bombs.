def caesar_decrypt_numeric(ciphertext, shift):
    # 建立數字對應表
    numeric_alphabet = "0123456789"
    shifted_numeric_alphabet = numeric_alphabet[shift:] + numeric_alphabet[:shift]

    # 建立字符映射表（解密）
    char_map = {}
    for i in range(len(shifted_numeric_alphabet)):
        char_map[shifted_numeric_alphabet[i]] = numeric_alphabet[i]

    decrypted_text = ""
    for char in ciphertext:
        if char.isdigit():
            # 查詢字符的解密對應
            decrypted_char = char_map.get(char, char)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

'''
ciphertext = ""
shift = 
decrypted_text = caesar_decrypt_numeric(ciphertext, shift)
print("解密後的文本:", decrypted_text)
'''