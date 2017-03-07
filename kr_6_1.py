class Student(object):

    def __init__(self, name, conf):

        self.name = name
        self.conf = conf
        self.labs = [0] * conf.get('lab_num')

    def set_lab(self, score, number = 0):

        if number > (len(self.labs) - 1):

            return 'error'

        if score > self.conf.get('lab_max'):

            score = self.conf.get('lab_max')

        if self.labs[0] != 0 and number == 0:

            self.labs[self.labs.index(0)] = score

        elif 0 not in self.labs:

            return 'error'

        else:
            if self.labs[number] != 0 and self.labs[number] != score:
                pass
            else:
                self.labs[number] = score

    def average_score(self):

        return round(sum(self.labs) / len(self.labs), 1)