from App.app import DB


class TokenModel(DB.Model):

    id = DB.Column(DB.Integer, primary_key = True)
    token = DB.Column(DB.String(255))

    def __repr__(self) -> str:
        return "<Token %r>"%self.token
