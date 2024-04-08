MODE_ENCRYPT = 1; # Criptografa
MODE_DECRYPT = 0; # Descriptografa
alphabet = 'abcdefghijklmnopqrstuvwxyz'; # Elementos do alfabeto

# Algoritmo de Ceasar
def caesar(data, key, mode): 
    new_data = '';
    
    for c in data: # Percorre todos os caracteres da String passada como argumento
        index = alphabet.find(c); # Retorna a posição de cada caractere para a variável 'index'
        
        if index == -1:
            new_data += c;
        else:
            if (mode == MODE_ENCRYPT):
                new_index = index + key # Criptografando
            else:
                new_index = index - key; # Descriptografando
                
            new_index = new_index % len(alphabet); # O novo índice será o resto da divisão entre o próprio novo índice e o tamanho do alfabeto (para os casos onde, após a soma com a chave, o valor do índice ultrapassa o tamanho do alfabeto)
            new_data += alphabet[new_index:new_index+1];
            
    return new_data;

def hackingCaesar(ciphered_text):
    n = len(alphabet) # Tamanho do alfabeto
    decriptedMessage = "" # String que será usada para comparação com a mensagem original
    
    for i in range(1, n + 1):
        decriptedMessage = caesar(ciphered, i, 0) # Iremos chamar a função "caesar" com todos os valores de chave possíveis (1 a 26)
        
        if(decriptedMessage == original): # E, caso a String retornada seja igual a original, retorna o valor da chave e a mensagem descriptografada
            print(f'\nA mensagem foi descriptografada com a chave no valor {i}\nMensagem descriptografada: {decriptedMessage}')
            
            return decriptedMessage;
        else:
            print(f'Tentativa com a chave {i}: {decriptedMessage}')

# Testando o algoritmo
key = 10

original = 'a ligeira raposa marrom saltou sobre o cachorro cansado' # Mensagem original
print(f'Original: {original}')
ciphered = caesar(original, key, MODE_ENCRYPT) # Mensagem criptografada
print(f'Encriptada: {ciphered}')
plain = caesar(ciphered, key, MODE_DECRYPT) # Mensagem descriptografada
print(f'Decriptada:{plain}\n')

""" original = 'alo'
print('Original:', original) # alo
ciphered = caesar(original, key, MODE_ENCRYPT)
print('Encriptada:', ciphered) # cnq
plain = caesar(ciphered, key, MODE_DECRYPT)
print('Decriptada: ', plain) # alo """

# Testando a função para hackear a chave
hackingCaesar(ciphered)