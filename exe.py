from Graph_generator_for_GNN.parsing.Generator import generate
import os

file_name = '2860.sol'

file_path = os.path.abspath('../Graph_generator_for_GNN/origin_sol_code/' + file_name)
generate(file_path, file_name)