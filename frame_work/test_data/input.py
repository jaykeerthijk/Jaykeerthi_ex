def values():
    import xlrd
    f_path = r"C:\Users\Jagadeesh\Desktop\data_to_input.xlsx"
    xl_obj = xlrd.open_workbook(f_path)
    # with open(f_path) as f:
    sheet1 = xl_obj.sheet_by_name("Input")
    data = sheet1.get_rows()
    #headers = next(data)
    #print(data)
    for rowno, row in enumerate(data):
        if row[0].value == 'test_login':
            data = sheet1.row_values(rowno, start_colx=0)
            print(data)
            #break
        #print(row[0].value, row[1].value)
values()
