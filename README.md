# Open with External Application

*Open with External Application* is a Sublime Text plugin that allows you to quickly open the current file in an external application.  This is useful for situations where you have a viewer-type application such as Marked.app that you can use to preview a file you're editing.

Please note that currently only macOS is supported.

## Installation

Clone this repository into your Sublime Text Packages directory.

    PACKAGE_DIR="$HOME/Library/Application Support/Sublime Text 3/Packages"
    REPO_URL="https://github.com/bkyle/sublime-plugin-open-with"
    (cd "${PACKAGE_DIR}" && git clone "${REPO_URL}")

## Configuration

By default, this plugin will open the default application that's configured by the operating system.  This can be overriden by configuration for this plugin.  The plugin looks for settings in a file called `Open-With.sublime-settings` in all of the usual places.

All of the editor configuration is stored under a dictionary with the key `editors`.  The keys for this dictionary are the file extensions, without a leading `.`, e.g. `md` would by used for a file called `README.md`.  The value for each key is either absolute path of the application to launch or a macOS bundle identifier.

A skeleton configuration is as follows.

    {
    	"editors": {
    		"md": "com.brettterpstra.marked2",
    		"txt": "TextEdit.app"
    	}
    }
