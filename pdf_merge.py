from PyPDF2 import PdfReader, PdfWriter
from utility import help_print
import os

def usage():
  print("""
  pdf merge - Used to merge pages from 1 or more pdf
  Output : output.pdf
  Usage: pdf merge file1.pdf file2.pdf 
  Advanced Usage:
  Use * to list all files
  Provide specific pages to extract and merge by using the format filename1.pdf[page_number_data]
  page_number_data: csv separated page information
  b -> add new blank page
  page_number -> extract only this page
  start_page_number-end_page_number -> extract page range end exclusive
  start_page_number- -> extract page range from start to end of pdf
  
  example: pdf merge a.pdf b.pdf[0,b,1-6,9-]

  """)

def merge(components):

  if len(list(filter(lambda x : x=="-h", components)))>0:
    help_print()

  file_names = []
  pages = {}

  for comp in components:
    if comp == "*":
      file_names.extend(list(filter(lambda x:x.endswith(".pdf") , os.listdir("."))))
    elif comp.endswith("]"):
      idx = comp.rindex("[")
      fname = comp[:idx]
      file_names.append(fname)
      pages[fname] = comp[idx+1:-1].split(",")
      print(pages)
      pass
    elif comp.endswith("pdf"):
      file_names.append(comp)
  with PdfWriter("output.pdf") as out:
    for fn in file_names:
      r = PdfReader(fn)
      if fn in pages:

        for consider in pages[fn]:
          if "b" in consider:
            out.add_blank_page()
          elif "-" in consider:
            page_range = consider.split("-")
            start_page = int(page_range[0])
            end_range = len(r.pages)
            if len(page_range) == 2:
              end_range = int(page_range[1])
            for i in range(start_page, end_range):
              out.add_page(r.pages[i])
          else:
            out.add_page(r.pages[int(consider)])
      else:
        for page in r.pages:
          out.add_page(page)

  pass