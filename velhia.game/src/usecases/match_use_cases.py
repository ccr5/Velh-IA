from src.entities.match import Match


class MatchUseCase(Match):
    """ Agent Use Case Class """

    def create_object(self):
        """
        Create a full obj to use in database functions
        """

        match_info = {"_id": self.id,
                      "begin": self.begin,
                      "time": self.time,
                      "sa": self.sa,
                      "mas": self.mas,
                      "plays": self.plays,
                      "status": self.status}

        if self.end != '':
            match_info['end'] = self.end

        if self.winner != '':
            match_info['winner'] = self.winner

        return match_info
