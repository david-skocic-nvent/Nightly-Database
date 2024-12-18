class Tee:
    def __init__(self, *streams):
        self.streams = streams
    
    def write(self, message):
        for stream in self.streams:
            stream.write(message)
    
    def flush(self):
        for stream in self.streams:
            stream.flush()