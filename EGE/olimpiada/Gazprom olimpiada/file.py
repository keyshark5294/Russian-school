def caesar_cipher(text, shift):
    # Определяем алфавит без буквы "ё"
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabet = alphabet.replace('ё', 'е')  # Убираем "ё"
    result = ''

    for char in text:
        if char.lower() in alphabet:
            # Индекс текущей буквы в алфавите
            idx = alphabet.index(char.lower())
            # Новый индекс с учётом цикличности
            new_idx = (idx + shift) % len(alphabet)
            # Добавляем новый символ в результат
            if char.isupper():
                result += alphabet[new_idx].upper()
            else:
                result += alphabet[new_idx]
        else:
            # Если символ не в алфавите, просто добавляем его
            result += char

    return result

def decode1(text: str) -> str:
    original_message = text
    new_message = ''
    index1 = 0
    index2 = 0

    for index in range(len(original_message)):
        
        if index == 0:
            index1 = index 
            index2 = index+1

        else:
            index1 = index1+2
            index2 = index2+2

        if index2 < len(original_message):
            new_message += original_message[index2] + original_message[index1]
    
    if len(original_message) % 2 != 0:
        new_message += original_message[-1] 

    return new_message

# Последнее сообщение и ключ для дешифровки
shift = -2 # Приводим сдвиг к длине алфавита
message = 'вйзгцфпз'
message = message[::-1]
decoded_message = caesar_cipher(message, shift)

decode1_result = decode1(decoded_message)
print(decode1_result)
# айона жыоюонрг нефтебаз