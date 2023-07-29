from enum import Enum
import os
import subprocess


class Stt_models(Enum):
    TINY = "TINY"
    BASE = "BASE"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class Stt_lang(Enum):
    English = "English"
    Hindi = "Hindi"


# Accessing enum members
# print(Color.RED)        # Color.RED
# print(Color.RED.value)  # 1


class Speech_to_text:
    """
    Class to convert speech to text
    """

    def __init__(self) -> None:
        pass

    def sample_stt(self, file_loc, mode: Stt_models, language: Stt_lang):
        command = f"whisper {file_loc} --model {mode} --language {language}"
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        print("Output:")
        print(result.stdout)
        print(result.stderr)
