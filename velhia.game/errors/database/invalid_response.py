class InvalidResponse(Exception):
    """ raised when receive a invalid http code response """

    def __init__(self, response, expect):
        self.response = response
        self.expect = expect
        self.message = f"http code response isn't {response}"

    def __str__(self):
        return f"response code = {self.response} -> {self.messages}"
