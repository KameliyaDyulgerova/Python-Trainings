<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">

    <title>Jupyter Notebook</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="/static/base/images/favicon-notebook.ico?v=eb02bb6f6435d048eba1bf1bd3b3621f8c14f26518dbadd8efd4ee6ee2721caf2367bc0cbc27d2ee2c35bc3b035aad07c6d625422b9445bf301897f493d0edc5">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="/static/components/jquery-ui/themes/smoothness/jquery-ui.min.css?v=fb45616eef2c454960f91fcd2a04efeda84cfacccf0c5d741ba2793dc1dbd6d3ab01aaae6485222945774c7d7a9a2e9fb87e0d8ef1ea96893aa6906147a371bb" type="text/css" />
    <link rel="stylesheet" href="/static/components/jquery-typeahead/dist/jquery.typeahead.min.css?v=5edf53bf6bb9c3b1ddafd8594825a7e2ed621f19423e569c985162742f63911c09eba2c529f8fb47aebf27fafdfe287d563347f58c1126b278189a18871b6a9a" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    


<script type="text/javascript" src="/static/components/MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML-full,Safe&delayStartupUntil=configured" charset="utf-8"></script>

<script type="text/javascript">
// MathJax disabled, set as null to distinguish from *missing* MathJax,
// where it will be undefined, and should prompt a dialog later.
window.mathjax_url = "/static/components/MathJax/MathJax.js";
</script>

<link rel="stylesheet" href="/static/components/bootstrap-tour/build/css/bootstrap-tour.min.css?v=95c93e52db61ab29625defe55361384ce6776a7d303b97da5a73fef5ddf8e391a6223599a0b58669476bd71645a4f0022df0517c88b0c05df80ba465e36f5417" type="text/css" />
<link rel="stylesheet" href="/static/components/codemirror/lib/codemirror.css?v=81fecb54f83101e2bbe6d2e3131e252ac83f2910366100ca83ba4834f5d41754c837f306eecfdceed05f9c9111614942e2ced5acdd8040746b66c6bef0141d0e">


    <link rel="stylesheet" href="/static/style/style.min.css?v=b092d0a2da5df36f2b073ddb4eafcd6c8094c4fa21b6dcd3f7185ce16c04ad66424083d785b81607a26b4b85b69a560574ada7db75262c886655f99d651c482e" type="text/css"/>
    

<link rel="stylesheet" href="/static/notebook/css/override.css?v=16733f6ba5f2224692fe4e654f3cbb2e3cae82f1df06ca53aa1cb88b147465f16c968c0898e2b0203a7ad3a469f82b959e26bb4b27b790f7f364c4336449b0aa" type="text/css" />
<link rel="stylesheet" href=""  id='kernel-css'                             type="text/css" />


    <link rel="stylesheet" href="/custom/custom.css" type="text/css" />
    <script src="/static/components/es6-promise/promise.min.js?v=bea335d74136a63ae1b5130f5ac9a50c6256a5f435e6e09fef599491a84d834a8b0f011ca3eaaca3b4ab6a2da2d3e1191567a2f171e60da1d10e5b9d52f84184" type="text/javascript" charset="utf-8"></script>
    <script src="/static/components/react/react.production.min.js?v=9a0aaf84a316c8bedd6c2ff7d5b5e0a13f8f84ec02442346cba0b842c6c81a6bf6176e64f3675c2ebf357cb5bb048e0b527bd39377c95681d22468da3d5de735" type="text/javascript"></script>
    <script src="/static/components/react/react-dom.production.min.js?v=6fc58c1c4736868ff84f57bd8b85f2bdb985993a9392718f3b4af4bfa10fb4efba2b4ddd68644bd2a8daf0619a3844944c9c43f8528364a1aa6fc01ec1b8ae84" type="text/javascript"></script>
    <script src="/static/components/create-react-class/index.js?v=894ad57246e682b4cfbe7cd5e408dcd6b38d06af4de4f3425991e2676fdc2ef1732cbd19903104198878ae77de12a1996de3e7da3a467fb226bdda8f4618faec" type="text/javascript"></script>
    <script src="/static/components/requirejs/require.js?v=d37b48bb2137faa0ab98157e240c084dd5b1b5e74911723aa1d1f04c928c2a03dedf922d049e4815f7e5a369faa2e6b6a1000aae958b7953b5cc60411154f593" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20230218141801",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

