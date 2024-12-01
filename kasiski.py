import math
from collections import Counter

def find_repeated_sequences(text, seq_len=3):
    sequences = {}
    for i in range(len(text) - seq_len + 1):
        seq = text[i:i+seq_len]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]
    # Залишаємо тільки ті послідовності, які повторюються
    repeated = {seq: positions for seq, positions in sequences.items() if len(positions) > 1}
    return repeated

def get_distances(repeated_sequences):
    distances = []
    for positions in repeated_sequences.values():
        for i in range(len(positions) - 1):
            distances.append(positions[i+1] - positions[i])
    return distances

def get_possible_key_lengths(distances):
    gcd_counts = Counter()
    for i in range(len(distances)):
        for j in range(i + 1, len(distances)):
            gcd = math.gcd(distances[i], distances[j])
            if 2 <= gcd <= 20:  # Обмежуємо довжину ключа
                gcd_counts[gcd] += 1
    possible_lengths = [length for length, count in gcd_counts.items() if count > 0]
    possible_lengths.sort(key=lambda x: -gcd_counts[x])
    return possible_lengths


def kasiski_examination(ciphertext):
    repeated_sequences = find_repeated_sequences(ciphertext, 3)
    distances = get_distances(repeated_sequences)
    possible_key_lengths = get_possible_key_lengths(distances)
    print("Можливі довжини ключа за методом Касіскі:", possible_key_lengths)
    return possible_key_lengths