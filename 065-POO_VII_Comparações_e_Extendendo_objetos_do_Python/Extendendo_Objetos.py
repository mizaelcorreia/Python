class Accounts(list):
    def sorting1(self):
        copy = self.copy()
        self.clear()
        while len(self) < len(copy):
            min_id = copy[0]
            for account in copy:
                if account.id < min_id.id:
                    min_id = account
            self.append(min_id)
            copy.remove(min_id)

    def sorting2(self):
        copy = self.copy()
        self.clear()
        copy = sorted(copy, key=lambda x: x.id)
        for v in copy:
            self.append(v)


class Bank:
    def __init__(self):
        self.accounts = Accounts()


class Account:
    def __init__(self, ID, balance):
        self.id = ID
        self.balance = balance