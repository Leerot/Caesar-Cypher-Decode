ascii_banner = """
By
 ___       _______   _______   ________  ________  _________   
|\  \     |\  ___ \ |\  ___ \ |\   __  \|\   __  \|\___   ___\ 
\ \  \    \ \   __/|\ \   __/|\ \  \|\  \ \  \|\  \|___ \  \_| 
 \ \  \    \ \  \_|/_\ \  \_|/_\ \   _  _\ \  \\\  \   \ \  \  
  \ \  \____\ \  \_|\ \ \  \_|\ \ \  \\  \\ \  \\\  \   \ \  \ 
   \ \_______\ \_______\ \_______\ \__\\ _\\ \_______\   \ \__\\
    \|_______|\|_______|\|_______|\|__|\|__|\|_______|    \|__|
"""
           





import string

def poly(plain: str, key: int) -> str:
    plain = plain.lower()
    alpha = string.ascii_lowercase
    shifted = alpha[key:] + alpha[:key]
    sub_dict = dict(zip(alpha, shifted))

    def encdec(c):
        return sub_dict[c] if c in sub_dict else c

    result = ''.join(encdec(c) for c in plain)
    return result.upper()

def main():
    print(ascii_banner)
    default_text = "UMHTGSJV TWXGJW DGSV TJAUC"
    cipher_input = input(f"String Cypher Caesar a descifrar (default: '{default_text}'): ").strip()
    if not cipher_input:
        cipher_input = default_text

    print("\n[*] 'Caesar Cipher' desencriptando con 26 keys:\n")
    for key in range(26):
        decrypted = poly(cipher_input, key)
        print(f"Key {key:2}: {decrypted}")

if __name__ == "__main__":
    main()
