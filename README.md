# Py_pdf_excel

Extract tables from pdf to excel by python.

- Resolved:
  - Basic extraction function
  - Simple cross page table extraction (without header or footer)
- To do list:
  - Cross page table extraction (with header or footer)
    - Idea: Directly delete the header and footer?
      - Try cutting, but failed. It has been proven that cropBox is changing the visible part of the PDF. The other parts are all there, but they just can't be seen.
