from pdf2docx import Converter

sample = 'samplepdf.pdf'
new_doc = 'sample.docx'

obj = Converter(sample)
obj.convert(new_doc)
obj.close()
