class MorseConverter:
    def __init__(self):
        self.morse_code_dict = {
            'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.', 
            'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',   'J': '.---', 
            'K': '-.-',  'L': '.-..', 'M': '--', '  N': '-.',   'O': '---', 
            'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-', 
            'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--', 
            'Z': '--..', '0': '-----','1': '.----','2': '..---','3': '...--', 
            '4': '....-','5': '.....','6': '-....','7': '--...','8': "---..", 
            "9": "----."
        }
    
    def text_to_morse(self, text):

        text =  " ".join(self.morse_code_dict.get(char.upper(), '<UNKNOWN>') for char in text if char.upper() in self.morse_code_dict)
        print(f"Converted text to Morse: {text}")
        return text
    