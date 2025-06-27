
morse = {
    # Letters
    "a": ".-","b": "-...","c": "-.-.","d": "-..","e": ".","f": "..-.","g": "--.",
    "h": "....","i": "..","j": ".---","k": "-.-","l": ".-..","m": "--","n": "-.",
    "o": "---","p": ".--.","q": "--.-","r": ".-.","s": "...","t": "-","u": "..-",
    "v": "...-","w": ".--","x": "-..-","y": "-.--","z": "--..",
    # Numbers
    "0": "-----","1": ".----","2": "..---","3": "...--","4": "....-",
    "5": ".....","6": "-....","7": "--...","8": "---..","9": "----.",
    # Punctuation
    "&": ".-...","'": ".----.","@": ".--.-.",")": "-.--.-","(": "-.--.",
    ":": "---...",",": "--..--","=": "-...-","!": "-.-.--",".": ".-.-.-",
    "-": "-....-","+": ".-.-.",'"': ".-..-.","?": "..--..","/": "-..-.",
}
decodemorse ={ m:n for n,m in morse.items()}
def decode_morse(message):
    """Decode a morse code message."""
    words = message.split('//')
    decoded_message = []
    for word in words:
        decoded_message.append(''.join(decodemorse.get(letter, '') for letter in word.split('/')))
    return ' '.join(decoded_message)

if __name__ == "__main__":
    message = input()
    decoded_message = decode_morse(message)
    print(decoded_message)
