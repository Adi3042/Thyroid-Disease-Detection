from flask import Flask, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    
    else:
        data = CustomData(
            age=int(request.form.get('age')),
            sex=request.form.get('sex'),
            lithium=request.form.get('lithium'),
            goitre=request.form.get('goitre'),
            psych=request.form.get('psych'),
            T3=float(request.form.get('T3')),
            T4U=float(request.form.get('T4U')),
            FTI=float(request.form.get('FTI')),
            tumor=request.form.get('tumor'),
            on_thyroxine=request.form.get('on_thyroxine'),
            hypopituitary=request.form.get('hypopituitary'),
            on_antithyroid_medication=request.form.get('on_antithyroid_medication'),
            thyroid_surgery=request.form.get('thyroid_surgery'),
            I131_treatment=request.form.get('I131_treatment')
        )
        final_new_data = data.get_data_as_dataframe()

        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        
        results = round(pred[0], 2)
        
        return render_template('form.html', final_result=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
