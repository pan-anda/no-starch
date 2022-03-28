" All system-wide defaults are set in $VIMRUNTIME/debian.vim and sourced by
" the call to :runtime you can find below.  If you wish to change any of those
" settings, you should do it in this file (/etc/vim/vimrc), since debian.vim
" will be overwritten everytime an upgrade of the vim packages is performed.
" It is recommended to make changes after sourcing debian.vim since it alters
" the value of the 'compatible' option.

runtime! debian.vim

" Vim will load $VIMRUNTIME/defaults.vim if the user does not have a vimrc.
" This happens after /etc/vim/vimrc(.local) are loaded, so it will override
" any settings in these files.
" If you don't want that to happen, uncomment the below line to prevent
" defaults.vim from being loaded.
" let g:skip_defaults_vim = 1

" Uncomment the next line to make Vim more Vi-compatible
" NOTE: debian.vim sets 'nocompatible'.  Setting 'compatible' changes numerous
" options, so any other options should be set AFTER setting 'compatible'.
"set compatible

" Vim5 and later versions support syntax highlighting. Uncommenting the next
" line enables syntax highlighting by default.
if has("syntax")
endif

" If using a dark background within the editing area and syntax highlighting
" turn on this option as well
"set background=dark

" Uncomment the following to have Vim jump to the last position when
" reopening a file
"au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

" Uncomment the following to have Vim load indentation rules and plugins
" according to the detected filetype.
"filetype plugin indent on

" The following are commented out as they cause vim to behave a lot
"set showcmd		" Show (partial) command in status line.
"set showmatch		" Show matching brackets.
"set autowrite		" Automatically save before commands like :next and :make
"set hidden		" Hide buffers when they are abandoned
"set mouse=a		" Enable mouse usage (all modes)

"limelight need to set up these for showing(begining)
" Color name (:help cterm-colors) or ANSI code
let g:limelight_conceal_ctermfg = 'gray'
let g:limelight_conceal_ctermfg = 240

" Color name (:help gui-colors) or RGB color
let g:limelight_conceal_guifg = 'DarkGray'
let g:limelight_conceal_guifg = '#777777'

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
"disable markdown folding 
let g:vim_markdown_folding_disabled = 1
"(end)

syntax on               "代码高亮
set nocompatible        "不与 Vi 兼容
set nobackup            "覆盖文件时不保留备份文件
set noerrorbells        "有错误信息时不响铃
set visualbell t_vb=    "turn off error beep/flash 
set encoding=utf-8      "vim内使用的字符编码(缓冲区、寄存器、表达式所用字符)
set cursorline
set number
set hlsearch
exec "nohlsearch"       
set ignorecase          "忽略大小写
set infercase           "she加入补全列表
set smartcase           "大兼小写
set hidden              "离开当前缓冲区自动隐藏
set incsearch           "随输随找
set autoindent          "自动缩进
set history=200         "保存200条历史命令
set tabstop=4           "按Tab缩进4字符
set nrformats=          "所有数字十进制（007+1为008）
set shiftwidth=4 softtabstop=4 expandtab   "用< > 缩进
filetype plugin on
runtime macros/matchit.vim  "加载matchit插件(%在配对关键字间跳转)

"noremap
noremap U 5k            "向上5行     
noremap E 5j            "向下5行
        "disable-arrowkeys
             "noremap <Up> <Nop>
             "noremap <Down> <Nop>
             "noremap <Left> <Nop>
             "noremap <Right> <Nop>
"nnoremap
nnoremap ; :
nnoremap kj <Esc>       "退出插入模式  
"map
map <C-h> <C-w>h     "split-window focus on hjkl
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l
map Y y$                "复制光标到行尾
"cmap w!! w !sudo tee >/dev/null %     ":w!! 以root权限保存文件，需输密码

inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i
inoremap " ""<ESC>i
inoremap ' ''<ESC>i
inoremap < <><ESC>i
inoremap <C-b> ()<ESC>i
inoremap <C-g> ()<ESC>i''<ESC>i

inoremap ; :<CR>
inoremap <C-e> <End><CR>

nnoremap :q :q!
nnoremap :wq :wq!
nnoremap zs 0i#<Esc> 

"ab
ab mp MarkdownPreview
ab pi PlugInstall
ab qq q!
ab wqq wq!
ab ct < C-v >
ab fj ####
ab jt →
ab sjt ⇒
ab 4k &#8195;

"iab
iab pt print('') 
iab sy """
iab pp print("\n")

nnoremap n20 20O<Esc>ggi
nnoremap n50 50O<Esc>ggi 
nnoremap n100 100O<Esc>ggi  
nnoremap nn10 10o<Esc>>kkkkkkkkki

"mapleader
"let mapleader="\"       "mapleader默认反斜杠
noremap<LEADER><CR> :nohlsearch<CR>    "取消高亮
map <leader>sa ggVG      "全选  

"脚本#1  按 F5 执行当前 Python 代码"
map <F5> :call PRUN()<CR>
func! PRUN()
    exec "w" 
    if &filetype == 'python'
        exec "!python %"
    endif
endfunc

"脚本#2  *查找选中文本 #反向
xnoremap * :<C-u>call <SID>VSetSearch('/')<CR>/<C-R>=@/<CR><CR>
xnoremap # :<C-u>call <SID>VSetSearch('?')<CR>?<C-R>=@/<CR><CR>
function! s:VSetSearch(cmdtype)
    let temp = @s
    norm! gv"sy
    let @/ = '\V' . substitute(escape(@s, a:cmdtype.'\'), '\n', '\\n', 'g')
    let @s = temp
endfunction)"

" Plugins
call plug#begin('~/.vim/plugged')
"Plug 'iamcco/markdown-preview.vim' 
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}
"fzf.vim
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
"airline
Plug 'vim-airline/vim-airline'
Plug 'connorholyday/vim-snazzy'
"limelight
Plug 'junegunn/limelight.vim'
"vim-markdown
Plug 'godlygeek/tabular'
Plug 'plasticboy/vim-markdown'
"auto-pair
Plug 'jiangmiao/auto-pairs'
"commentary(tim pope)
Plug 'tpope/vim-commentary'
"tpope/vim-surround
Plug 'tpope/vim-surround'
"# ae {motion}整个文件（=ae 自动缩进整个文件; gcae 注释整个文件 ）
"# Plug 'kana/vim-textobj-entire'
call plug#end()


" Source a global configuration file if available
if filereadable("/etc/vim/vimrc.local")
  source /etc/vim/vimrc.local
endif