</head>

<body class="notebook_app "
 


  
    data-jupyter-api-token="e70d8a0621220fd27754f46a339ed88d703dcbeac56179b6"
  
 
data-base-url="/"
data-ws-url=""
data-notebook-name="Cards.ipynb"
data-notebook-path="Cards.ipynb"

dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="/tree?token=e70d8a0621220fd27754f46a339ed88d703dcbeac56179b6" title='dashboard'>
      <img src='/static/base/images/logo.png?v=a2a176ee3cee251ffddf5fa21fe8e43727a9e5f87a06f9c91ad7b776d9e9d3d5e0159c16cc188a3965e00375fb4bc336c16067c688f5040c0c2d4bfdb852a9e4' alt='Jupyter Notebook'/>
  </a></div>

  


<span id="save_widget" class="save_widget">
    <span id="notebook_name" class="filename"></span>
    <span class="checkpoint_status"></span>
    <span class="autosave_status"></span>
</span>


  

<span id="kernel_logo_widget">
  
  <img class="current_kernel_logo" alt="Current Kernel Logo" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
  
</span>


  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
<div id="menubar-container" class="container">
<div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
            <button type="button" class="btn btn-default navbar-btn navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <i class="fa fa-bars"></i>
              <span class="navbar-text">Menu</span>
            </button>
            <p id="kernel_indicator" class="navbar-text indicator_area">
              <span class="kernel_indicator_name">Kernel</span>
              <i id="kernel_indicator_icon"></i>
            </p>
            <i id="readonly-indicator" class="navbar-text" title='This notebook is read-only'>
                <span class="fa-stack">
                    <i class="fa fa-save fa-stack-1x"></i>
                    <i class="fa fa-ban fa-stack-2x text-danger"></i>
                </span>
            </i>
            <i id="modal_indicator" class="navbar-text"></i>
            <span id="notification_area"></span>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="dropdown"><a href="#" class="dropdown-toggle" id="filelink" data-toggle="dropdown" aria-haspopup="true" aria-controls="file_menu">File</a>
                    <ul id="file_menu" class="dropdown-menu" role="menu" aria-labelledby="filelink">
                        <li id="new_notebook" class="menu_focus_highlight dropdown dropdown-submenu" role="none">
                            <a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">New Notebook<span class="sr-only">Dropdown</span></a>
                            <ul class="dropdown-menu" id="menu-new-notebook-submenu" role="menu">
                            </ul>
                        </li>
                        <li id="open_notebook" role="none"
                            title="Opens a new window with the Dashboard view">
                            <a href="#" role="menuitem">Open...</a></li>
                        <!-- <hr/> -->
                        <li class="divider" role="none"></li>
                        <li id="copy_notebook" role="none"
                            title="Open a copy of this notebook's contents and start a new kernel">
                            <a href="#" role="menuitem">Make a Copy...</a></li>
                        <li id="save_notebook_as" role="none"
                            title="Save a copy of the notebook's contents and start a new kernel">
                            <a href="#" role="menuitem">Save as...</a></li>
                        <li id="rename_notebook" role="none"><a href="#" role="menuitem">Rename...</a></li>
                        <li id="save_checkpoint" role="none"><a href="#" role="menuitem">Save and Checkpoint</a></li>
                        <!-- <hr/> -->
                        <li class="divider" role="none"></li>
                        <li id="restore_checkpoint" class="menu_focus_highlight dropdown-submenu" role="none"><a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Revert to Checkpoint<span class="sr-only">Dropdown</span></a>
                          <ul class="dropdown-menu">
                            <li><a href="#"></a></li>
                            <li><a href="#"></a></li>
                            <li><a href="#"></a></li>
                            <li><a href="#"></a></li>
                            <li><a href="#"></a></li>
                          </ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="print_preview" role="none"><a href="#" role="menuitem">Print Preview</a></li>
                        <li class="dropdown-submenu menu_focus_highlight" role="none"><a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Download as<span class="sr-only">Dropdown</span></a>
                            <ul id="download_menu" class="dropdown-menu">
                                
                                <li id="download_asciidoc">
                                    <a href="#">AsciiDoc (.asciidoc)</a>
                                </li>
                                
                                <li id="download_html">
                                    <a href="#">HTML (.html)</a>
                                </li>
                                
                                <li id="download_latex">
                                    <a href="#">LaTeX (.tex)</a>
                                </li>
                                
                                <li id="download_markdown">
                                    <a href="#">Markdown (.md)</a>
                                </li>
                                
                                <li id="download_notebook">
                                    <a href="#">Notebook (.ipynb)</a>
                                </li>
                                
                                <li id="download_pdf">
                                    <a href="#">PDF via LaTeX (.pdf)</a>
                                </li>
                                
                                <li id="download_rst">
                                    <a href="#">reST (.rst)</a>
                                </li>
                                
                                <li id="download_script">
                                    <a href="#">Script ()</a>
                                </li>
                                
                                <li id="download_slides">
                                    <a href="#">Reveal.js slides (.slides.html)</a>
                                </li>
                                
                                <li id="download_webpdf">
                                    <a href="#">PDF via HTML (.html)</a>
                                </li>
                                
                            </ul>
                        </li>
                        <li class="dropdown-submenu hidden" role="none"><a href="#" role="menuitem">Deploy as</a>
                            <ul id="deploy_menu" class="dropdown-menu"></ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="trust_notebook" role="none"
                            title="Trust the output of this notebook">
                            <a href="#" role="menuitem">Trust Notebook</a></li>
                        <li class="divider" role="none"></li>
                        <li id="close_and_halt" role="none"
                            title="Shutdown this notebook's kernel, and close this window">
                            <a href="#" role="menuitem">Close and Halt</a></li>
                    </ul>
                </li>

                <li class="dropdown"><a href="#" class="dropdown-toggle" id="editlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="edit_menu">Edit</a>
                    <ul id="edit_menu" class="dropdown-menu" role="menu" aria-labelledby="editlink">
                        <li id="cut_cell" role="none"><a href="#" role="menuitem">Cut Cells</a></li>
                        <li id="copy_cell" role="none"><a href="#" role="menuitem">Copy Cells</a></li>
                        <li id="paste_cell_above" class="disabled" role="none"><a href="#" role="menuitem" aria-disabled="true">Paste Cells Above</a></li>
                        <li id="paste_cell_below" class="disabled" role="none"><a href="#" role="menuitem" aria-disabled="true">Paste Cells Below</a></li>
                        <li id="paste_cell_replace" class="disabled" role="none"><a href="#" role="menuitem" aria-disabled="true">Paste Cells &amp; Replace</a></li>
                        <li id="delete_cell" role="none"><a href="#" role="menuitem">Delete Cells</a></li>
                        <li id="undelete_cell" class="disabled" role="none"><a href="#" role="menuitem" aria-disabled="true">Undo Delete Cells</a></li>
                        <li class="divider" role="none"></li>
                        <li id="split_cell" role="none"><a href="#" role="menuitem">Split Cell</a></li>
                        <li id="merge_cell_above" role="none"><a href="#" role="menuitem">Merge Cell Above</a></li>
                        <li id="merge_cell_below" role="none"><a href="#" role="menuitem">Merge Cell Below</a></li>
                        <li class="divider" role="none"></li>
                        <li id="move_cell_up" role="none"><a href="#" role="menuitem">Move Cell Up</a></li>
                        <li id="move_cell_down" role="none"><a href="#" role="menuitem">Move Cell Down</a></li>
                        <li class="divider" role="none"></li>
                        <li id="edit_nb_metadata" role="none"><a href="#" role="menuitem">Edit Notebook Metadata</a></li>
                        <li class="divider" role="none"></li>
                        <li id="find_and_replace" role="none"><a href="#" role="menuitem"> Find and Replace </a></li>
                        <li class="divider" role="none"></li>
                        <li id="cut_cell_attachments" role="none"><a href="#" role="menuitem">Cut Cell Attachments</a></li>
                        <li id="copy_cell_attachments" role="none"><a href="#" role="menuitem">Copy Cell Attachments</a></li>
                        <li id="paste_cell_attachments"  class="disabled" role="none"><a href="#" role="menuitem" aria-disabled="true">Paste Cell Attachments</a></li>
                        <li class="divider" role="none"></li>
                        <li id="insert_image" class="disabled" role="none"><a href="#" role="menuitem" aria-disabled="true">  Insert Image </a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" id="viewlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="view_menu">View</a>
                    <ul id="view_menu" class="dropdown-menu" role="menu" aria-labelledby="viewlink">
                        <li id="toggle_header" role="none"
                            title="Show/Hide the logo and notebook title (above menu bar)">
                            <a href="#" role="menuitem">Toggle Header</a>
                        </li>
                        <li id="toggle_toolbar" role="none"
                            title="Show/Hide the action icons (below menu bar)">
                            <a href="#" role="menuitem">Toggle Toolbar</a>
                        </li>
                        <li id="toggle_line_numbers" role="none"
                            title="Show/Hide line numbers in cells">
                            <a href="#" role="menuitem">Toggle Line Numbers</a>
                        </li>
                        <li id="menu-cell-toolbar" class="menu_focus_highlight dropdown-submenu" role="none">
                            <a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Cell Toolbar</a>
                            <ul class="dropdown-menu" id="menu-cell-toolbar-submenu"></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" id="insertlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="insert_menu">Insert</a>
                    <ul id="insert_menu" class="dropdown-menu" role="menu" aria-labelledby="insertlink">
                        <li id="insert_cell_above" role="none"
                            title="Insert an empty Code cell above the currently active cell">
                            <a href="#" role="menuitem">Insert Cell Above</a></li>
                        <li id="insert_cell_below" role="none"
                            title="Insert an empty Code cell below the currently active cell">
                            <a href="#" role="menuitem">Insert Cell Below</a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" id="celllink" data-toggle="dropdown" aria-haspopup="true" aria-controls="cell_menu">Cell</a>
                    <ul id="cell_menu" class="dropdown-menu" role="menu" aria-labelledby="celllink">
                        <li id="run_cell" role="none" title="Run this cell, and move cursor to the next one">
                            <a role="menuitem" href="#">Run Cells</a></li>
                        <li id="run_cell_select_below" role="none" title="Run this cell, select below">
                            <a href="#" role="menuitem">Run Cells and Select Below</a></li>
                        <li id="run_cell_insert_below" role="none" title="Run this cell, insert below">
                            <a href="#" role="menuitem">Run Cells and Insert Below</a></li>
                        <li id="run_all_cells" role="none" title="Run all cells in the notebook">
                            <a href="#" role="menuitem">Run All</a></li>
                        <li id="run_all_cells_above" role="none" title="Run all cells above (but not including) this cell">
                            <a href="#" role="menuitem">Run All Above</a></li>
                        <li id="run_all_cells_below" role="none" title="Run this cell and all cells below it">
                            <a href="#" role="menuitem">Run All Below</a></li>
                        <li class="divider" role="none"></li>
                        <li id="change_cell_type" class="menu_focus_highlight dropdown-submenu" role="none"
                            title="All cells in the notebook have a cell type. By default, new cells are created as 'Code' cells">
                            <a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Cell Type</a>
                            <ul class="dropdown-menu" role="menu">
                              <li id="to_code" role="none"
                                  title="Contents will be sent to the kernel for execution, and output will display in the footer of cell">
                                  <a href="#">Code</a></li>
                              <li id="to_markdown"
                                  title="Contents will be rendered as HTML and serve as explanatory text">
                                  <a href="#">Markdown</a></li>
                              <li id="to_raw"
                                  title="Contents will pass through nbconvert unmodified">
                                  <a href="#">Raw NBConvert</a></li>
                            </ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="current_outputs" class="menu_focus_highlight dropdown-submenu" role="none"><a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Current Outputs</a>
                            <ul class="dropdown-menu" role="menu">
                                <li id="toggle_current_output" role="none"
                                    title="Hide/Show the output of the current cell">
                                    <a href="#">Toggle</a>
                                </li>
                                <li id="toggle_current_output_scroll"
                                    title="Scroll the output of the current cell">
                                    <a href="#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_current_output"
                                    title="Clear the output of the current cell">
                                    <a href="#">Clear</a>
                                </li>
                            </ul>
                        </li>
                        <li id="all_outputs" class="menu_focus_highlight dropdown-submenu" role="none"><a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">All Output</a>
                            <ul class="dropdown-menu" role="menu">
                                <li id="toggle_all_output" role="none"
                                    title="Hide/Show the output of all cells">
                                    <a href="#">Toggle</a>
                                </li>
                                <li id="toggle_all_output_scroll"
                                    title="Scroll the output of all cells">
                                    <a href="#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_all_output"
                                    title="Clear the output of all cells">
                                    <a href="#">Clear</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" id="kernellink">Kernel</a>
                    <ul id="kernel_menu" class="dropdown-menu" aria-labelledby="kernellink">
                        <li id="int_kernel"
                            title="Send Keyboard Interrupt (CTRL-C) to the Kernel">
                            <a href="#">Interrupt</a>
                        </li>
                        <li id="restart_kernel"
                            title="Restart the Kernel">
                            <a href="#">Restart</a>
                        </li>
                        <li id="restart_clear_output"
                            title="Restart the Kernel and clear all output">
                            <a href="#">Restart &amp; Clear Output</a>
                        </li>
                        <li id="restart_run_all"
                            title="Restart the Kernel and re-run the notebook">
                            <a href="#">Restart &amp; Run All</a>
                        </li>
                        <li id="reconnect_kernel"
                            title="Reconnect to the Kernel">
                            <a href="#">Reconnect</a>
                        </li>
                        <li id="shutdown_kernel"
                            title="Shutdown the Kernel">
                            <a href="#">Shutdown</a>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="menu-change-kernel" class="menu_focus_highlight dropdown-submenu" role="menuitem">
                            <a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Change kernel</a>
                            <ul class="dropdown-menu" id="menu-change-kernel-submenu"></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Help</a>
                    <ul  id="help_menu" class="dropdown-menu">
                        
                        <li id="notebook_tour" title="A quick tour of the notebook user interface"><a href="#">User Interface Tour</a></li>
                        <li id="keyboard_shortcuts" title="Opens a tooltip with all keyboard shortcuts"><a href="#">Keyboard Shortcuts</a></li>
                        <li id="edit_keyboard_shortcuts" title="Opens a dialog allowing you to edit Keyboard shortcuts"><a href="#">Edit Keyboard Shortcuts</a></li>
                        <li class="divider"></li>
                        

						
                        
                            
                                <li><a rel="noreferrer" href="http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Notebook Help
                                </a></li>
                            
                                <li><a rel="noreferrer" href="https://help.github.com/articles/markdown-basics/" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Markdown
                                </a></li>
                            
                            
                        
                        <li class="divider"></li>
                        <li title="About Jupyter Notebook"><a id="notebook_about" href="#">About</a></li>
                        
                    </ul>
                </li>
              </ul>
            </div>
        </div>
    </div>
