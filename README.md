# Iris-Flower-Data-Classification-by-KNN-and-Navie-Bayes
<h1>Iris Species Classification Web Application</h1>

<h2>Project Overview</h2>
<p>
This is a <b>Flask-based web application</b> that classifies Iris flower species using
<b>K-Nearest Neighbors (KNN)</b> and <b>Naive Bayes</b> machine learning algorithms.
The application provides an interactive dashboard where users can input flower
measurements and get real-time predictions along with model performance metrics.
</p>

<h2>Features</h2>

<h3>Interactive Prediction Interface</h3>
<ul>
    <li>Input fields for four flower measurements</li>
    <li>Toggle between KNN and Naive Bayes models</li>
    <li>Real-time species prediction (Setosa, Versicolor, Virginica)</li>
</ul>

<h3>Model Performance Dashboard</h3>
<ul>
    <li>Accuracy score</li>
    <li>Classification report</li>
    <li>Confusion matrix</li>
    <li>Dynamic display based on selected model</li>
</ul>

<h2>Machine Learning Models</h2>
<ul>
    <li>KNN Classifier (k=3)</li>
    <li>Gaussian Naive Bayes</li>
    <li>Trained on Iris dataset (150 samples)</li>
</ul>

<h2>Dataset Information</h2>

<table>
<tr><th>Feature</th><th>Description</th><th>Range</th></tr>
<tr><td>Sepal Length</td><td>Length of sepal in cm</td><td>4.3 - 7.9</td></tr>
<tr><td>Sepal Width</td><td>Width of sepal in cm</td><td>2.0 - 4.4</td></tr>
<tr><td>Petal Length</td><td>Length of petal in cm</td><td>1.0 - 6.9</td></tr>
<tr><td>Petal Width</td><td>Width of petal in cm</td><td>0.1 - 2.5</td></tr>
</table>

<h2>Target Classes</h2>
<table>
<tr><th>Class</th><th>Label</th><th>Samples</th></tr>
<tr><td>Iris Setosa</td><td>0</td><td>50</td></tr>
<tr><td>Iris Versicolor</td><td>1</td><td>50</td></tr>
<tr><td>Iris Virginica</td><td>2</td><td>50</td></tr>
</table>

<h2>File Structure</h2>
<pre>
iris-classifier/
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
├── KNN.pkl
├── Navis.pkl
├── test_knn.json
└── test_Navia.json
</pre>

<h2>Deployment</h2>
<pre>
web: gunicorn app:app
</pre>

<h2>Local Setup</h2>
<pre>
git clone https://github.com/yourusername/iris-classifier.git
cd iris-classifier
python -m venv venv
pip install -r requirements.txt
python app.py
</pre>

<h2>Future Enhancements</h2>
<ul>
    <li>Add Decision Tree, SVM, Random Forest</li>
    <li>Data visualization</li>
    <li>Batch CSV prediction</li>
    <li>User accounts</li>
</ul>

<h2>Contact</h2>
<p>Email: bandisaiteja2@gmail.com</p>

<p><b>Created by Bandi Saiteja</b></p>
