import gspread

gc = gspread.service_account()

sh = gc.open("Example spreadsheet")

ALPHABAT_LIST='ABCDEFGJIJ'

result_json = {
  'TID_FAIL01': 'failed',
  'TID_FAIL02': 'failed',
  'TID_FAIL03': 'failed',
  'TID_PASS01': 'passed',
  'TID_PASS02': 'passed',
  'TID_PASS03': 'passed',
  'TID_PASS04': 'passed',
  'TID_PASS05': 'passed'
  }


for i in range(1,100):
  test_id_on_sheet=sh.sheet1.cell(i, 1).value
  print('test_id_on_sheet {}'.format(test_id_on_sheet))
  if test_id_on_sheet=='':
    print("empty found, update done ?")
    break

  # sh.sheet1.update_cell(row,  column, testname)
  sh.sheet1.update_cell(i, 2, result_json[test_id_on_sheet])
