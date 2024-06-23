gen_code_keys = (lambda book, plain_text:(
    {c: str(book.find(c)) for c in plain_text}))
plain_text = "no is no"
book = "In a village of La Mancha, the name of which I have no desire to call \
to mind, there lived not long since one of those gentlemen that keep a lance \
in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing."
gen_code_keys(book, plain_text)

encoder = (lambda code_keys, plain_text:
           ''.join(['*' + code_keys[c] for c in plain_text])[1:])

encrypt = (lambda book, plain_text:
           encoder(gen_code_keys(book, plain_text), plain_text))

Don_Quixote = book
encrypt(Don_Quixote, 'no is no')

gen_decode_keys = (lambda book, cipher_text:(
    {s: book[int(s)] for s in cipher_text.split('*')}))

code_message = encrypt(Don_Quixote, 'z is not in the book')
# 암호화된 메시지에 ?가 포함되지 않는다고 가정합니다
new_Don_Quixote = Don_Quixote + '?'
print(gen_decode_keys(new_Don_Quixote, code_message))


decoder = (lambda decode_keys, encrypted_text: (
           ''.join([decode_keys[i] for i in encrypted_text.split('*')])))
decrypt = (lambda book, encrypted_text:
           decoder(gen_decode_keys(book, encrypted_text), encrypted_text))
encrypted_text = '22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*\
137*59*11*23*11*1*57*6*173*7*11'
print(decrypt(Don_Quixote, encrypted_text))