from collections import Counter

def calculate_ic(text):
    N = len(text)
    frequencies = Counter(text)
    ic = sum(f * (f - 1) for f in frequencies.values()) / (N * (N - 1))
    return ic

def friedman_test(text, max_key_length=20):
    ics = []
    for key_len in range(1, max_key_length + 1):
        subtexts = ['' for _ in range(key_len)]
        for i, char in enumerate(text):
            subtexts[i % key_len] += char
        ic = sum(calculate_ic(sub) for sub in subtexts) / key_len
        ics.append((key_len, ic))
    return ics

def frequency_analysis(subtext):
    frequencies = Counter(subtext)
    N = len(subtext)
    if N == 0:
        return 'A'  # Default to 'A' if subtext is empty to avoid errors

    # Updated English letter frequency (normalized to probabilities)
    letter_frequency = {
        'E': 12.0, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95,
        'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88,
        'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03,
        'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11,
        'J': 0.10, 'Z': 0.07
    }
    expected = [letter_frequency[chr(i + ord('A'))] / 100 for i in range(26)]
    chi_squareds = []

    for shift in range(26):
        chi2 = 0.0
        for i in range(26):
            c = chr((i + shift) % 26 + ord('A'))
            observed = frequencies.get(c, 0) / N
            expected_freq = expected[i]
            chi2 += ((observed - expected_freq) ** 2) / expected_freq if expected_freq > 0 else 0
        chi_squareds.append((chi2, shift))

    # Find the shift with the smallest chi-squared value
    _, best_shift = min(chi_squareds)
    key_char = chr(best_shift + ord('A'))
    return key_char


def friedman_examination(ciphertext):
    ics = friedman_test(ciphertext)
    # Виводимо результати
    print("Результати тесту Фрідмана (довжина ключа та IC):")
    for key_len, ic in ics:
        print(f"Довжина ключа {key_len}: IC = {ic}")
    # Вибираємо довжину ключа з IC найближчим до 0.065
    possible_key_lengths = [key_len for key_len, ic in ics if abs(ic - 0.065) < 0.005]
    print("Можливі довжини ключа за тестом Фрідмана:", possible_key_lengths)
    return possible_key_lengths