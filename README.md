# paperday
Manage your every research papers with paperday, A powerfull tool to visualize user written research paper with AI.

## Environment Setup
**Library Requirements**
  * flask
  * numpy
  * scikit-image
  * image-quality
  * pymupdf
  
 **Code Configuration**
 
    git clone https://shah-codex/paperday.git
    cd paperday
    
The ```app.py``` is the entry point to the project. Running it will run the server on ```localhost:5000```.

    paperday
        \
         +----> app.py      [ Main entry point server for flask api. ]
         +----> models/     [ The ML algorithm files. ]
         +----> templates/  [ All UI view files html. ]
         +----> {keys/}     [ API key a folder need to be created. ]

Create the keys module and initialize the ```API_KEY``` and ```header``` containing the API link and header token for calling the third-party API.

    mkdir keys && touch keys/keys.py

The ```keys.py``` file will have the content as below.

    API_URL = "https://api-inference.huggingface.co/models/mrm8488/xlm-roberta-base-finetuned-HC3-mix"
    headers = {"Authorization": f"Bearer {'YOUR_TOKEN_HERE'}"}


## Run

    cd paperday
    python3 app.py
    
    visit http://localhost:5000/ in your browser
    
![image](https://user-images.githubusercontent.com/66596874/222943212-77c8a94e-2c26-4345-a7ba-0fd35a8d502a.png)

![image](https://user-images.githubusercontent.com/66596874/222943269-19de5e8e-ef2b-4ee1-8a52-5fdfa0f6bab8.png)

![image](https://user-images.githubusercontent.com/66596874/222951141-beeaa6b9-f0b9-4d8f-bbb2-50db8ca401e0.png)


