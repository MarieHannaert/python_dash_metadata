# python_dash_metadata
This is a tool to make it easier for researchers to save their metadata. Since it will be an interactive web interface and not a command line, because they are scared of that.

To use this metadata tool: 

## Installing conda 
Look at the conda documentation for installing this. [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
You will also need Biconda. [Bioconda](https://bioconda.github.io/)

## Installing the tool
````
$ git clone https://github.com/MarieHannaert/python_dash_metadata.git
````
## Running the tool
There is a small preparing step to get the enviroment that you need
### Installing the enviroment
````
conda env create -f meta_python_dash.yaml
````
### Activating the enviroment
````
conda activate meta_python_dash
````
### running the app
this is the step that will affective launch the metadatatool: 
````
$ cd python_dash_metadata
$ python app.py
````

normally now you can select something like: *http://127.0.0.1:8050/* in your terminal, paste this in your webbrowser, and then fill in the form and save and the metadata file will appear in the python dash directory