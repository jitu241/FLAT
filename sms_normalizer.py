class SimpleSMSNormalizer:
    def __init__(self):
        
        self.sms_map = {
            'u': 'you',
            'r': 'are',
            '2': 'to',
            '4': 'for',
            '8': 'ate',
            'gr8': 'great',
            'l8r': 'later',
            'b4': 'before',
            'plz': 'please',
            'thx': 'thanks',
            'msg': 'message',
            'c': 'see'
        }
    
    def normalize(self, text):
       
        words = text.split()
        result = []
        
        for word in words:
          
            if word in self.sms_map:
                result.append(self.sms_map[word])
            else:
                result.append(word)
        
        return ' '.join(result)

def test_simple_normalizer():
    normalizer = SimpleSMSNormalizer()
    
    test_cases = [
        ("u", "you"),
        ("r u there", "are you there"),
        ("c u l8r", "see you later"),
        ("plz come b4 8", "please come before ate"),
        ("thx for the msg", "thanks for the message"),
        ("hello world", "hello world")
    ]
    
    print("Simple SMS Normalizer Test Results:")
    print("=" * 40)
    
    for sms_input, expected in test_cases:
        result = normalizer.normalize(sms_input)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input:  '{sms_input}'")
        print(f"  Output: '{result}'")
        print(f"  Expected: '{expected}'")
        print()


def simple_interactive():
    normalizer = SimpleSMSNormalizer()
    
    print("=== Simple SMS Normalizer ===")
    print("Type 'quit' to exit")
    print("Supported abbreviations: u, r, 2, 4, 8, gr8, l8r, b4, plz, thx, msg, c")
    print("-" * 40)
    
    while True:
        user_input = input("\nEnter SMS text: ").strip()
        
        if user_input.lower() == 'quit':
            break
            
        if user_input:
            result = normalizer.normalize(user_input)
            print(f"Normalized: {result}")

if __name__ == "__main__":
    #test_simple_normalizer()
    
    # Uncomment below to run interactive mode
     simple_interactive()