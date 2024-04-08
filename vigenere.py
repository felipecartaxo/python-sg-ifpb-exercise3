MODE_ENCRYPT = 1
MODE_DECRYPT = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def vigenere(data, key, mode):
    # Transformando o texto e a chave para letras minúsculas para facilitar as operações
    data = data.lower()
    key = key.lower()
    
    temp_key = ''
    
    for char in key:
        if char in alphabet:
            temp_key += char # Chave sem os caracteres que não são do alfabeto (basicamente para remover os espaços)
    
    key = temp_key # Atribui a chave, sem os espaços, à variável 'key'

    key_repetitions = len(data) // len(key) # Número de vezes que a chave cabe completamente no texto
    remaining_key = len(data) % len(key) # Tamanho do pedaço da chave que sobra
    repeated_key = key * key_repetitions + key[:remaining_key] # Repetição da chave seguida pelo pedaço restante

    result = ''
    
    j = 0 # Variável para rastrear a posição na chave
    
    for i in range(len(data)):
        if data[i] in alphabet:
            char_index = alphabet.index(data[i])
            key_index = alphabet.index(repeated_key[j % len(repeated_key)])
            
            if mode == MODE_ENCRYPT:
                encrypted_index = (char_index + key_index) % len(alphabet)
                result += alphabet[encrypted_index]
            elif mode == MODE_DECRYPT:
                decrypted_index = (char_index - key_index) % len(alphabet)
                result += alphabet[decrypted_index]
                
            j += 1
        else:
            # Se não for uma letra, apenas adicionamos o caractere à mensagem cifrada
            result += data[i]

    return result

# Tests
key = 'ch4ve'
original = 'a ligeira raposa marrom saltou sobre o cachorro cansado'
print('Original:', original)
ciphered = vigenere(original, key, MODE_ENCRYPT)
print('Encriptada:', ciphered)
plain = vigenere(ciphered, key, MODE_DECRYPT)
print('Decriptada:', plain)