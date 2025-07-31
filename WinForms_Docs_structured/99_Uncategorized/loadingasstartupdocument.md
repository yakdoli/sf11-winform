---
title: loadingasstartupdocument.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\loadingasstartupdocument.md
created_at: 2025-07-03
---








  









### Loading As Startup Document {#loading-as-startup-document style="tab-stops: 0pt"}

[] 

An HTML document can be loaded at startup by two ways:

[] 

[·      ]Using the Properties window

[·      ]By coding

[] 

Using the Properties window, involves specifying the location of the startup HTML file by using the **StartupDocument** property of the HTMLUI control. The link shown at the bottom of the Properties window can also be used for the same purpose.

[] 

{border="0"}

[      ]

Figure 57: HTMLUI control Property Grid

**[]** 

While using code for the Startup Document, it should be written in the **Form_Load** event that occurs before the form is displayed for the first time. 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [// Get or Set the path to the Startup Document for the control.]                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [private][ [void] Form1_Load([object] sender, System.[EventArgs] e)] |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [this][.htmluiControl1.StartupDocument = [@\"C:\\MyProjects\\Startup\\startup_page.htm\"];]                    |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                |
| [\' Get or Set the path to the Startup Document for the control.]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                |
| [Me][.htmluiControl1.StartupDocument = [\"C:\\MyProjects\\Startup\\startup_page.htm\"]]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p195} 

[]{#related-topics}

