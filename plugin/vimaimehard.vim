" Guard against multiple inclusions
if exists("g:loaded_vimaimehard")
  finish
endif
let g:loaded_vimaimehard = 1

" Define the command :Vimaimehard
command! -nargs=+ Vimaimehard call s:HandleUserRequest(<f-args>)

function! s:HandleUserRequest(...)
  let l:user_request = join(a:000, " ")

  " Call the Python script and capture the output
  let l:command_response = system('python3 python/vimaimehard.py ' . shellescape(l:user_request))

  " Prepare the command to be fed into Vim's command line
  let l:vim_command = ':' . l:command_response . "\<Left>"

  " Use feedkeys to put the command in Vim's command line
  call feedkeys(l:vim_command, 'n')
endfunction

