text = "X-DSPAM-Confidence:    0.8475"

txt = text.find('0')
#print(txt)

num =  float(text[23:])
print(num)
