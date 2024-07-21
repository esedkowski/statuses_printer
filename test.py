from pylatex import Document, Section, Subsection

doc=Document(documentclass='article')

# creating a pdf with title "the simple stuff"
with doc.create(Section('The simple stuff')):
    doc.append('Some regular text and some')

doc.generate_pdf('full', clean_tex=False)

