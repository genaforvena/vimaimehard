" Guard against multiple inclusions
if exists("g:loaded_vimaimehard")
  finish
endif
let g:loaded_vimaimehard = 1

" Define the command :Vimaimehard
command! -nargs=+ Vimaimehard call s:HandleUserRequest(<f-args>)

" Global variable to track recording state
let g:vimaimehard_recording = 0

" Global list to store command history
let g:vimaimehard_command_history = []

function! s:HandleUserRequest(...)
  let l:user_request = join(a:000, " ")

  " Call the Python script and capture the output
  let l:command_response = system('python3 python/vimaimehard.py ' . shellescape(l:user_request))

  " Prepare the command to be fed into Vim's command line
  let l:vim_command = ':' . l:command_response . "\<Left>"

  " Split the response into lines
  let l:response_lines = split(l:command_response, '\n')

  " Open a new buffer for the response
  new
  setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile

  " Insert the response lines into the buffer
  call setline(1, l:response_lines)
  setlocal nomodified
endfunction

function! s:StartRecording()
    let g:vimaimehard_recording = 1
    let g:vimaimehard_command_history = []
    echo "Vimaimehard recording started."
endfunction

function! s:StopRecording()
    let g:vimaimehard_recording = 0
    echo "Vimaimehard recording stopped."
    call s:AnalyzeCommands()
endfunction

augroup vimaimehard
    autocmd!
    autocmd CmdlineEnter : if g:vimaimehard_recording | call s:RecordCommand()
augroup END

function! s:RecordCommand()
    " Example of recording a command. This needs to be fleshed out
    " to capture the actual command entered by the user.
    let l:command = getcmdline()
    call add(g:vimaimehard_command_history, l:command)
endfunction
 

function! s:SerializeHistory()
    let l:json_str = '['
    for l:index in range(len(g:vimaimehard_command_history))
        let l:cmd = g:vimaimehard_command_history[l:index]
        let l:json_str .= '"' . escape(l:cmd, '"\') . '"'
        if l:index < len(g:vimaimehard_command_history) - 1
            let l:json_str .= ', '
        endif
    endfor
    let l:json_str .= ']'
    return l:json_str
endfunction

function! s:AnalyzeCommands()
    let l:json_str = s:SerializeHistory()
    let l:command_response = system('python3 python/vimaimehard.py --analyze ' . shellescape(l:json_str))
    let l:response_lines = split(l:command_response, '\n')
    new
    setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile
    call setline(1, l:response_lines)
    setlocal nomodified
endfunction

command! VimaimehardStartRecording call s:StartRecording()
command! VimaimehardStopRecording call s:StopRecording()

