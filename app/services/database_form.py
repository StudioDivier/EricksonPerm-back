from ..models import Offers


def add_offer_to_db(name:str, email: str, form:str):
    """
    Функция добавления записи из формы в БД
    :param name: имя польлзователя
    :param email: почта заявителя
    :param form: название или нахождение формы
    :return: True
    """
    try:
        offer = Offers()
        offer.name = name
        offer.email = email
        offer.form = form
        offer.save()
        return True

    except BaseException:
        return False
