# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import ablog
import alabaster

# -- ABlog Sidebars -------------------------------------------------------

# There are seven sidebars you can include in your HTML output.
# postcard.html provides information regarding the current post.
# recentposts.html lists most recent five posts. Others provide
# a link to a archive pages generated for each tag, category, and year.
# In addition, there are authors.html, languages.html, and locations.html
# sidebars that link to author and location archive pages.
html_sidebars = {
    '**': [ 'about.html',
            'postcard.html', 'navigation.html',
            'recentposts.html', 'tagcloud.html',
            'categories.html',  'archives.html',
            'searchbox.html',
            ],
    }

# -- Project information -----------------------------------------------------
# 项目名
project = 'MyBlog'
# 版权，著作权
copyright = '2023, Eugene Forest'
# 作者
author = 'Eugene Forest'

# The short X.Y version. 主要项目版本，用作 |version| .
version = 'alpha'
# The full version, including alpha/beta/rc tags. 完整的项目版本，用作 |release|
release = 'alpha'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%Y-%m-%d, %H:%M:%S"

# The encoding of source files.
# 建议的编码和默认值是 'utf-8-sig' .
source_encoding = 'utf-8-sig'

# The master toctree document.
# “主控”文档的文档名称，即包含根目录的文档 toctree 指令。
# 在 2.0 版更改: 默认值更改为 'index' 从 'contents' .
master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# 在这里以字符串的形式添加任何Sphinx扩展模块名。
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    'ablog',
    'alabaster',
]
myst_update_mathjax = False
# "sphinx.ext.todo" : 对TODO项的支持
# "sphinx.ext.intersphinx" :链接到其他项目的文档
# "sphinx.ext.autosectionlabel" : label 标签自动选中确保唯一性,并允许引用节使用其标题,同时自动为标题创建label
# 'myst_parser' : myst 解析器, 默认情况下，myst_parser 会解析 markdown(.md) ,而 .rst 文件会被 Sphinx 原生解析器 restructureText 解析。
# "sphinx_design" : 用于设计美观、视图大小的响应式 Web 组件。
# "sphinx_copybutton": 代码块复制按钮扩展

# Make sure the target is unique (sphinx.ext.autosectionlabel 插件的配置)
autosectionlabel_prefix_document = True

# MyST Markdown 扩展语法
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "smartquotes", "replacements",
    "linkify",
    "html_image",
    "substitution",
    "dollarmath", "amsmath",
]
# 如果为false,只有包含方案（例如http）的链接才会被识别为外部链接
myst_linkify_fuzzy_links = False
# substitution 的扩展的全局替换，作用于 .md
myst_substitutions = {}
# default is ['{', '}']，替换指令分隔符，不建议更改
# myst_sub_delimiters = ["|", "|"]

# 数学公式语法 $ （dollar math） 设置
myst_dmath_allow_labels = True
myst_dmath_double_inline = True
# myst_dmath_allow_space = False, will cause inline math to only be parsed if there are no initial / final spaces, e.g. $a$ but not $ a$ or $a $.
# myst_dmath_allow_digits = False, will cause inline math to only be parsed if there are no initial / final digits, e.g. $a$ but not 1$a$ or $a$2.

# -- global replace order configuration are as follows---
# 全局字符串替换指令
# 需要注意的是，全局加入替换的功能要谨慎使用，要酌情使用；因为在这里添加后会影响到项目所有的 rst 文件（在所有 rst 文件中添加定义的替换指令）
# 一串 reStructuredText，它将包含在每个读取的源文件的末尾。 这是一个可以添加应该在每个文件中可用的替换的地方
rst_prolog = """
.. |15| raw:: html
      
      <hr width='15%'>

.. |30| raw:: html
      
      <hr width='30%'>
      
.. |50| raw:: html
      
      <hr width='50%'>

.. |75| raw:: html
      
      <hr width='75%'>

"""

# 图片编号功能
# -- numfig configuration are as follows---
# 表格和代码块如果有标题则会自动编号
numfig = True
# -- numfig_secnum_depth configuration are as follows---
# 如果设置为“0”，则数字，表格和代码块从“1”开始连续编号。
# 如果“1”(默认)，数字将是“x.1”。“x.2”，… 与“x”的节号(顶级切片;没有“x”如果没有部分)。只有当通过 toctree 指令的“:numbered:”选项激活了段号时，这才自然适用。
# 如果“2”，表示数字将是“x.y.1”，“x.y.2”，…如果位于子区域(但仍然是 x.1 ，x.2 ，… 如果直接位于一个部分和 1 ，2 ， … 如果不在任何顶级部分。)
numfig_secnum_depth = 2
# -- numfig_format configuration are as follows---
# 一个字典将“‘figure’”，“‘table’”，“‘code-block’”和“‘section’”映射到用于图号格式的字符串。作为一个特殊字符，“%s”将被替换为图号。
# 默认是使用“‘Fig.%s’”为“‘figure’”, “‘Table%s’”为“‘table’”，“‘Listing%s’”为“‘code-block’”和“‘Section’”为 “‘section’”。
numfig_format = {'code-block': '代码块 %s', }
# -- html_codeblock_linenos_style configuration are as follows---
# 代码块的行号样式
html_codeblock_linenos_style = 'table'
# html_codeblock_linenos_style = 'inline'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# 博客的过滤和搜索
exclude_patterns = [
    "posts/*/.ipynb_checkpoints/*",
    ".github/*",
    ".history",
    "github_submodule/*",
    "LICENSE.md",
    "README.md",
]
blog_post_pattern = ["src/*.rst","src/*.md"]

# -- Sphinx Options -----------------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates", ablog.get_html_templates_path()]

# The suffix(es) of source filenames.
source_suffix = ".md"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = "False"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'github_button': False,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [alabaster.get_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# 添加你自己的 CSS 规则
html_static_path = ['_static']
html_css_files = ["custom.css"]

# 自定义徽标、和网站图标
html_logo = "./_static/template.svg"
html_favicon = "./_static/template.svg"

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%%b %%d, %%Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "MyBlogdoc"
