import whisper
model= whisper.load_model("medium")
out=model.transcribe("your_audio" ,language="lang")
out