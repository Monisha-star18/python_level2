class ErrorClass (Exception):
    pass

class FileNotFound(ErrorClass) :

    def __init__(self):
        self.message = "The path is wrong or the file is not exists"
        super().__init__(self.message)

class DataNotFoundError(ErrorClass) :
     def __init__(self):
            self.message = "data Not found"
            super().__init__(self.message)
