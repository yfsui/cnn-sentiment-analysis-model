# CNN Sentiment Analysis Model
## End-to-end Training and Deployment on the AWS

***raw-data.zip***: unprocessed data, split into three subsets

Link to the raw dataset on the S3: https://aiops-2020-public.s3.us-east-2.amazonaws.com/training.full.csv

* `train.csv`
* `dev.csv`
* `eval.csv`

<br>

***lambda-function***
* `my_lambda_pre_processor.py`: lambda function
* pre_processing: Python library for preprocessing
    - `word_embedding.py`: load embedding dictionary
    - `text_processing.py`: clean and tokenize text
    - `pre_processing.py`: pre-process tweets
    - `nltk_tokenize.py`: nltk tokenizer library
    - resources
      - `glove.txt`: embedding dictionary (without vector)
      
<br>

***aws-glue-job***
* `glue_preprocessing_job_script.py`: script for Glue ETL job
* `glue-job-output`: processed data
    * `train.json`
    * `dev.json`
    * `eval.json`

<br>

***sagemaker_jupyter_code.ipynb***: jupyter notebook used to train model on the SageMaker

<br>

***model_training***
* `sentiment_dataset.py`: load datasets
* `training_config.json`: store the value of model parameters
* `sentiment_model_cnn.py`: define the CNN model
* `sentiment_training.py`: pass in arguments and train the model

<br>

***model-saved***: the final version of the trained model

<br>


Link to the GloVe dictionary (25d) on the S3: https://e4577-cloud.s3.amazonaws.com/dictionary/glove.txt 

Link to the GloVe dictionary (50d) on the S3: https://e4577-cloud.s3.amazonaws.com/dictionary/glove.50d.txt 

Link to the GloVe dictionary (200d) on the S3: https://e4577-cloud.s3.amazonaws.com/dictionary/glove.200d.txt 

<br>

### Reference

Under the instruction of Professor Pierre-Hadrien Arnoux @ Columbia University

Twitter GloVe embedding dictionary from https://github.com/stanfordnlp/GloVe
