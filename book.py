#!C:\Sangeeta\python
import xml.etree.ElementTree as ET
tree = ET.parse('Books.xml')
root = tree.getroot()
for book in root.findall('book'):
     author = book.find('author').text
     id = book.get('id')
     print("%s was written by %s" % (id, author))	  