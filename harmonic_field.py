from notes import Notes 

class HarmonicField():

    def __init__(self, tonic):
        self.tonic = tonic
    
    """ Generates the Major Harmonic Field of the given tonic
        and returns a 7-tuple containing the chords """
    def major(self):
        