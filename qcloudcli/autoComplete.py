import sys
import logging
import copy
from . import handleData

LOG = logging.getLogger(__name__)


class Completer(object):

    def __init__(self):
        self.handleData = handleData.handleData()
        self.main_options = ['output', 'SecretId', 'SecretKey', 'RegionId', 'profile']
        self.main_options_version = ['output', 'SecretId', 'SecretKey', 'RegionId', 'profile','Version']
        self.qcloudcli = 'qcloudcli'


    def _complete_option(self, option_name):
        if option_name == '--output':
            cli_data = ['text', 'table', 'json']
            return cli_data
        return []

    def _complete_provider(self):
        retval = []
        if self.current_word.startswith('-'):
            cw = self.current_word.lstrip('-')
            l = ['--' + n for n in self.main_options
                 if n.startswith(cw)]
            retval = l
        elif self.current_word == self.qcloudcli:
            retval = self._documented(self.handleData.getAllModules())
        else:
            retval = self._documented(self.handleData.getAllModules(),
                                      startswith=self.current_word)
        return retval

    def _complete_command(self):
        retval = []
        if self.current_word == self.command_name:
            _operations = set()
            apiOperations = self.handleData.getModuleActions(self.command_name)
            from . import commandConfigure
            _configure = commandConfigure.commandConfigure()
            for item in apiOperations:
                _operations.add(item)
            if self.handleData.getModuleActions(self.command_name):
                retval = self._documented(_operations)
        elif self.current_word.startswith('-'):
            retval = self._find_possible_options()
        else:
            _operations = set()
            apiOperations = self.handleData.getModuleActions(self.command_name)
            from . import commandConfigure
            _configure = commandConfigure.commandConfigure()
            for item in apiOperations:
                _operations.add(item)
            if self.handleData.getModuleActions(self.command_name):
                retval = self._documented(_operations, startswith=self.current_word)
        return retval

    def _documented(self, table, startswith=None):
        names = []
        for key in table:
            if startswith is not None and not key.startswith(startswith):
                continue
            names.append(key)
        return names

    def _complete_subcommand(self):
        retval = []
        if self.current_word == self.operation:
            retval = []
        elif self.current_word.startswith('-'):
            retval = self._find_possible_options()
        return retval

    def _find_possible_options(self):
        all_options = copy.copy(self.main_options)
        cmdInstance = self.handleData.makeInstance(self.command_name, self.operation)
        mclassname = self.handleData.makeClass(self.command_name, self.operation)
        old_arg_list = list()
        if cmdInstance is None:
            from . import commandConfigure
            _configure = commandConfigure.commandConfigure()
            old_arg_list = _configure.getExtensionOptions(self.command_name, self.operation)
        else:
            old_arg_list = self.handleData.getSetFuncs(mclassname)
        new_arg_list = set()
        if not old_arg_list is None:
            for item in old_arg_list:
                if not item.startswith('_'):
                    new_arg_list.add(item)
            all_options = all_options + self._documented(new_arg_list)
        for opt in self.options:
            if opt != self.current_word:
                stripped_opt = opt.lstrip('-')
                if stripped_opt in all_options:
                    all_options.remove(stripped_opt)
        cw = self.current_word.lstrip('-')
        possibles = ['--' + n for n in all_options if n.startswith(cw)]
        if len(possibles) == 1 and possibles[0] == self.current_word:
            return self._complete_option(possibles[0])
        return possibles

    def _help_to_show_instance_attribute(self, classname, classnameVersion):
        com_options = copy.copy(self.main_options)
        com_options_version = copy.copy(self.main_options_version)
        old_arg_list = self.handleData.getSetFuncs(classname)
        old_arg_list_version = self.handleData.getSetFuncs(classnameVersion)
        new_arg_list = set()
        new_arg_list_version = set()
        if not old_arg_list is None:
            for item in old_arg_list:
                if not item.startswith('_'):
                    new_arg_list.add(item)
            action_options = self._documented(new_arg_list)
        if not old_arg_list_version is None:
            for item in old_arg_list_version:
                if not item.startswith('_'):
                    new_arg_list_version.add(item)
            action_options_version = self._documented(new_arg_list_version)
        if not action_options_version is None and 'Version' in action_options_version:
            action_options_version.remove('Version')
        com_possibles = ['--' + n for n in com_options]
        action_possibles = ['--' + n for n in action_options]
        com_possibles_version = ['--' + n for n in com_options_version]
        action_possibles_version = ['--' + n for n in action_options_version]
        return com_possibles, action_possibles, com_possibles_version, action_possibles_version

    def _process_command_line(self):
        self.command_name = None
        self.operation = None
        self.words = self.cmdline[0:self.point].split()
        self.current_word = self.words[-1]
        if len(self.words) >= 2:
            self.previous_word = self.words[-2]
        else:
            self.previous_word = None
        self.non_options = [w for w in self.words if not w.startswith('-')]
        self.options = [w for w in self.words if w.startswith('-')]
        for w in self.non_options:
            if w in self.handleData.getAllModules(): # cmd check
                self.command_name = w
                cmd_obj = self.handleData.getModuleActions(self.command_name)
                if not cmd_obj is None:
                    for w in self.non_options:
                        if w in cmd_obj:
                            self.operation = w
                            break
                break

    def complete(self, cmdline, point):
        self.cmdline = cmdline
        self.command_name = None
        if point is None:
            point = len(cmdline)
        self.point = point
        self._process_command_line()
        if not self.command_name:
            return self._complete_provider()
        if self.command_name and not self.operation:
            return self._complete_command()
        return self._complete_subcommand()


def complete(cmdline, point):
    choices = Completer().complete(cmdline, point)
    print((' \n'.join(choices)))


if __name__ == '__main__':
    pass
