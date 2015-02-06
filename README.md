MML-Frontend
===========================================================
* Homepage: https://github.com/aabaa/mmlfrontend
* Generated Reference: http://webmizar.cs.shinshu-u.ac.jp/mmlfe/current/

Overview
===========================================================
This program downloads and analyzes Mizar Wiki, or HTML-ized MML files, and generates HTML file for each term definition.
It is similar to documentation generator for programming language, like Doxygen.

Features
===========================================================
## List of Terms
All terms defined in MML (predicate, structure, mode, functor, attribute) are contained in a list-box in the left pain.
By clicking a term, you can jump to its page.

## Incremental Search
You can narrow list of terms by inputting words in the upper-left search-box.
If several words (separated with spaces) are input, the system squeezes the list of terms which includes all the input words.
The search logic is case-insensitive.

## Source
HTML structure of source code is copied from Mizar Wiki.
By clicking a keyword, you can jump to the term page or, if it is not a term, jump to a corresponding Mizar Wiki page.

## Referenced In
You can check dependency between terms in MML.
The following relations are listed up in each term page.
* mode, structure
** mode, structure, function, attribute, predicate
* function, attribute
** cluster

Installation
===========================================================
1. Install [PyCharm](https://www.jetbrains.com/pycharm/)
2. Install [Anaconda 3.4](http://continuum.io/downloads#py34)
3. Prepare required libraries (listed in requirements.txt) from Settings - Project Interpreter
4. Install Plugins from Setting - Plugins
  * [Markdown preview](https://plugins.jetbrains.com/plugin/5970?pr=phpStorm)
5. Prepare [CoffeeScript environment](https://www.jetbrains.com/pycharm/webhelp/transpiling-coffeescript-to-javascript.html)

Usage
===========================================================
1. Run downloader.py to download HTML-ized MML articles.
  * It will download from http://mizar.org/version/current/html by default.
  * You can change the URL by modifying the following code in 'mmlfrontend/downloader.py'
    ```
    downloader.read_index('http://mizar.org/version/current/html')
    ```
  * You also have to change article_path in 'mmlfrontend/html/js/mml-var.js' before you deploy.
2. Run processor.py to create HTML files. The files will be created in 'html' folder.

Dependencies
===========================================================
* This product is implemented in Python and CoffeeScript.
* See requirements.txt for a list of third-party libraries used in this product.
* I would like to mention that logic of incremental search is based on **JsonIndex generator** used in [RDoc](https://github.com/rdoc/rdoc/blob/master/lib/rdoc/generator/template/json_index/js/searcher.js).
* This work deeply depends on the study of **mwiki**. See [website](http://cs.ru.nl/~urban/MathWiki.html) for more details.

License
===========================================================
MML-frontend is Copyright (c) 2015 Kazuhisa Nakasho, a graduate student in Shinshu University.
This program code and its product are published under GNU General Public License version 3 or later.
See [LICENSE.md](LICENSE.md) for more details.

Contact
===========================================================
E-mail: 13st205f@shinshu-u.ac.jp
