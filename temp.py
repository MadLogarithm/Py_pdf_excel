import pdfplumber
import pandas as pd
import glob

# with pdfplumber.open('./test.pdf') as pdf:
#     for page in pdf.pages:
#         text = page.extract_text()
#         print(text)


# path = "H:/py_pdf/*.pdf"
# file_list = glob.glob(path)
# # print(file_list)
# for filename in file_list:
#     # print(filename)
#     with pdfplumber.open(filename) as pdf:
#     # with pdfplumber.open(filename, password = pwd) as pdf:
#         cnt = 0
#         writer = pd.ExcelWriter(str(filename)[:-4]+'.xlsx', engine='xlsxwriter')
#         for page in pdf.pages:
#             # print(page)
#             tables = page.extract_tables()
#             for table in tables:
#                 # print(table)
#                 cnt += 1
#                 table_df = pd.DataFrame(table)
#                 # table_df = pd.DataFrame(table[1:],columns = table[0])
#                 table_df.to_excel(writer, sheet_name='sheet'+str(cnt))
#                 # print(table_df)
#                 # for row in table:
#                 #     print(row)
#         writer.save()

def tail_not_space_char(page_chars):
    i = -1
    while page_chars[i].get('text').isspace():
        i -= 1
    return page_chars[i]

def head_not_space_char(page_chars):
    i = 0
    while page_chars[i].get('text').isspace():
        i += 1
    return page_chars[i]


def ectract_tables(filename):
    with pdfplumber.open(filename) as pdf:
        y0_bottom_char = []
        y0_bottom_table = []
        y1_top_char = []
        y1_top_table = []
        text_all_table = []

        for page in pdf.pages:
            table_objects = page.find_tables()
            text_table_current_page = page.extract_tables()
            if text_table_current_page:
                text_all_table.append(text_table_current_page)
                y0_bottom_char.append(tail_not_space_char(page.chars).get('y0'))
                y0_bottom_table.append(page.bbox[3] - table_objects[-1].bbox[3])
                y1_top_char.append(head_not_space_char(page.chars).get('y1'))
                y1_top_table.append(page.bbox[3] - table_objects[0].bbox[1])

        i = 0
        while i < len(text_all_table):
            if i + 1 >= len(text_all_table):
                break
            j = i + 1
            k = 1
            while text_all_table[j]:
                if y0_bottom_table[i] <= y0_bottom_char[i] and y1_top_table[j] >= y1_top_char[j]:
                    text_all_table[i][-1] = text_all_table[i][-1] + text_all_table[j][0]
                    text_all_table[j].pop(0)
                    if not text_all_table[j] and j + 1 < len(text_all_table) and text_all_table[j + 1]:
                        k += 1
                        j += 1
                    else:
                        i += k
                        break
                else:
                    i += k
                    break
        
        # writer = pd.ExcelWriter('./excel/' + str(filename)[6:-4] + '.xlsx', engine= 'xlsxwriter')
        writer = pd.ExcelWriter('./excel/' + str(filename)[10:-4] + '.xlsx', engine= 'xlsxwriter')
        for page_num, page in enumerate(text_all_table):
            for table_num, table in enumerate(page):
                if table:
                    table_df = pd.DataFrame(table[1:], columns= table[0])
                    table_df.to_excel(writer, sheet_name= 'page{0}_table{1}'.format(page_num, table_num))
        writer.save()

if __name__ == '__main__':

    # path = "./pdf/*.pdf"
    path = "./cut_pdf/*.pdf"
    file_list = glob.glob(path)
    for filename in file_list:
        ectract_tables(filename)