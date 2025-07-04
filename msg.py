import random
import string

def generate_random_chars(length=3):
    """generate random lowercase letters of given length"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
def code_word(word):
    if len(word) >= 3:
        coded = word[1:] + word[0]
        return generate_random_chars() + coded + generate_random_chars()
    else:
        return word[::-1]



def decode_word(word):
    if len(word) < 3:
        return word[::-1]
    else:
        trimmmed = word[3:-3]
        return trimmmed [-1] + trimmmed[:-1]







def process_text(text, operation):
    """Process entire text (coding or decoding)""" 
    words = text.split()
    processor = code_word if operation == 'code' else decode_word
    return ' '.join(processor(word) for word  in words)
 



def main():
    print("Secret Code Language Translator")
    while True:
        print("\nOptions:")
        print("\nOptions:")
        print("1. Code a message")
        print("2. Decode a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '3':
            print("Exiting the program. Goodbye!")
            break
            
        if choice not in ('1', '2'):
            print("Invalid choice. Please try again.")
            continue
            
        operation = 'code' if choice == '1' else 'decode'
        message = input(f"Enter the message to {operation}: ").strip()
        
        if not message:
            print("Message cannot be empty!")
            continue
            
        result = process_text(message, operation)
        print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
        








