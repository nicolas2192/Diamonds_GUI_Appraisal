import tkinter as tk
import pickle
import pandas as pd


def num_check(element):
	try:
		float(element)
		return float(element)
	except ValueError:
		print("X, Y, Z, Depth, Table and Carat values must be numbers. The program has stopped!")
		exit()


def cat_check(element):
	if element != "":
		return element
	else:
		print("Cut, Color and Clarity cannot be left empty. The program has stopped!")
		exit()


def get_values(entry_x, entry_y, entry_z, entry_depth, entry_table, entry_carat, cut_var, color_var, clarity_var, model):
	value_x = num_check(entry_x)
	value_y = num_check(entry_y)
	value_z = num_check(entry_z)
	value_depth = num_check(entry_depth)
	value_table = num_check(entry_table)
	value_carat = num_check(entry_carat)
	value_cut = cat_check(cut_var)
	value_color = cat_check(color_var)
	value_clarity = cat_check(clarity_var)

	features_dict = {"x": [value_x], "y": [value_y], "z": [value_z], "depth": [value_depth], "table": [value_table],
					 "carat": [value_carat], "cut": [value_cut], "color": [value_color], "clarity": [value_clarity]}

	# Generating dataframe to predict
	df_to_predict = pd.DataFrame(features_dict)

	# Loading model
	with open(model, "rb") as f:
		loaded_model = pickle.load(f)
		print("Model loaded!")

	# price prediction
	predicted_price = loaded_model.predict(df_to_predict)

	global price_var
	calculated_price = round(predicted_price[0], 2)
	price_var.set(f"$ {calculated_price}")
	print(f"Calculated price: {calculated_price}")


