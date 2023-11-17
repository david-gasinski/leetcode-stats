from utils.fetch import fetchData, endpoint

class User:
    def __init__(self, username):
        self.username = username
        self.fetchData()

    def fetchData(self):
        rejected_attr = ['status', 'retrieved', 'reputation', 'contributionPoints']
        data = fetchData(endpoint(self.username))

        # map data to object, ignoring rejected attributes  
        for v in data.items():
            if v[0] not in rejected_attr:
                setattr(self, v[0], v[1])

        # stops DivisionByZero error.
        if (data['status'] == 'error'):
            self.username = "User not found"
            self.solvedDeg = 0.1
        else:
            self.solvedDeg = (self.totalSolved / self.totalQuestions) * 360
