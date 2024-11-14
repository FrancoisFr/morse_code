import click

### function to decode morse_code
def decode_morse(morse_code):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9'
    }

    letters = morse_code.split('/')
    decoded_message = ''
        
    for letter in letters:
        decoded_message += morse_dict.get(letter, '')

    return decoded_message.strip()


### function to encode in morse a string
def encode_morse(message):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'
    }
    
    # Convert the message to uppercase and remove leading/trailing whitespaces
    message = message.upper().strip()
    encoded_message = []
    
    # Encode each character in Morse
    for char in message:
        if char in morse_dict:
            encoded_message.append(morse_dict[char])
        elif char == ' ':
            # Separate words with "/"
            encoded_message.append('/')
    
    return ' '.join(encoded_message)

# Exemple d'utilisation
text = "HELLO WORLD"
morse_code = encode_morse(text)
print(morse_code)

# Commande principale
@click.command()
@click.argument('text')
@click.option('--mode', type=click.Choice(['encode', 'decode'], case_sensitive=False), required=True, help="Mode de transformation : 'encode' to encode in Morse, 'decode' to decode in clear.")
def cli(text, mode):
    """Encode or Decode a message in Morse code."""
    if mode == 'encode':
        result = encode_morse(text)
        click.echo(f"Message encoded in Morse : {result}")
    elif mode == 'decode':
        result = decode_morse(text)
        click.echo(f"Message decoded : {result}")

if __name__ == '__main__':
    cli()