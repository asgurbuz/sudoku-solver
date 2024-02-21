from paddleocr import PaddleOCR,draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
img_path = 'z.webp'
result = ocr.ocr(img_path, cls=True)

for idx in range(len(result)):
    res = result[idx]



# import required module
from PIL import Image

# get image
img = Image.open(img_path)

# get width and height
width,height = img.size
rowSize , colSize = width//9 , height//9

grid = [[0 for col in range(9)] for row in range(9)]

for idx in range(len(result)):
    res = result[idx]
    for line in res:
      grid[int(line[0][0][1]//rowSize)][int(line[0][0][0]//colSize)] = int(line[1][0])

for s in grid:
  print(s)
