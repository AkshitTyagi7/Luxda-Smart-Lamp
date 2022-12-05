import base64
def convert(string):#write mode

#  file1.write(string)
 string += "=" * ((4 - len(string) % 4) % 4) #ugh
 convert=bytes(string, 'utf-8')
 wav_file = open("temp.wav", "wb")
 decode_string = base64.b64decode(convert)
 wav_file.write(decode_string)
# file1 = open("try.txt","r+")
# text=file1.read()
# convert(text)