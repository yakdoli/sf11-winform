---
title: creatingdocumentcontainercontrol1.md
original_path: WinForms_Docs/99_Uncategorized/creatingdocumentcontainercontrol1.md
created_at: 2025-08-05
---






#### Creating Document Container control {#creating-document-container-control style="tab-stops: 0pt"}

There are two possible ways of creating a simple DocumentContainer control.

 

Through Designer

To create the Document Container control through designer, drag a Document Container control from the toolbox onto the design area.

 

{border="0"}

Figure 394: DocumentContainer control dragged from the Toolbox to the designer

 

Programmatically

To create the Document Container programmatically, use the following XAML or C# code.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<!\--][ Adding Document Container ][\--\>]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][syncfusion:DocumentContainer][ ][Name][=][\"[DocContainer]\"[/\>]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                                       |
| [//Creating instance of document container]                                         |
|                                                                                                                                                       |
| [DocumentContainer DocContainer = [new] DocumentContainer();]                |
|                                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                                       |
| [//Adding control to the window]                                                    |
|                                                                                                                                                       |
| [this][.Content = DocContainer;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p213} 

[]{#related-topics}

