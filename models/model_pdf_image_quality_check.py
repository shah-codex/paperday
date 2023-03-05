import fitz
import datetime
import numpy as np
from skimage import io, img_as_float
import imquality.brisque as brisque
doc = fitz.open("Doc1.pdf")
page=len(doc)
j=0
img_l = []
score = []
score_label = []
for i in range(page):
    for img in doc.get_page_images(i):
        print(j)
        customxref=img[0]
        pic=fitz.Pixmap(doc,customxref)
        finalpic = fitz.Pixmap(fitz.csRGB,pic)
        finalpic.save(str(j)+".png")
        img_l.append(img_as_float(io.imread(str(j)+".png",as_gray=True)))
        score.append(brisque.score(img_l[j]))
        if score[j] <= 25:
            score_label.append("Very Good")
        elif 25 < score[j] <= 50:
            score_label.append("Good")
        elif 50 < score[j] <= 65:
            score_label.append("Normal")
        elif 65 < score[j] <= 100:
            score_label.append("Bad")
        elif score[j] > 100:
            score_label.append("Very Bad")
        elif score[j] < 0:
            score_label.append("Excellent")
        else:
            score_label.append("Undefined")
        print(score[j])
        print(score_label[j])
        pic=None
        finalpic=None
        j = j+1
        