import datetime

from django.urls import register_converter


class DateConverter:
    regex = r'([0][1-9]|[1-2][0-9]|[3][0-1])-([1][0-2]|[0][1-9])-(\d{4})'

    def to_python(self, value: str):
        valid_date = datetime.datetime.strptime(value, '%d-%M-%Y').date()
        if valid_date.year > 2100:
            raise ValueError()
        return valid_date

    def to_url(self, value: str):
        return str(value)


def register_all_ls4_converters():
    register_converter(DateConverter, 'date')
