# Diamonds_Appraisal

## :boom: Diamonds's price assessment GUI

This project's idea came from a private kaggle competition. The main goal was to create the best machine learning model at predicting diamond's prices. 

## :computer: **Technology stack**
Wrote in python 3. Main modules:

**Scikit-Learn** -> Model training and prediction, RandomForestRegressor(n_estimators=512, max_depth=16)

**Tkinter** -> Graphical User Interface (GUI)

## :wrench: **Configuration**
Install python and mandatory modules

You can use the following code if you are using the anaconda distribution.

```
conda create -n new_env_name_here
conda activate new_env_name_here
conda install python=3.7
pip install -r requirements.txt
```

*Note:* Each environment manager has its own installation method. It's strongly recommended to check its documentation.

## :snake: **Running the GUI**
This GUI comes with a pre-trained model saved as a binary file. Nevertheless, this GUI can run any other model that was trained using the diamonds data set found in the data folder.

### Running GUI using pre-installed model 
Navigate to where the rep was downloaded and type `python main.py` in your terminal. This will run the main.py script which automatically opens the GUI and loads the pre-installed Random Forest model.

### Running GUI using another model
Any model trained using the diamonds data set can be used to run the GUI. Custom models should be placed in the following path Diamonds_Appraisal/data/model_binary/my_custom_model.pkl

Once there, go to your terminal and run the following line of code: `python main.py my_custom_model.pkl`

![](images/gui1.png) ![](images/gui2.png)

### Predicting diamond's price 
Prices are calculated using all 9 entries at the left part of the window. All entries should be filled. First 6 entries can only take float or integer values, while the last 3 are drop-down lists.

Once all entries are filled, click on the "Calculate price" button to update the "Predicted Price" label.

## :information_source: **Data set info**

![](images/diamond.jpg)

Comprised by almost 54.000 registries. Data set features are the following:

**price** price in US dollars (min: $326 - max: $18,823)

**carat** weight of the diamond (min: 0.2 - max: 5.01)

**cut** quality of the cut (Fair (lowest), Good, Very Good, Premium, Ideal (highest))

**color** diamond colour, from J (worst) to D (best)

**clarity** a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))

**x** length in mm (min: 0 - max: 10.74)

**y** width in mm (min: 0 - max: 58.9)

**z** depth in mm (min: 0 - max: 31.8)

**depth** total depth percentage = z / mean(x, y) = 2 * z / (x + y) (min: 43 - max: 79)

**table** width of top of diamond relative to widest point (min: 43 - max: 95)

## :file_folder: **Folder structure**
```
└── Diamonds_Appraisal
    ├── .gitignore
    ├── requirements.txt
    ├── README.md
    ├── main.py
    ├── notebooks
    │   └── Pipeline.ipynb
    ├── packages
    │   ├── GUI
    │   │   └── GUI.py
    │   └── Model
    │   │   └── model.py
    └── data
        ├── raw
        │   ├── diamonds.csv
        │   ├── diamonds_test.csv
        │   └── diamonds_train.csv
        └── model_binary
            └── RandomForest.pkl
```

## :interrobang: **Custom models**
Check the Pipeline.ipynb notebook or the model.py script to get a broad idea. These two files have all necessary steps to create, test, enhance and save your modules.

## :love_letter: **Contact info**
Any doubt? Advice?  Drop me a line! :smirk:
