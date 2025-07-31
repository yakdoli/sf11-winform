---
title: elementformat.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\elementformat.md
created_at: 2025-07-03
---








  









## [][]{#p164}Element Format {#element-format style="tab-stops: 0pt"}

[[[]]]{.underline} 

Essential HTMLUI supports formatting of not only the entire HTML document as a whole, but also the individual elements. With HTMLUI, the user can replace any HTML element into some other format before displaying, in a view to develop advanced user interactivity.

\
The following snippet shows how a text content can be replaced with an image in a text sequence.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [private][ [const] [string] DEF_IMG_TAG = [\"\<img src=\'..\\\\..\\\\clock.jpg\'\>\"];] |
|                                                                                                                                                                                                                                                                                |
| [private][ [const] [string] DEF_TIME = [\"time\"];]                                     |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [private][ [void] htmluiControl1_LoadFinished([object] sender, System.[EventArgs] e)]   |
|                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                |
| [//  Returns the html element by its ID, defined in HTML document.]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [IHTMLElement][ p = [this].htmluiControl1.Document.GetElementByUserId([\"p\"]);]                          |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [// Replace the  HTML inner text of current element. ]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [p.InnerHTML = p.InnerHTML.Replace(DEF_TIME, DEF_IMG_TAG);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [this][.htmluiControl1.Refresh();]                                                                                                                        |
|                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Const] DEF_IMG_TAG [As] [String] = [\"\<img src=\'..\\..\\clock.jpg\'\>\"]]                                                             |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Const] DEF_TIME [As] [String] = [\"time\"]]                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] htmluiControl1_LoadFinished([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\'  Returns the html element by its ID, defined in HTML document. ]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ p [As] IHTMLElement = [Me].htmluiControl1.Document.GetElementByUserId([\"p\"])]                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' Replace the  HTML inner text of current element ]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [p.InnerHTML = p.InnerHTML.Replace(DEF_TIME, DEF_IMG_TAG)]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.htmluiControl1.Refresh()]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image shows the text element **Time** replaced by an image while displayed using HTMLUI.

 

 

{border="0"}

 

Figure 45: Formatting HTML Elements by using HTMLUI Control

[]{#p165} 

More:





