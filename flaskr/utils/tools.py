
unit_type = {
  'Piece'   : 0,
  'Kilogram': 1,
  'Gram' : 2,
  'Litre': 3,
  'Centilitre': 4,
  'Millilitre': 5
}

def get_unit_type(unit):
  return unit_type[unit]

def cast_stringy_boolean(bool):
  if bool == 'true':
    return 1
  elif bool == 'false':
    return 0
