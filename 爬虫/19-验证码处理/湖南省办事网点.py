import ddddocr
ocr = ddddocr.DdddOcr()
with open("verifyCode.png", 'rb') as f:
    img_bytes = f.read()
red = ocr.classification(img_bytes)
print(red)