from notes import Notes 

class HarmonicField():

    def __init__(self, tonic):
        self.tonic = tonic
    
    """ Generates the Major Scale of the given tonic
        and returns a 7-tuple containing the notes """
    def major_natural_scale(self):
        scale = {}
        scale['first_degree'] = self.tonic
        scale['second_degree'] = self.tonic + 2
        scale['third_degree'] = self.tonic + 4
        scale['fourth_degree'] = self.tonic + 5
        scale['fifth_degree'] = self.tonic + 7
        scale['sixth_degree'] = self.tonic + 9
        scale['seventh_degree'] = self.tonic + 11
        return scale
