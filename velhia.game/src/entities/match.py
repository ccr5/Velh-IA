class Match:
    """
    Match Class
    :param obj: `IMatch` Match object saved in MongoDB
    """

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
