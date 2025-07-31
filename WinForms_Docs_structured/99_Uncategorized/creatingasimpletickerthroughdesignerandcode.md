---
title: creatingasimpletickerthroughdesignerandcode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingasimpletickerthroughdesignerandcode.md
created_at: 2025-07-03
---






##### Creating a Simple Ticker through Designer and Code {#creating-a-simple-ticker-through-designer-and-code style="tab-stops: 0pt"}

[] 

Through Designer

[] 

1.   To the application add the Ticker control.

28.  Set the **Text** property to the string that should be displayed.

29.  Build and run the application.

[] 

Through Code

[] 

The following code snippet creates a ticker control and assigns the text that should be displayed.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                                                       |
| [  ]                                                                                                                                |
|                                                                                                                                                                                                       |
| [Ticker][ ticker1 = [new] [Ticker]();] |
|                                                                                                                                                                                                       |
| [form1.Controls.Add(ticker1);]                                                                                                                    |
|                                                                                                                                                                                                       |
| [ticker1.Text = [\"This is a sample text\"];]                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                                                 |
| [  ]                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [Private][ ticker1 [As] Ticker = [New] Ticker()] |
|                                                                                                                                                                                                                 |
| [form1.Controls.Add(ticker1)]                                                                                                                               |
|                                                                                                                                                                                                                 |
| [Private][ ticker1.Text = [\"This is a sample text\"]]              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

