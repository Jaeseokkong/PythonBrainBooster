#딕셔너리 내포
number_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
word_to_number = {w: d for d, w in number_to_word.items()}
print(word_to_number)

# 책 암호
gen_code_keys = (lambda book, plain_text:(
    {c: str(book.find(c)) for c in plain_text}))

book = "Once upon a time, in a house in a land far away"
plain_text = "no is no"
print(gen_code_keys(book, plain_text))


encoder = (lambda code_keys, plain_text:
           ''.join(['*' + code_keys[c] for c in plain_text])[1:])

encrypt = (lambda book, plain_text:
           encoder(gen_code_keys(book, plain_text), plain_text))

Don_Quixote = book
print(encrypt(Don_Quixote, 'no is no'))

gen_decode_keys = (lambda book, cipher_text:(
    {s: book[int(s)] for s in cipher_text.split('*')}))

gen_decode_keys(Don_Quixote, '1*13*2*6*57*2*1*13')
