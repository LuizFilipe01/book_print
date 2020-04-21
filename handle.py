import PyPDF2 as pdf


class Pdf(object):
    def __init__(self):
        #arquivo = r"/home/master/Programas_python/book_print/teste.pdf"
        arquivo = r"/home/master/teste.pdf"

        self.pdf_input = pdf.PdfFileReader(arquivo)
        self.pdf_output = pdf.PdfFileWriter()

        self.pdf_output_2 = pdf.PdfFileWriter()

        # getPage

        self.num_pages = self.pdf_input.getNumPages()

        #page[0] é a capa
        self.pages = []

    def get_pages(self):
        for p in range(self.num_pages):
            self.pages.append(self.pdf_input.getPage(p))

        #self.pages.pop(0)

        return self.pages



    def write(self, pages):
        output = open('/home/master/m_frente.pdf', 'wb')

        for x in pages:
            self.pdf_output.addPage(x[0])
            self.pdf_output.addPage(x[-1])
            print('Ok: primeiro')

        self.pdf_output.write(output)

        output.close()
        pass
    

    def write_2(self, pages):
        output = open('/home/master/m_verso.pdf', 'wb')

        for x in pages:
            self.pdf_output_2.addPage(x[-1])
            self.pdf_output_2.addPage(x[0])
            print('Ok: segundo')


        self.pdf_output_2.write(output)

        output.close()
        pass




