
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
result = tokenizer.tokenize("Wow! I am excited to learn Compiler Designing")
print(result)