# vimstamp
vim plugin to avoid changing mtime when comments, white spaces and newlines are changed.

If you change a comment in some header file and then recompile your project you may be in for a long wait. This plugin tries to fix this issue by retaining the old mtime if nothing changed.
