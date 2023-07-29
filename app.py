import whisper
import logging
import ffmpeg
logging.basicConfig(
    filename="newfile.log", format="%(asctime)s %(message)s", filemode="w"
)

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages

model = whisper.load_model("base")
result = model.transcribe("./sample-1.mp3")
print(result["text"])

logger.info(result['text'])