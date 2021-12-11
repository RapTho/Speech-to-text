const fs = require("fs");
const SpeechToTextV1 = require("ibm-watson/speech-to-text/v1");
const { IamAuthenticator } = require("ibm-watson/auth");
const dotenv = require("dotenv");

dotenv.config({
  debug: false,
  path: "./src/config.env",
});

const speechToText = new SpeechToTextV1({
  authenticator: new IamAuthenticator({
    apikey: process.env.APIKEY,
  }),
  serviceUrl: process.env.URL,
});

const recognizeParams = {
  audio: fs.createReadStream(process.env.PATH_TO_FILE),
  contentType: process.env.AUDIO_FORMAT,
  wordAlternativesThreshold: 0.9,
};

speechToText
  .recognize(recognizeParams)
  .then((speechRecognitionResults) => {
    if (speechRecognitionResults.result.results[0].final) {
      let transcription =
        speechRecognitionResults.result.results[0].alternatives[0].transcript;
      fs.writeFileSync("src/transcript.txt", transcription);
      console.log(`Transcription:\n${transcription}`);
    } else {
      throw new Error("No final transcription found");
    }
  })
  .catch((err) => {
    console.error("error: ", err);
  });
