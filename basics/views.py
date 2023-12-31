from django.shortcuts import render

# Create your views here.
def index(request):
  if(request.method=="POST"):
    data = request.POST
    Area = data.get('textarea')
    Majoraxislength = data.get('textmajoraxislength')
    Minoraxislength = data.get('textminoraxislength')
    Eccentricity = data.get('texteccentricity')
    ConvexArea = data.get('textconvexarea')
    EquivDiameter = data.get('textequivdiameter')
    Extent = data.get('textextent')
    Perimeter = data.get('textperimeter')
    Roundness = data.get('textroundness')
    AspectRation = data.get('textaspectration')
    if ('buttonpredict' in request.POST):
      import pandas as pd
      path ="C:\\Users\\Harshitha\\OneDrive\\Desktop\\PROJECT-ML\\33_ricetypeclassification\\riceClassification.csv"
      data = pd.read_csv(path)

      inputs = data.drop(['id','Class'],axis=1)
      outputs = data['Class']

      import sklearn
      from sklearn.model_selection import train_test_split
      x_train,x_test,y_train,y_test = train_test_split(inputs,outputs,train_size=0.8)

      from sklearn.ensemble import RandomForestClassifier
      model = RandomForestClassifier(n_estimators=100)
      model.fit(x_train,y_train)
      y_pred = model.predict(x_test)

      result = model.predict([[int(Area),float(Majoraxislength),float(Minoraxislength),float(Eccentricity),int(ConvexArea),float(EquivDiameter),float(Extent),float(Perimeter),float(Roundness),float(AspectRation)]])
    return render(request,'index.html',context={'result':result})
  return render(request,'index.html')
