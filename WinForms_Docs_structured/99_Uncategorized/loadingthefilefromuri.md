---
title: loadingthefilefromuri.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\loadingthefilefromuri.md
created_at: 2025-07-03
---






#### Loading the File From URI {#loading-the-file-from-uri style="tab-stops: 0pt"}

HTML contents can also be loaded from the URI (Uniform Resource Identifier). This is a great advantage of HTMLUI that it can be used for browsing purposes like popular web browsers.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [// Load the HTML document from the specified Uri in to HTMLUI Control.]                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [Uri][ uri = [new] [Uri]([\"http://www.syncfusion.com\"]);] |
|                                                                                                                                                                                                                                                          |
| [htmluiControl1.LoadHTML(uri);]                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [\'  Load the HTML document from the specified Uri in to HTMLUI Control.]                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [Private][ uri [As] Uri = [New] Uri([\"http://www.syncfusion.com\"])] |
|                                                                                                                                                                                                                                                              |
| [HtmluiControl1.LoadHTML(uri)]                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A new URI has to be declared in the code with the path from which the URI has to be loaded, as shown in the above example. The **URI** class provides an object representation of a URI and also provides easy access to the parts of the URI.

[]{#p26} 

[]{#related-topics}

