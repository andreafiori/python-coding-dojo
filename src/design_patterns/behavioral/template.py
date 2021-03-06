"""
An example of the Template pattern in Python

Defines the skeleton of a base algorithm, deferring definition of exact
steps to subclasses.
"""

class Template(object):
    @staticmethod
    def get_text():
        return "plain-text"

    @staticmethod
    def get_pdf():
        return "pdf"

    @staticmethod
    def get_csv():
        return "csv"

    @staticmethod
    def convert_to_text(data):
        # print("[CONVERT]")
        return "{} as text".format(data)

    @staticmethod
    def saver():
        return "[SAVE]"

    @staticmethod
    def template_function(getter, converter=False, to_save=False):
        data = getter()
        # print("Got `{}`".format(data)

        if len(data) <= 3 and converter:
            data = Template.converter(data)
        else:
            print("Skip conversion")

        if to_save:
            Template.saver()

        return "`{}` was processed".format(data)


"""
>>> template_function(get_text, to_save=True)
Got `plain-text`
Skip conversion
[SAVE]
`plain-text` was processed

>>> template_function(get_pdf, converter=convert_to_text)
Got `pdf`
[CONVERT]
`pdf as text` was processed

>>> template_function(get_csv, to_save=True)
Got `csv`
Skip conversion
[SAVE]
`csv` was processed
"""
