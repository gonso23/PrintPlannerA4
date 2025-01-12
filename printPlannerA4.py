# 2 sided printing

#Personal, Standard, Medium, Classic Planer 17,1 * 9,5 cm (min 0,7mm punch hole margin left)
#Max Fit 18 cm * 9,9 cm

#Page width 8,8cm | 249px + 0,7cm | 20px margin
#Page 17,1cm | 485px

from __future__ import print_function
import fitz, sys
import os
import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith(".pdf"):
    print("usage: {} <input.pdf>".format(sys.argv[0]))
    sys.exit()

IN = sys.argv[1]
OUT = f"{os.path.splitext(IN)[0]}_p1.pdf"

PHM = 20 #punch hole margin 20 pixel aprox 0,7cm

src = fitz.open(IN)
dst = fitz.open()  # empty output PDF

outWidth, outHeight = fitz.paper_size("a4-l")  # A4 landscape output page format

print("outWidth: " , outWidth)
print("outHeight: " , outHeight)

#first page shapes the output!
inWidth = src[0].rect.width
inHeight = src[0].rect.height

if(inWidth>inHeight): #fit page orientation
    print("fix page orientation")
    t = inWidth
    inWidth = inHeight
    inHeight = t

print("inWidth: " , inWidth)
print("inHeight: " , inHeight)

if (inWidth+PHM) * 3 > outWidth: #Limit outWidth
    inWidth = (outWidth / 3) - PHM
    print("fix inWidth: " , inWidth)

if inHeight > outHeight*485/595: #Limit outHeight 510 => 18cm 485px => 17,1cm
    inHeight = outHeight*485/595
    print("fix inHeight: " , inHeight)


# define the 3 rectangles front PHM on the left
rf1 = fitz.Rect(PHM, 0, inWidth+PHM, inHeight)
rf2 = fitz.Rect(inWidth+2*PHM, 0, 2*(inWidth+PHM), inHeight)
rf3 = fitz.Rect(2*(inWidth+PHM)+PHM, 0, 3*(inWidth+PHM), inHeight)
#order how they appear on output
r_tab = [rf1, rf2, rf3]


for ipage in src:
    if ipage.number % 3 == 0:  # create new output page
        #cutting edge
        page = dst.new_page(-1, width=outWidth, height=outHeight)
        page.draw_line((0, inHeight),(outWidth, inHeight)) # Long Edge
        page.draw_line((inWidth+PHM, inHeight),(inWidth+PHM, outHeight)) # Page 1 
        page.draw_line((2*(inWidth+PHM), inHeight),(2*(inWidth+PHM), outHeight))
        page.draw_line((3*(inWidth+PHM), inHeight),(3*(inWidth+PHM), outHeight))
        
        #page outer frame
        page.draw_line((0, outHeight),(outWidth, outHeight))
        page.draw_line((0, 0),(0, outHeight))
        page.draw_line((0, 0),(outWidth, 0))
        page.draw_line((outWidth, 0),(outWidth, outHeight))
        
        
    #fit page orientation
    if(src[ipage.number].rect.width > src[ipage.number].rect.height):
        print("page: " +str(ipage.number)+ " rotation")
        src[ipage.number].set_rotation(0)
    
    page.show_pdf_page(r_tab[ipage.number % 3], src, ipage.number, False )

dst.save(OUT, garbage=4, deflate=False)

src.close()
dst.close()