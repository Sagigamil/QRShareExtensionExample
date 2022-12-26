from qrshare.ViewInterface import ViewInterface

class ConsoleView(ViewInterface):
    def __init__(self, color='black'):
        self._color = color

    @staticmethod
    def validate_init_params(**params):
        if len(params.keys()) > 0:
            raise ValueError("not expect params, but params were given")

    def view(self, str):
        print(str)