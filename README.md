# Speech-to-text

Speech-to-text transcription of a local audio file using IBM Watson Speech-to-Text. So far only synchronous transcription requests are implemented.

### Prerequisites

- Install [Python](https://www.python.org/downloads/)
- Create an IBM Cloud account and a **free** [speech-to-text service](https://cloud.ibm.com/catalog/services/speech-to-text)
- Copy the newly generated **API key** into the [config.env](src/config.env) file
- Choose the correct [service endpoint](https://cloud.ibm.com/apidocs/speech-to-text?code=node#service-endpoint) of your instance and add this to the [config.env](src/config.env) file

### How to use

Clone the github repository and change into the local repo

```
git clone https://github.com/RapTho/speech-to-text.git
cd speech-to-text
```

Install the python dependencies

```
pip3 install -r requirements.txt
```

Then start the transcription, wait until it's done and check the stdout or [transcript.txt](src/output/transcript.txt)

```
python3 src/main.py
```

You may replace the audio file in [src/input](src/input) and if necessary also the AUDIO_FORMAT in the [config.env](src/config.env) file.

### Change language

Change the **language** by modifying the LANGUAGE key in the [config.env](src/config.env). Choose one of the existing [language models](https://cloud.ibm.com/apidocs/speech-to-text?code=python#getmodel)

### Adjust background noise suppression

Change the BACKGROUND_SUPPRESSION key in the [config.env](src/config.env). Choose a value between 0.0 and 1 where 0 means no suppression and 1 is the maximum.

### Run containerized

Build the container. All commands I run using podman work with docker also.

```
podman build -t speech-to-text:latest .
```

```
podman run -v ${PWD}/src/output/:/app/src/output/ speech-to-text:latest
```
