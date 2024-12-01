

def transposition_encrypt(text, key):
    num_cols = len(key)
    num_rows = len(text) // num_cols + (1 if len(text) % num_cols else 0)
    padded_text = text.ljust(num_rows * num_cols)
    encrypted_text = [''] * num_cols

    for col in range(num_cols):
        for row in range(num_rows):
            encrypted_text[col] += padded_text[row * num_cols + col]

    return ''.join(encrypted_text)

def transposition_decrypt(cipher_text, key):
    num_cols = len(key)
    num_rows = len(cipher_text) // num_cols
    decrypted_text = [''] * num_rows

    col = 1
    row = 0
    for symbol in cipher_text:
        decrypted_text[row] += symbol
        row += 1

        if (row == num_rows) or (row == num_rows and len(cipher_text[row]) >= num_cols - len(decrypted_text[row])):
            row = 0
            col += 1

    return ''.join(decrypted_text)

def double_transposition_encrypt(text, key1, key2):
    # Перший рівень шифрування
    first_encryption = transposition_encrypt(text, key1)
    # Другий рівень шифрування
    second_encryption = transposition_encrypt(first_encryption, key2)
    return second_encryption

def double_transposition_decrypt(cipher_text, key1, key2):
    # Перший рівень дешифрування (за другим ключем)
    first_decryption = transposition_decrypt(cipher_text, key2)
    # Другий рівень дешифрування (за першим ключем)
    second_decryption = transposition_decrypt(first_decryption, key1)
    return second_decryption

# Використання
text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
key = "SECRET"
encrypted_text = transposition_encrypt(text, key)
print("Зашифрований текст:", encrypted_text)

decrypted_text = transposition_decrypt(encrypted_text, key)
print("Розшифрований текст:", decrypted_text)

key2 = "CRYPTO"
# Шифрування
encrypted_text = double_transposition_encrypt(text, key, key2)
print("Зашифрований текст:", encrypted_text)

# Дешифрування
decrypted_text = double_transposition_decrypt(encrypted_text, key, key2)
print("Розшифрований текст:", decrypted_text)