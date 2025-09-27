class CompoundWordSplitter:
    def __init__(self):
        self.common_words = {
            'a', 'an', 'the', 'i', 'you', 'he', 'she', 'it', 'we', 'they',
            'is', 'am', 'are', 'was', 'were', 'be', 'being', 'been',
            'have', 'has', 'had', 'do', 'does', 'did',
            'and', 'but', 'or', 'nor', 'for', 'yet', 'so',
            'in', 'on', 'at', 'by', 'with', 'about', 'against',
            'to', 'from', 'up', 'down', 'of', 'off', 'over', 'under',
            'this', 'that', 'these', 'those',
            'my', 'your', 'his', 'her', 'its', 'our', 'their',
            'not', 'no', 'yes', 'very', 'too', 'much', 'many',
            'one', 'two', 'three', 'first', 'second', 'third',
            'big', 'small', 'good', 'bad', 'hot', 'cold', 'new', 'old',
            'time', 'person', 'year', 'way', 'day', 'thing', 'man', 'world',
            'life', 'hand', 'part', 'child', 'eye', 'woman', 'place', 'work',
            'week', 'case', 'point', 'government', 'company', 'number', 'group',
            'problem', 'fact', 'water', 'fire', 'air', 'earth', 'sun', 'moon',
            'book', 'pen', 'paper', 'computer', 'phone', 'car', 'house', 'food',
            'note', 'book', 'note', 'book', 'note', 'book', 'note', 'book'
        }
        
        self.compound_patterns = [
            ('note', 'book'), ('foot', 'ball'), ('basket', 'ball'), ('base', 'ball'),
            ('sun', 'flower'), ('rain', 'bow'), ('snow', 'flake'), ('star', 'fish'),
            ('tooth', 'brush'), ('hair', 'brush'), ('air', 'port'), ('sea', 'port'),
            ('book', 'shelf'), ('word', 'processor'), ('key', 'board'), ('mouse', 'pad'),
            
            ('black', 'board'), ('green', 'house'), ('blue', 'berry'), ('hot', 'dog'),
            ('soft', 'ware'), ('hard', 'ware'), ('free', 'dom'), ('high', 'way'),
            
            ('break', 'fast'), ('play', 'ground'), ('swim', 'pool'), ('drive', 'way'),
            ('park', 'way'), ('run', 'way'), ('check', 'point'), ('search', 'light'),
            
            ('under', 'ground'), ('over', 'coat'), ('after', 'noon'), ('before', 'noon')
        ]
    
    def split_compound(self, word):
        word = word.lower()
        for split_pos in range(1, len(word)):
            part1 = word[:split_pos]
            part2 = word[split_pos:]
            if self._is_valid_word(part1) and self._is_valid_word(part2):
                return part1, part2
        return (word,)
    
    def _is_valid_word(self, word):
        return (word in self.common_words or 
                len(word) > 2 and word.isalpha())
    
    def split_multiple(self, words):
        results = []
        for word in words.split():
            parts = self.split_compound(word)
            results.extend(parts)
        return ' '.join(results)

def split_compound_word(word):
    common_splits = {
        'notebook': ['note', 'book'],
        'football': ['foot', 'ball'],
        'basketball': ['basket', 'ball'],
        'baseball': ['base', 'ball'],
        'sunflower': ['sun', 'flower'],
        'rainbow': ['rain', 'bow'],
        'toothbrush': ['tooth', 'brush'],
        'hairbrush': ['hair', 'brush'],
        'airport': ['air', 'port'],
        'seaport': ['sea', 'port'],
        'bookshelf': ['book', 'shelf'],
        'blackboard': ['black', 'board'],
        'greenhouse': ['green', 'house'],
        'blueberry': ['blue', 'berry'],
        'hotdog': ['hot', 'dog'],
        'software': ['soft', 'ware'],
        'hardware': ['hard', 'ware'],
        'freedom': ['free', 'dom'],
        'highway': ['high', 'way'],
        'breakfast': ['break', 'fast'],
        'playground': ['play', 'ground'],
        'swimmingpool': ['swimming', 'pool'],
        'driveway': ['drive', 'way']
    }
    word = word.lower()
    return common_splits.get(word, [word])

def test_splitter():
    print("Compound Word Splitter Test")
    print("=" * 40)
    test_words = [
        'notebook', 'football', 'basketball', 'sunflower',
        'rainbow', 'toothbrush', 'airport', 'blackboard',
        'greenhouse', 'breakfast', 'playground', 'hello'
    ]
    splitter = CompoundWordSplitter()
    print("Class Version Results:")
    for word in test_words:
        result = splitter.split_compound(word)
        print(f"{word:15} → {' + '.join(result)}")
    print("\n" + "=" * 40)
    print("Simple Function Results:")
    for word in test_words:
        result = split_compound_word(word)
        print(f"{word:15} → {' + '.join(result)}")

def interactive_demo():
    print("Compound Word Splitter - Interactive Mode")
    print("Type 'quit' to exit")
    print("=" * 40)
    splitter = CompoundWordSplitter()
    while True:
        user_input = input("\nEnter a compound word: ").strip()
        if user_input.lower() == 'quit':
            break
        if user_input:
            result1 = splitter.split_compound(user_input)
            result2 = split_compound_word(user_input)
            print(f"Class method: {' + '.join(result1)}")
            print(f"Simple method: {' + '.join(result2)}")

if __name__ == "__main__":
    test_splitter()
    print("\n" + "=" * 50)
    print("Try the interactive demo below:")
    interactive_demo()
