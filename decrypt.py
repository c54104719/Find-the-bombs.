def caesar_decrypt_dict(ciphertext, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    shifted_alphabet = alphabet[shift:] + alphabet[:shift] #shift是偏移

    #建立字符映射表（解密映射）
    char_map = {}
    for i in range(len(shifted_alphabet)):
        char_map[shifted_alphabet[i]] = alphabet[i]


    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = char_map.get(char.upper(), char)#這一段是bing寫的
            decrypted_text += decrypted_char if char.isupper() else decrypted_char.lower()
        else:
            decrypted_text += char

    return decrypted_text

# 如果只要確認一個
'''
ciphertext = "Wkh erpe lv lq fodvvurrp"
decrypted_text = caesar_decrypt_dict(ciphertext,3)
print(decrypted_text)'''
# 如果要分析全部
'''for i in range (26):
    decrypted_text = caesar_decrypt_dict(ciphertext, i)
    print(f"Shift {i}: {decrypted_text}")'''

