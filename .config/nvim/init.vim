set nocompatible
filetype off
call plug#begin()
Plug 'roxma/nvim-completion-manager'
Plug 'junegunn/goyo.vim' 
Plug 'junegunn/limelight.vim'
Plug 'SirVer/ultisnips'
Plug 'xuhdev/vim-latex-live-preview'
Plug 'honza/vim-snippets'
Plug 'euclio/vim-markdown-composer'
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() } } 
call plug#end()

set number
" enable syntax highlighting
syntax enable
set encoding=utf-8
" show line numbers
set number

" set tabs to have 4 spaces
set ts=4

" indent when moving to the next line while writing code
set autoindent

" expand tabs into spaces
set expandtab

" when using the >> or << commands, shift lines by 4 spaces
set shiftwidth=4

" show a visual line under the cursor's current line
set cursorline

" show the matching part of the pair for [] {} and ()
set showmatch

" enable all Python syntax highlighting features
let python_highlight_all = 1
 
 
 " or path directly to the library file

"let g:clang_exec = '/usr/bin/clang'
"let g:clang_library_path='/usr/lib64/libclang.so.7'
"let g:clang_use_library = 1
"let g:clang_user_options = '2> NUL || exit 0"'

" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
" % Set the following lines in your ~/.vimrc or the systemwide /etc/vimrc:
filetype plugin indent on
set grepprg=grep\ -nH\ $*
let g:tex_flavor = "latex"

" % Also, this installs to /usr/share/vim/vimfiles, which may not be in
" % your runtime path (RTP). Be sure to add it too, e.g:
set runtimepath=~/.vim,$VIM/vimfiles,$VIMRUNTIME,$VIM/vimfiles/after,~/.vim/after
" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
" color name (:help cterm-colors) or ANSI code
let g:limelight_conceal_ctermfg = 'gray'
let g:limelight_conceal_ctermfg = 240

" Color name (:help gui-colors) or RGB color
let g:limelight_conceal_guifg = 'SlateBlue'
"let g:limelight_conceal_guifg = '#777777'

" Default: 0.5
let g:limelight_default_coefficient = 0.7

" Number of preceding/following paragraphs to include (default: 0)
let g:limelight_paragraph_span = 1

" Beginning/end of paragraph
"   When there's no empty line between the paragraphs
"   and each paragraph starts with indentation
let g:limelight_bop = '^\s'
let g:limelight_eop = '\ze\n^\s'

" Highlighting priority (default: 10)
"   Set it to -1 not to overrule hlsearch
let g:limelight_priority = -1

autocmd User GoyoEnter Limelight
autocmd User GoyoLeave Limelight!<Paste>
