import click
import json

class ParseDataJSON():
  """docstring for ParseDataJSON"""
  def __init__(self, json_file):
    self.json_file= json_file
  def parse_data(self):
    self.data_dict = {}
    with open(self.json_file, 'r') as f:
      data = f.read()
      self.data_dict =json.loads(data)

@click.command()
@click.argument('json_file', type=click.Path(exists=True, dir_okay=False))
def main(json_file):
  parsed_data = ParseDataJSON(json_file)
  parsed_data.parse_data()
  print(parsed_data.data_dict['PlotTitle'])
  return 0

if __name__ == '__main__':
  main()