def load_GUI(model):
	# Instantiate tkinter and initial settings
	root = tk.Tk()
	root.title("Diamond Appraisal")
	root.resizable(width=False, height=False)

	canvas = tk.Canvas(root, height=500, width=700)
	canvas.pack()

	bg_img = tk.PhotoImage(file="images/bg2.png")  # /home/nicolas/Reps/Diamonds_Appraisal/images/bg2.png
	back_label = tk.Label(root, image=bg_img)
	back_label.place(relheight=1, relwidth=1)

	# Features frame
	frame1 = tk.Frame(root, bg="black")
	frame1.place(relx=0.06, rely=0.15, relheight=0.7, relwidth=0.4)

	# Button and price prediction frame
	frame2 = tk.Frame(root, bg="black")
	frame2.place(relx=0.575, rely=0.435, relheight=0.25, relwidth=0.3)

	# Constants
	LABEL_BG_COLOR = "black"
	FONT = "Arial 16"
	ENTRY_BG_COLOR = "#D3D3D3"
	CUT_LIST = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
	COLOR_LIST = ["J", "I", "H", "G", "F", "E", "D"]
	CLARITY_LIST = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
	Xpos, Ypos = 0.05, 0.05
	ENTRY_WIDTH = 0.4
	ENTRY_Xpos = 0.55

	# X feature
	label_x = tk.Label(frame1, text="X dimension:", fg="white", bg=LABEL_BG_COLOR, font=FONT, justify="center")
	label_x.place(relx=Xpos, rely=Ypos)
	entry_x = tk.Entry(frame1, bg=ENTRY_BG_COLOR, font=FONT, justify="center")
	entry_x.place(relx=ENTRY_Xpos, rely=Ypos, relwidth=ENTRY_WIDTH)

	# Y feature
	label_y = tk.Label(frame1, text="Y dimension:", fg="white", bg=LABEL_BG_COLOR, font=FONT, justify="center")
	label_y.place(relx=Xpos, rely=Ypos + 0.10)
	entry_y = tk.Entry(frame1, bg=ENTRY_BG_COLOR, font=FONT, justify="center")
	entry_y.place(relx=ENTRY_Xpos, rely=Ypos + 0.10, relwidth=ENTRY_WIDTH)

	# Z feature
	label_z = tk.Label(frame1, text="Z dimension:", fg="white", bg=LABEL_BG_COLOR, font=FONT, justify="center")
	label_z.place(relx=Xpos, rely=Ypos + 0.20)
	entry_z = tk.Entry(frame1, bg=ENTRY_BG_COLOR, font=FONT, justify="center")
	entry_z.place(relx=ENTRY_Xpos, rely=Ypos + 0.20, relwidth=ENTRY_WIDTH)

	# depth feature
	label_depth = tk.Label(frame1, text="Depth:", fg="white", bg=LABEL_BG_COLOR, font=FONT, justify="center")
	label_depth.place(relx=Xpos, rely=Ypos + 0.30)
	entry_depth = tk.Entry(frame1, bg=ENTRY_BG_COLOR, font=FONT, justify="center")
	entry_depth.place(relx=ENTRY_Xpos, rely=Ypos + 0.30, relwidth=ENTRY_WIDTH)

	# table feature
	label_table = tk.Label(frame1, text="Table:", fg="white", bg=LABEL_BG_COLOR, font=FONT, justify="center")
	label_table.place(relx=Xpos, rely=Ypos + 0.40)
	entry_table = tk.Entry(frame1, bg=ENTRY_BG_COLOR, font=FONT, justify="center")
	entry_table.place(relx=ENTRY_Xpos, rely=Ypos + 0.40, relwidth=ENTRY_WIDTH)

	# carat feature
	label_carat = tk.Label(frame1, text="Carat:", fg="white", bg=LABEL_BG_COLOR, font=FONT, justify="center")
	label_carat.place(relx=Xpos, rely=Ypos + 0.50)
	entry_carat = tk.Entry(frame1, bg=ENTRY_BG_COLOR, font=FONT, justify="center")
	entry_carat.place(relx=ENTRY_Xpos, rely=Ypos + 0.50, relwidth=ENTRY_WIDTH)

	# cut feature
	label_cut = tk.Label(frame1, text="Cut:", fg="white", bg=LABEL_BG_COLOR, font=FONT, justify="center")
	label_cut.place(relx=Xpos, rely=Ypos + 0.60)
	cut_var = tk.StringVar()
	drop_cut = tk.OptionMenu(frame1, cut_var, *CUT_LIST)
	drop_cut.place(relx=ENTRY_Xpos, rely=Ypos + 0.60, relwidth=ENTRY_WIDTH)

	# color feature
	label_color = tk.Label(frame1, text="Color:", fg="white", bg=LABEL_BG_COLOR, font=FONT, justify="center")
	label_color.place(relx=Xpos, rely=Ypos + 0.70)
	color_var = tk.StringVar()
	drop_color = tk.OptionMenu(frame1, color_var, *COLOR_LIST)
	drop_color.place(relx=ENTRY_Xpos, rely=Ypos + 0.70, relwidth=ENTRY_WIDTH)

	# clarity feature
	label_clarity = tk.Label(frame1, text="Clarity:", fg="white", bg=LABEL_BG_COLOR, font=FONT, justify="center")
	label_clarity.place(relx=Xpos, rely=Ypos + 0.80)
	clarity_var = tk.StringVar()
	drop_clarity = tk.OptionMenu(frame1, clarity_var, *CLARITY_LIST)
	drop_clarity.place(relx=ENTRY_Xpos, rely=Ypos + 0.80, relwidth=ENTRY_WIDTH)

	# Calculate price button
	btn_price = tk.Button(frame2, text="Calculate price", bg="gray", fg="white",
						  command=lambda: get_values(entry_x.get(), entry_y.get(), entry_z.get(), entry_depth.get(),
													 entry_table.get(), entry_carat.get(), cut_var.get(),
													 color_var.get(), clarity_var.get(), model))

	btn_price.place(relx=0.20, rely=0.15)

	# Predicted price label
	global price_var
	price_var = tk.StringVar()
	price_var.set("Predicted Price")
	label_price = tk.Label(frame2, textvariable=price_var, bg="black", fg="white", font="Modern 16", anchor="center")
	label_price.place(relx=0.15, rely=0.5, relwidth=0.75)

	root.mainloop()
