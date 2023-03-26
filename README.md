# **Dorothy AI**

The goal of this project is to create a machine learning model that can accurately predict the likelihood and intensity of tornadic activity, based on the real-time data collected predominantly during storm chases, including but not limited to, chases I physically am present for and participate in.

## **Installation**

To use Dorothy AI, you will need to have Python and Julia installed on your system. You can install the required Python packages using pip:

```
pip install -r requirements.txt
```

You can install the required Julia packages using the Julia package manager:

```
import Pkg
Pkg.activate(".")
Pkg.instantiate()
```


## **Usage**

To run this project, you can follow these steps:

1. Clone the repository:
```
git clone https://github.com/your_username/dorothy-ai.git
```
2. Open the project in Google Colab.

3. Follow the instructions in the notebook to train and test the machine learning model on the provided data.

Alternatively, you can download the project as a ZIP file and run the notebooks locally on your machine using Jupyter Notebook or JupyterLab.

Note: Using Google Colab provides the advantage of free access to GPUs, which can significantly speed up the training process.


## **Data Collection**

To collect data for the project, you will need real-world weather data as well as data collected in the field during recent storm chases. The data collected will include information such as tornado location, size, wind speed, and direction. Weather data utilized will specifically include atmospheric conditions such as temperature, pressure fluctuation, humidity, wind direction + speed, precipitation levels + patterns, lightning activity, radar data (such as reflectivity and velocity) as well as satellite imagery.

Transfer Learning will be explored and leveraged when and if the need arises due to gaps or inefficiencies in data.


## **Preprocessing**

Once you have collected the data, you will need to preprocess it before feeding it into the machine learning models. This may include cleaning the data, transforming it into a usable format, and splitting it into training and testing sets.


## **Machine Learning**

You can use both Python and Julia to build and train the machine learning models. This project includes examples of various machine and deep learning techniques such as regression, classification, and clustering.

For supervised learning, we plan to explore classification algorithms such as Random Forest, Support Vector Machines, and Convolutional Neural Networks. Unsupervised learning techniques like K-means clustering and Principal Component Analysis will also be employed to extract patterns and insights from the data. In addition, we will also be using time series analysis and anomaly detection methods to identify any unusual or abnormal patterns.


## **Evaluation**

After training the models, you can evaluate their performance using metrics such as accuracy, precision, and recall. You can also use visualization tools to analyze the results and gain insights into the data.


## **Contributing**

This project is open to contributions from anyone interested in machine learning, atmospheric sciences, or storm chasing. To contribute, please fork the repository and submit a pull request with your changes.


## **License**

This project is licensed under the MIT License - see the <a href="https://github.com/erosmarcello/dorothy-ai/blob/main/LICENSE.md">LICENSE.md</a> file for details.


