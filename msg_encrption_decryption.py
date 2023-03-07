# creating dictionary according to given key
def encrypt_msg(msg,key,d):
    for c in (65,97):
        for i in range(26):
            d[chr(i+c)] = chr( ( (i+key)%26 ) + c )
    print('Message after encryption is:',''.join([d.get(c,c) for c in msg]))


def decrypt_msg(msg,key,d):
    for c in (65,97):
        for i in range(26):
            d[chr(i+c)] = chr( ( (i-key)%26 ) + c )
    print('Message after decryption is:',''.join([d.get(c,c) for c in msg]))

d  = {}
msg = input('Enter message to [encrypt/decrypt]:')

print('='*60)
print('1:Encrypt Message','2:Decrypt Message',sep='\n')
print('='*60)

choice = int(input('Enter choice[1/2]:'))

key = int(input('Enter the key to [encrypt/decrypt]:'))

if choice == 1:
    encrypt_msg(msg,key,d)
else:
    decrypt_msg(msg,key,d)



