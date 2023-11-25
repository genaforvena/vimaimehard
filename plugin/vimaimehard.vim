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

  " Use the response in your Vim script
  echo l:command_response
endfunction
