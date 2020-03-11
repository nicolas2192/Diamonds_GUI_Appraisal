import packages.GUI.GUI as gui
import argparse
from glob import glob

parser = argparse.ArgumentParser(description="Calculates a diamond's price given certain features")
parser.add_argument("-m", "--model", type=str, metavar="", help="Model used to predict",
					default=glob("data/model_binary/*.pkl")[0])
args = parser.parse_args()


def main():
	# loading GUI
	model = args.model
	gui.load_GUI(model)


if __name__ == "__main__":
	main()
