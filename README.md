Create env:
``create env -n mlops python==3.7 -y
``

Activate env:
``conda activate mlops
``

Create requirements file - 
install requirements file

`` pip install -r requirements.txt
``

Download dataset from here:

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5

Install dvc :
`` pip install dvc
``

Initializing git:
``git init
``

Initializing dvc:
``dvc init
``


Add version control to the dataset folder.

`` dvc add data_given\winequality.csv
``




