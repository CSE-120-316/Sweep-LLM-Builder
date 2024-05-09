# Chat-Cats

## About

There is a demand for companies to create their
own internal tools by utilizing Large Language
Models (LLMs), but current solutions would require
for companies to send private data to companies
like Open-AI; this is not a practical solution due to
high costs and security risks. Alternatively, a
company can attempt to train their own model in a
technically demanding process that requires
skilled labor. Sweep, a Merced-based software
company, seeks a solution.

## Deployment

> This application has high system requirements and requires a Nvidia GPU. If you'd like to deploy this on a device without a Nvidia GPU, open docker-compose.yaml and comment out the indicated code. The application will run, but fine-tuning will never progress.

This application makes use of Docker. To deploy the application,
make sure Docker Engine is installed and running. From the root of the folder run this command:

`docker build -t chat-cats-base -f dockerfile.chat-cats-base .`

This only needs to be run once, as it is used to create the base for the main docker container.

Now, anytime you need to deploy the application just run:

`docker compose up`

This will start the application and you can access it at `localhost:6360`

If you make any changes to the code, run this command:

`docker compose up --build`

## Demo

Our demo front-end application only works with Sweep's server, which is only open for I2G.

We have provided an alternate demo. There is a Python notebook in `demo/Demo.ipynb`. To use it, make sure requests is available in the notebook's Python environment with `pip install requests`.

Make sure to change the host variable in the first code block to match with the host of the deployed Docker container.

## Endpoints

Here is a list of each endpoint and what it accepts:


### Endpoints:

#### 1. Upload Training Data

- **URL:** `/trainingDataUpload`
- **Method:** POST
- **Description:** This endpoint receives training data for the Language Learning Model (LLM) and saves it.
- **Parameters:**
  - `data_name`: Name of the dataset (form field)
  - `dataset`: JSON file containing the training data (form field)
- **Response:**
  - `dataSet`: Name of the dataset
  - `message`: Confirmation message

#### 2. Create ChatBot

- **URL:** `/createChatBot`
- **Method:** POST
- **Description:** Creates a new ChatBot with the specified name and learning rate.
- **Parameters:**
  - `name`: Name of the ChatBot (form field)
  - `lr`: Learning rate (form field)
- **Response:**
  - `ChatBot`: Information about the created ChatBot
  - `message`: Confirmation message

#### 3. Train ChatBot

- **URL:** `/trainChatBot`
- **Method:** POST
- **Description:** Begins training the specified ChatBot with the provided dataset.
- **Parameters:**
  - `name`: Name of the ChatBot (form field)
  - `data_name`: Name of the dataset for training (form field)
- **Response:**
  - `ChatBot`: Information about the ChatBot after training
  - `message`: Training status message

#### 4. Message ChatBot

- **URL:** `/messageChatBot`
- **Method:** POST
- **Description:** Sends a message to the specified ChatBot.
- **Parameters:**
  - `name`: Name of the ChatBot (form field)
  - `message`: Message to send to the ChatBot (form field)
- **Response:**
  - `ChatBot`: Information about the ChatBot
  - `message`: Response from the ChatBot

#### 5. Check Status

- **URL:** `/checkStatus`
- **Method:** GET
- **Description:** Checks the status of the specified ChatBot.
- **Parameters:**
  - `name`: Name of the ChatBot (query parameter)
- **Response:** Information about the status of the ChatBot

#### 6. List ChatBots

- **URL:** `/listChatBots`
- **Method:** GET
- **Description:** Lists all ChatBots based on their status.
- **Parameters:**
  - `status`: Filter by status (`Untrained`, `Training`, `Trained`, `All`) (query parameter)
- **Response:** List of ChatBots matching the specified status

#### 7. List Datasets

- **URL:** `/listDatasets`
- **Method:** GET
- **Description:** Lists all available datasets.
- **Response:** List of datasets

#### 8. Ping

- **URL:** `/ping`
- **Method:** GET
- **Description:** Checks the status of the server.
- **Response:** "pong"

#### 9. Delete ChatBot

- **URL:** `/deleteChatBot`
- **Method:** POST
- **Description:** Deletes the specified ChatBot.
- **Parameters:**
  - `name`: Name of the ChatBot to delete (form field)
- **Response:** Confirmation message

#### 10. Delete Dataset

- **URL:** `/deleteDataset`
- **Method:** POST
- **Description:** Deletes the specified dataset.
- **Parameters:**
  - `data_name`: Name of the dataset to delete (form field)
- **Response:** Confirmation message

#### 11. Delete Everything

- **URL:** `/deleteEverything`
- **Method:** POST
- **Description:** Deletes all ChatBots and datasets.
- **Response:** Confirmation message
