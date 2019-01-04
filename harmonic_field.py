from notes import Notes
import pprint

class HarmonicField():

    def __init__(self, tonic):
        self.tonic = tonic
    
    """ Generates the Major Scale of the given tonic
        and returns a dictionary containing the notes """
    def major_scale(self):
        scale = {}
        scale['first_degree'] = self.tonic.name
        scale['second_degree'] = (self.tonic + 2).name
        scale['third_degree'] = (self.tonic + 4).name
        scale['fourth_degree'] = (self.tonic + 5).name
        scale['fifth_degree'] = (self.tonic + 7).name
        scale['sixth_degree'] = (self.tonic + 9).name
        scale['seventh_degree'] = (self.tonic + 11).name

        print(scale)

        return scale

    """ Generates the Minor Natural Scale of the given tonic
        and returns a dictionary containing the notes """
    def minor_natural_scale(self):
        scale = {}
        scale['first_degree'] = self.tonic.name
        scale['second_degree'] = (self.tonic + 2).name
        scale['third_degree'] = (self.tonic + 3).name
        scale['fourth_degree'] = (self.tonic + 5).name
        scale['fifth_degree'] = (self.tonic + 7).name
        scale['sixth_degree'] = (self.tonic + 8).name
        scale['seventh_degree'] = (self.tonic + 10).name

        print(scale)

        return scale
