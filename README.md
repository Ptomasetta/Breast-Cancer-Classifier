# Breast-Cancer-Classifier


Classifier of cancerous breast tumors using cell data from the Breast Cancer Wisconsin (Diagnostic) Data Set

[Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)

![](https://github.com/Ptomasetta/Breast-Cancer-Classifier/blob/master/Interface.jpg?raw=true)

## -Instructions to Run

- Open one terminal window and navigate to Cancer-Classifier-App/ui
  - Install yarn
         
        $ yarn install
  - Install serve
  
        $ npm install -g serve
  - Build application
  
        $ npm run build
  - Run the UI on port 3000

        $ serve -s build -l 3000
- Open a second terminal window and navigate to Cancer-Classifier-App/service
  - Create a virtual environment
        
        $ python3 -m venv env
  - Enter virtual environment
        
        $ source env/bin/activate
  - Install dependencies in virtual environment
        
        $ pip install -r requirements.txt
  - Run Flask application
        
        $ FLASK_APP=diagnose_app.py flask run
- Running on: http://localhost:3000  