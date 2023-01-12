from django.shortcuts import render
from django.http import HttpResponse
import pickle
from keras.models import Model,load_model
from keras_preprocessing.sequence import pad_sequences
from .models import Prediction2

with open('tokenizer3.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = load_model('LSTMdev')

# Create your views here.
def predict(request):
    if request.method != "POST":
        return render(request,"index.html",{"text": ""})
    else:
        text = request.POST["name"]
        sequences = tokenizer.texts_to_sequences([text])
        sequences_matrix = pad_sequences(sequences,maxlen=120,padding='post')
        prediction = model.predict(sequences_matrix)[0][0]
        if prediction > 0.5:
            class_ = 1
        else:
            class_ = 0
        if class_ == 1:
            confidance = prediction *100

        else:
            confidance = 0.5 - prediction
            confidance = (1 - confidance) * 100
        pred = Prediction2(text=text,Predicted_Class = class_,confidance_score = format(confidance, '.2f'))
        pred.save()
        return render(request,"index.html",{"text": f"Predicted Class :{class_},with {format(confidance, '.2f')}% Confidance."})