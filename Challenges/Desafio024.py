cid = str(input('Digite a sua cidade: ')).strip().upper()
pos = cid.find('SANTO')
if pos == 0:
    print('Sua cidade começa com a palavra SANTO!')
else:
    print('Sua cidade não começa com a palavra SANTO!')
