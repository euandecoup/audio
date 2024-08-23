import whisper

model = whisper.load_model("base")
result = model.transcribe("recording1.wav")

with open("transcription.txt", "w") as f:
    f.write(result["text"])