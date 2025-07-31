---
title: htmlrenderer.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\htmlrenderer.md
created_at: 2025-07-03
---








  









## []HTML Renderer[] {#html-renderer style="tab-stops: 0pt"}

 

As the HTMLUI control supports rendering of web pages, it can be used like a light-weight web browser for compact applications that include links to references.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                              |
|                                                                                                                                                                                                       |
| [// Load the specified HTML document from System.Uri in to HTMLUI Control and renders it.]                                          |
|                                                                                                                                                                                                       |
| [string][ path = [\"http://www.Google.com\"];]           |
|                                                                                                                                                                                                       |
| [Uri][ uri = [new] [Uri](path);] |
|                                                                                                                                                                                                       |
| [htmluiControl1.LoadHTML(uri);]                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                                     |
| [\' Load the specified HTML document from System.Uri in to HTMLUI Control and renders it.]                                                                                        |
|                                                                                                                                                                                                                                                     |
| [Private][ path [As] [String] = [\"http://www.Google.com\"]] |
|                                                                                                                                                                                                                                                     |
| [Private][ uri [As] Uri = [New] Uri(path)]                                           |
|                                                                                                                                                                                                                                                     |
| [HtmluiControl1.LoadHTML(uri)]                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Also the ability of the HTMLUI control to load from strings can be used in creating HTML editors for tutorial applications.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                                   |
| **[]**                                                                                                          |
|                                                                                                                                                                                   |
| [// Load HTML Document from String.]                                                                            |
|                                                                                                                                                                                   |
| [string][ htmlString = [\"\<HTML\>]] |
|                                                                                                                                                                                   |
| [\<BODY\> Document loaded through the LoadFromString method \</BODY\> ]                                                       |
|                                                                                                                                                                                   |
| [\</HTML\>[\"; ]]                                                                                     |
|                                                                                                                                                                                   |
| [this][.htmluiControl1.LoadFromString(htmlString);]          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                      |
| [Private][ htmlString [As] [String] = [\"\<HTML\>\"]]                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [\<BODY\>Document loaded through the LoadFromString method[\</][BODY][\>] ]                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [\</][HTML][\>][\" ] |
|                                                                                                                                                                                                                                                                                                      |
| [Me][.HtmluiControl1.LoadFromString(htmlString)]                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following figure shows an HTML Editor rendered using HTMLUI.

[] 

                      {border="0"}

***[]*** 

Figure 37: HTML Editor rendered by using the HTMLUI Control

 

More:







