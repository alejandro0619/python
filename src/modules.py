import modules_one
from docx import Document

document = Document()
document.add_heading('Document Title', 0)
document.save("aa.docx")
modules_one.say_hello("Juan")