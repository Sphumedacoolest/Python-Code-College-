import external_module

def process_data(name, age, city):
  """Processes the received arguments."""
  print(f"Name: {name}")
  print(f"Age: {age}")
  print(f"City: {city}")

if __name__ == "__main__":
  data = external_module.get_data()
  process_data(**data)