</div>

<div id="maintoolbar" class="navbar">
  <div class="toolbar-inner navbar-inner navbar-nobg">
    <div id="maintoolbar-container" class="container"></div>
  </div>
</div>
</div>

<div class="lower-header-bar"></div>

</div>

<div id="site">


<div id="ipython-main-app">
    <div id="notebook_panel">
        <div id="notebook"></div>
        <div id='tooltip' class='ipython_tooltip' style='display:none'></div>
    </div>
</div>



</div>



<div id="pager">
    <div id="pager-contents">
        <div id="pager-container" class="container"></div>
    </div>
    <div id='pager-button-area'></div>
</div>






<script type="text/javascript">
    sys_info = {"notebook_version": "6.4.12", "notebook_path": "C:\\Users\\mn\\anaconda3\\Lib\\site-packages\\notebook", "commit_source": "", "commit_hash": "", "sys_version": "3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)]", "sys_executable": "C:\\Users\\mn\\anaconda3\\python.exe", "sys_platform": "win32", "platform": "Windows-10-10.0.19045-SP0", "os_name": "nt", "default_encoding": "utf-8"};
</script>

<script src="/static/components/text-encoding/lib/encoding.js?v=737ac6f9f978afb6348b5914877e7d7136de7465cd4cdf389bad9a6b3ad5ceffbfb23febc75c23378967d7d36f98f5388208e8eb78c80f2bf47e8f8c000481ad" charset="utf-8"></script>

<script src="/static/notebook/js/main.min.js?v=a4e125c812cb3975203ae429a5b40d180b59b8e4602fcc78390ef4f0dd4d14ac3559189f65f23cd50fd971f98f5842b7746f4182babd20b7ca84e52314bcd4ac" type="text/javascript" charset="utf-8"></script>



<script type='text/javascript'>
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>
</body>

</html>