


class sus():

    def __init__(self):
        self.__currency_name = str()
        self.__currency_value = float()

    def check_if_admin(self, admins, id):
        a = False
        for i in admins:
            if id == i:
                a = True
                break
            else:
                a = False
        return a

    def chart(self, mc, *args):
        pass


