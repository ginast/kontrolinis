"""Sukurti programa, kuri uždėtų nuotraukai kontrastą ir išsaugotų atnaujintą nuotrauką
"""

from PIL import Image, ImageEnhance

nissan = Image.open('300zx.png')
enh = ImageEnhance.Contrast(nissan)
enh.enhance(5).show()

#jeigu norime išsaugoti:
enh.enhance(2).save('300zx_kontrastas.png')
