from enum import Enum


class EditMessagesFilesFileType(str, Enum):
    FILE = "file"
    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
