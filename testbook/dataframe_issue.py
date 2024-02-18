# code in notebook would have function that takes dictionary
def create_graph(path_to_data):
  # first you would create the dataframe from the dictionary
  df = pandas.read_csv(path_to_data)
  # then you do what your function was doing before with the df created in the previous line


# in the test file
@testbook('test.ipynb', execute=True)
def test_create_graph(tb):
    create_graph = tb.ref("create_graph")

    foo("testdata.csv") # put your test data in a csv next to the test file, and put the filename of the csv here
