---
title: tdtablecelltag.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tdtablecelltag.md
created_at: 2025-07-03
---








  









### TD - Table Cell Tag {#td---table-cell-tag style="tab-stops: 0pt"}

[] 

The **Table Cell** tag defines a cell inside a table. The **\<td\>** tag has a parent \<tr\> tag to define the row and a \<table\> tag to define the table in which it is present. The td tag in HTMLUI supports the following attributes that help the user in designing custom structures for their documents easily.

[] 

[·      ]**align**: Specifies the alignment of the text inside the table cell

[·      ]**bgcolor**: Specifies a background color for the specified cell

[·      ]**colspan**: Spans the cell to the specified number of columns. This is used in merging the columns in the table.

[·      ]**height**: Specifies custom height for the cells

[·      ]**nowrap**: Extends the text inside a particular cell into a single line. This display extends the width of the cell according to the contents inside it.

[·      ]**rowspan**: Extends the height of the cell to the specified number of rows. This is helpful in custom merging the rows of the given cell

[·      ]**valign**: Determines the vertical alignment of the text inside the table cell

[·      ]**width**: Specifies user-defined width for the specified cells

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[HTML\]]**                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [File Location and Name:  C:\\MyProjects\\table\\td.html]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][html][\>]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][body][\>]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][table][ [border] [=] [\"1\"\>]]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][tr][\>]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][ [\>]Sample[\</][td][\>]]                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][ [align][=\"center\"\>]Text Aligned Cell[\</][td][\>]]                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][tr][\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][tr][\>]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][ [bgcolor][=\"Blue\"\>]bgcolor cell[\</][td][\>]]                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][ [\>]Cell[\</][td][\>]]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][tr][\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][tr][\>]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][ [colspan][=2\>]Colspan cell[\</][td][\>]]                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][tr][\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][tr][\>]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][ [height][=\"50\"\>]Custom height cell[\</][td][\>]]                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][ [nowrap][\>]nowrap cell[\</][td][\>]]                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][tr][\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][tr][\>]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][ [rowspan][=2\>]Rowspan cell[\</][td][\>]]                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][ [valign][=\"bottom\"] [height][=\"80\"\>]V align cell[\</][td][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][tr][\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][tr][\>]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][ [width][=\"300\"\>]custom width cell[\</][td][\>]]                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][tr][\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][tr][\>]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][\>][Cell[\</][td][\>]]                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][td][\>][Cell[\</][td][\>]]                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][tr][\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][table][\>]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][body][\>]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][html][\>]                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                                      |
| **[]**                                                                                                                                             |
|                                                                                                                                                                                                                      |
| [this][.htmluiControl.LoadHTML([@\"C:\\MyProjects\\table\\td.html\"]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                                   |
| [Me][.htmluiControl.LoadHTML(@[\"C:\\MyProjects\\table\\td.html\"])] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

