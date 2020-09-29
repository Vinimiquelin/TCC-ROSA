Como utilizar o ROSA 0.3.0:

Na pasta "Face_classifier_construction":

- Copiar a pasta "data" para "TCC-ROSA"
- Copiar o classificador "haarcascade_frontalface_default" para "TCC-ROSA"
- Alimentar a pasta "data" rodando o o arquivo "collect_training_data.py"
- Excecutar o "classifier.py" para gerar o "classifier.xml"

Na pasta "Chabot_cosntruction":

- Copiar o "intents.json" para "TCC-ROSA"
- Excecutar o "neural_network_construction" para gerar os arquivos do modelo do chatbot que são:
	* "model.tflearn.data-00000-of-00001"
	* "model.tflearn.index"
	* "model.tflearn.meta"
	* "data.pickle"
	* "checkpoint"

Na pasta "ROSA_prototype":

- Excecutar o "0.3.0_ROSA_prototype.py" para rodar o projeto do robô ROSA
