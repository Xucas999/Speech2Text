from threading import Thread
import main,AudioIn as ain,SpeechRecognition as sr

def startRecording():
    main.logger.info("Recording...")
    record = Thread(target=ain.record_microphone)
    record.start()

    transcribe = Thread(target=sr.speech_recognition,args=(output,))
    transcribe.start()

def stopRecording():
    main.logger.info("Stopped Recording...")
    main.messages.get()


rec = False
while True:
    inp = input()
    rec = (rec==False)
    if rec:
        startRecording()
    else:
        stopRecording()