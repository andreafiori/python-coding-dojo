"""
Command pattern decouples the object invoking a job from the one who knows
how to do it. As mentioned in the GoF book, a good example is in menu items.
You have a menu that has lots of items. Each item is responsible for doing a
special thing and you want your menu item just call the execute method when
it is pressed. To achieve this you implement a command object with the execute
method for each menu item and pass to it.

*About the example
We have a menu containing two items. Each item accepts a file name, one hides the file
and the other deletes it. Both items have an undo option.
Each item is a MenuItem class that accepts the corresponding command as input and executes
it's execute method when it is pressed.

"""


class HideFileCommand(object):
    """
    A command to hide a file given its name
    """

    def __init__(self):
        # an array of files hidden, to undo them as needed
        self._hidden_files = []

    def execute(self, filename):
        """

        :param filename: string
        :return: string
        """
        self._hidden_files.append(filename)
        return f'hiding {filename}'

    def undo(self):
        filename = self._hidden_files.pop()
        return f'un-hiding {filename}'


class DeleteFileCommand(object):
    """
    A command to delete a file given its name
    """

    def __init__(self):
        # an array of deleted files, to undo them as needed
        self._deleted_files = []

    def execute(self, filename):
        self._deleted_files.append(filename)
        return f'deleting {filename}'

    def undo(self):
        filename = self._deleted_files.pop()
        return f'restoring {filename}'


class MenuItem(object):
    """
    The invoker class. Here it is items in a menu.
    """

    def __init__(self, command):
        """
        Set command object
        :param command: Command
        """
        self._command = command

    def on_do_press(self, filename):
        return self._command.execute(filename)

    def on_undo_press(self):
        return self._command.undo()
