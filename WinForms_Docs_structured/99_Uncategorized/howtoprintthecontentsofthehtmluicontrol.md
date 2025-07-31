---
title: howtoprintthecontentsofthehtmluicontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoprintthecontentsofthehtmluicontrol.md
created_at: 2025-07-03
---








  









## How To Print the Contents Of the HTMLUI Control? {#how-to-print-the-contents-of-the-htmlui-control style="tab-stops: 0pt"}

[] 

The document available in the HTMLUI control can be printed with the help of the **HTMLUIPrintDocument** class. The **Print** method of this class is used to start the document printing process.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                                                           |
| **[]**                                                                                                                  |
|                                                                                                                                                                                           |
| [//represents printing support in the HTMLUI control]                                                                   |
|                                                                                                                                                                                           |
| [HTMLUIPrintDocument][ pd;]                                       |
|                                                                                                                                                                                           |
| [pd = [new] [HTMLUIPrintDocument]([this].htmluiControl1.Document);] |
|                                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                                           |
| [// starts the printing process ]                                                                                       |
|                                                                                                                                                                                           |
| [pd.Print();]                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [\'  represents printing support in the HTMLUI control]                                                                                                               |
|                                                                                                                                                                                                                                         |
| [Private][ pd [As] HTMLUIPrintDocument]                                                       |
|                                                                                                                                                                                                                                         |
| [Private][ pd = [New] HTMLUIPrintDocument([Me].HtmluiControl1.Document)] |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [\'  Starts the printing process]                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [pd.Print()]                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p197} 

 

[]{#related-topics}

