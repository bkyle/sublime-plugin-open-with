import subprocess
import sys
import os

import sublime
import sublime_plugin

class OpenWithExternalAppCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    if sys.platform.startswith("darwin"):
      self.view.run_command("save")
      self._perform_open()

  def _perform_open(self):
    base, ext = os.path.splitext(self.view.file_name())
    ext = ext.lower().replace(".", "")

    # Find the configured editor based on the extension.  If there is a configured editor
    # then determine whether or not the editor is an application or a bundle identifier.
    # The parameters used to start the "open" command will depend on whether or not the
    # value is an app or bundle identifier.
    settings = sublime.load_settings("Open-With.sublime-settings")
    app = settings.get("editors.%s" % ext)
    if app:
      cmd = ["open"]
      if os.path.exists(app):
        cmd += ["-a", app]
      else:
        cmd += ["-b", app]
      cmd += [self.view_file_name()]
      if sub_process.call(cmd) == 0:
        return

    # If there was no configured application, or the invocation of open with the
    # configured application failed then just open the application with the
    # default editor.
    subprocess.call(["open", self.view.file_name()])
