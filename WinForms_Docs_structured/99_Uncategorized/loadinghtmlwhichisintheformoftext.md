---
title: loadinghtmlwhichisintheformoftext.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\loadinghtmlwhichisintheformoftext.md
created_at: 2025-07-03
---






#### Loading HTML Which Is In the Form Of Text {#loading-html-which-is-in-the-form-of-text style="tab-stops: 0pt"}

[] 

The HTML code sometimes can be directly written and stored as a string. The HTML code available in the form of string is loaded into the HTMLUI Control by using the **LoadFromString** method and the HTML contents will be displayed in the HTMLUI control.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                                |
| **[]**                                                                                                       |
|                                                                                                                                                                                |
| [// Load HTML Document from String.]                                                                         |
|                                                                                                                                                                                |
| [string][ htmlCode =[\"\<HTML\>]] |
|                                                                                                                                                                                |
| [\<HEAD\>]                                                                                                                 |
|                                                                                                                                                                                |
| [\<TITLE\>HI\</TITLE\>]                                                                                                    |
|                                                                                                                                                                                |
| [\</HEAD\>]                                                                                                                |
|                                                                                                                                                                                |
| [\<BODY bgcolor=[\'#ffffff\']\>]                                                                   |
|                                                                                                                                                                                |
| [\<INPUT type=[\'button\'] id=[\'btn\']/\>\</INPUT\>]                      |
|                                                                                                                                                                                |
| [\</BODY\>]                                                                                                                |
|                                                                                                                                                                                |
| [\</HTML\>[\";]]                                                                                   |
|                                                                                                                                                                                |
| [this][.htmluiControl1.LoadFromString(htmlCode);]         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [\'  Load HTML Document from String]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [Private][ htmlCode [As] [String] = [\"\<HTML\>]]                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [\<HEAD\>]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| [\<TITLE\>HI[\</][TITLE][\>]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| [\</][HEAD][\>]                                                                         |
|                                                                                                                                                                                                                                                                                                     |
| [\<BODY bgcolor=[\'#ffffff\'\>]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [\<INPUT type=[\'button\' id=\'btn\'/\>\</INPUT\>]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                     |
| [\</][BODY][\>]                                                                         |
|                                                                                                                                                                                                                                                                                                     |
| [\</][HTML][\>][\"] |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.HtmluiControl1.LoadFromString(htmlCode)]                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

