# Breast-Cancer-Classifier
Classifier of cancerous breast tumors using cell data from the Breast Cancer Wisconsin (Diagnostic) Data Set

[Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)

-Instructions to run
    Open one terminal window
        Navigate to Cancer-Classifier-App/ui
            $ yarn install
            $ npm install -g serve
            $ npm run build
            $ serve -s build -l 3000
    Open a second terminal window
        Navigate to Cancer-Classifier-App/service
            $ python3 -m venv env
                Creates virtual environment
            $ source env/bin/activate
                Enters virtual environment
            $ pip install -r requirements.txt
                Installs dependencies in ve
            $ FLASK_APP=diagnose_app.py flask run
                Runs Flask application
