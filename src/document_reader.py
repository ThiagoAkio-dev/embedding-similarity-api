class DocumentReader:

    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def read_text(self) -> str:
        with open (self.file_path, "r", encoding="utf-8") as file:
            text = file.read().strip()

            if not text:
                raise ValueError("The document is empty")
            
            return text