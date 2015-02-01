def convert(num, form=1):
  """Converts interger to roman system.
  Args:
    num: integer to convert as int.
    form: form for representing result as int, could be 1 for simple form or 2 for advanced.

  Returns:
    Roman style num or None if int <= 0

  """
  if num >0:
    simple_form = [(1000, "M"),(500, "D"),(100, "C"),(50, "L"),(10, "X"),(5, "V"),(1, "I")]
    advanced_form = [(1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),(90, "XC"),
                     (50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"),(4, "IV"),(1, "I")]
    convert_form = simple_form
    if form == 2:
      convert_form = advanced_form
    print convert_form
    result = ''
    for item in convert_form:
            while num >= item[0]:
                    num -= item[0]
                    result += item[1]
    return result
  return 'Give me valid integer'
