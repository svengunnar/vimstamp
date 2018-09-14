import vim
from simplify import *

def vimstamp_init():
    vim.command('''
        function! VimStampOpenFile()
          pyx vimstamp_open_file()
        endfunction
            ''')

    vim.command('''
        function! VimStampWriteFile()
          pyx vimstamp_write_file()
        endfunction
            ''')

    vim.command("autocmd BufRead *.h,*.cpp :call VimStampOpenFile()")
    vim.command("autocmd BufWritePost *.h,*.cpp :call VimStampWriteFile()")

    vim.vars["g:vimstamp_idx2stamp"] = {}

def vimstamp_open_file():
    path = vim.bindeval("resolve(expand(\'%\'))").decode("utf-8")
    ts = get_time_stamp(path)
    s = simplify(vim.current.buffer)

    vim.vars["g:vimstamp_idx2stamp"][str(vim.current.window.buffer.number)] = (s, ts, path)

def vimstamp_write_file():
    s, ts, path = vim.vars["g:vimstamp_idx2stamp"][str(vim.current.window.buffer.number)]

    s_new = simplify(vim.current.buffer)
    ts_new = get_time_stamp(path)

    if s_new == s and ts != ts_new:
        set_time_stamp(path, ts)
        vim.command("e")

