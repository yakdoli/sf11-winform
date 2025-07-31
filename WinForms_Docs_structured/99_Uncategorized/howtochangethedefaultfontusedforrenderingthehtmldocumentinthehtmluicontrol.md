---
title: howtochangethedefaultfontusedforrenderingthehtmldocumentinthehtmluicontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtochangethedefaultfontusedforrenderingthehtmldocumentinthehtmluicontrol.md
created_at: 2025-07-03
---








  









## How To Change the Default Font Used For Rendering the HTML Document In the HTMLUI Control? {#how-to-change-the-default-font-used-for-rendering-the-html-document-in-the-htmlui-control style="tab-stops: 0pt"}

[] 

HTMLUI uses a default font to render the text from the HTML document, in cases where there are no specifications for the font to be used. You can change this default font by using the **DefaultFormat.Font** property, written while initializing the HTMLUI control.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                                           |
| [htmluiControl1 = [new] Syncfusion.Windows.Forms.HTMLUI.[HTMLUIControl]();] |
|                                                                                                                                                                           |
| [htmluiControl1.DefaultFormat.Font = [new] Font([\"Pristina\"],16);]      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [Private][ htmluiControl1 = [New] Syncfusion.Windows.Forms.HTMLUI.HTMLUIControl()]                   |
|                                                                                                                                                                                                                                                |
| [Private][ htmluiControl1.DefaultFormat.Font = [New] Font([\"Pristina\"],16)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p188} 

 

[]{#related-topics}

