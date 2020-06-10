from memoization import cached
from os import listdir

def set_data_folder(dir_string = "./", tries_count = 0):
  dir = listdir(dir_string)

  if tries_count == 3:
    raise FileNotFoundError("Você está executando esse código em um diretório estranho, execute-o diretamente da pasta src")

  if 'data' in dir:
    return "{}data/".format(dir_string)
  else:
    return set_data_folder("{}../".format(dir_string), tries_count + 1)


DATA_FOLDER = set_data_folder()

@cached
def get_file(filename):
  return open("{}{}".format(DATA_FOLDER, filename), "r")

def get_gastos_file(ano):
  return get_file("gastos-{}.xlsx".format(ano))

def get_gastos_path(ano):
  return "{}gastos-{}.xlsx".format(DATA_FOLDER, ano)
