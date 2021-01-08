class Match:

    def __init__(self, obj):
        self.id = obj['_id'] if '_id' in obj else obj['id']
        self.begin = obj['begin']
        self.end = obj['end'] if 'end' in obj else ''
        self.time = obj['time']
        self.sa = obj['sa']
        self.mas = obj['mas']
        self.plays = obj['plays']
        self.status = obj['status']
        self.winner = obj['winner'] if 'winner' in obj else ''

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
