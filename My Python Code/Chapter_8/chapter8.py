def show_magicians(magicians):
  """Prints the name of each magician in the list."""
  for magician in magicians:
    print(magician.title())

magician_names = ['david copperfield', 'houdini', 'penn & teller', 'shin lim']
show_magicians(magician_names)


def make_great(magicians):
  """Adds 'the Great' to each magician's name in the list."""
  great_magicians = []
  for magician in magicians:
    great_magicians.append(f"the Great {magician.title()}")
  return great_magicians

def show_magicians(magicians):
  """Prints the name of each magician in the list."""
  for magician in magicians:
    print(magician)

magician_names = ['david copperfield', 'houdini', 'penn & teller', 'shin lim']
great_magician_names = make_great(magician_names)
show_magicians(great_magician_names)


def make_great(magicians):
  """Adds 'the Great' to each magician's name in a new list."""
  great_magicians = []
  for magician in magicians:
    great_magicians.append(f"the Great {magician.title()}")
  return great_magicians

def show_magicians(magicians):
  """Prints the name of each magician in the list."""
  for magician in magicians:
    print(magician)

magician_names = ['david copperfield', 'houdini', 'penn & teller', 'shin lim']
great_magician_names = make_great(magician_names[:])  # Passing a copy of the list

print("Original Magicians:")
show_magicians(magician_names)

print("\nGreat Magicians:")
show_magicians(great_magician_names)


def make_sandwich(*items):
  """Prints a summary of the items on a sandwich."""
  print("\nMaking a sandwich with the following items:")
  for item in items:
    print(f"- {item.title()}")
  print("Enjoy your sandwich!")

make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('roast beef', 'cheddar cheese')
make_sandwich('peanut butter', 'jelly', 'banana', 'honey')

def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user."""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

my_profile = build_profile('john', 'doe',
                             location='pietermaritzburg',
                             field='software development',
                             favorite_color='blue')

print(my_profile)


car = make_car('subaru', 'outback', color='blue', tow_package=True)

def make_car(manufacturer, model, **kwargs):
  """Store information about a car in a dictionary."""
  car_info = {
      'manufacturer': manufacturer.title(),
      'model': model.title(),
  }
  car_info.update(kwargs)
  return car_info

my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)

another_car = make_car('toyota', 'camry', year=2023, sunroof=False)
print(another_car)