from handle import Pdf


new_pdf = Pdf()

pages = new_pdf.get_pages()
print('Número de páginas: ', len(pages))

#s_pages = 12
#s_book = []
#book = []

book = pages

internas = []
externas = []

for x in range(len(book)):
    s_book.append(x+1)

#-------------------------------------------------------

for x in range(int(len(book)/2)):
    c = x % 2

    if c != 0:
        internas.append([book[0], book[-1]])
        book.pop(0)
        book.pop(-1)
        print('Inpar')
        pass
        # 2-11, 4-9, 6-7

    else:
        externas.append([book[0], book[-1]])
        book.pop(0)
        book.pop(-1)
        print('Par')
        # 1-12, 3-10, 5-8

    pass

externas.reverse() #segundo
internas.reverse() #primeiro

new_pdf.write(internas)
new_pdf.write_2(externas)


    


