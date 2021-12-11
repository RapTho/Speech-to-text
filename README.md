# Speech-to-text

Speech-to-text transcription of a local audio file using IBM Watson Speech-to-Text. So far only synchronous transcription requests are implemented.

### Prerequisites

- Install [Node.js](https://nodejs.org/en/download/)
- Create an IBM Cloud account and a **free** [speech-to-text service](https://cloud.ibm.com/catalog/services/speech-to-text)
- Copy the newly generated API key into the [config.env](src/config.env) file
- Choose the correct [service endpoint](https://cloud.ibm.com/apidocs/speech-to-text?code=node#service-endpoint) of your instance and add this to the [config.env](src/config.env) file

### How to use

Clone the github repository and change into the local repo

```
git clone https://github.com/RapTho/speech-to-text.git
cd speech-to-text
```

Install the node dependencies

```
npm install
```

Enter the full path to the audio file in the [config.env](src/config.env) and modify the AUDIO_FORMAT if needed. Find the list of supported audio formats [here](https://cloud.ibm.com/apidocs/speech-to-text?code=node#recognize).

Then start the transcription, wait until it's done and check the stdout or [transcript.txt](src/transcript.txt)

```
npm start
```
