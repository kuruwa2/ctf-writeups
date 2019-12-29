c = "2bi4j2fcjli84edk07kbjj3cggg3k5ih0hcgg710260lak1ibead1gf15hflb5f41"

m = int(c,22)

import codecs
print(codecs.decode(hex(m)[2:],'hex'))
