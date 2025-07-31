---
title: addingtabsplitteritemtothetabsplittercontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingtabsplitteritemtothetabsplittercontrol.md
created_at: 2025-07-03
---






##### Adding TabSplitterItem to the TabSplitter Control {#adding-tabsplitteritem-to-the-tabsplitter-control style="tab-stops: 0pt"}

TabSplitter contains one or more pages that are defined as TabSplitter Items. Use the following code to add a TabSplitter Item to the TabSplitter control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<!\-- Adding TabSplitter \--\>]                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][TabSplitter][ Name][=\"tabsplitter\"\>]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    ][\<!\-- Adding TabSplitterItem \--\>]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [   \<][syncfusion][:][TabSplitterItem][ Header][=\"Window1.xaml\"][ [Name][=\"tabSplitterItem1\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    ][\</][syncfusion][:][TabSplitterItem][\>]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\</][syncfusion][:][TabSplitter][\>]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [\[C#\]]                                                                                                                                             |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
| [// Creating an instance of TabSplitter]                                                                                                             |
|                                                                                                                                                                                                        |
| [TabSplitter][ tabSplitter = [new] [TabSplitter]();]              |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
| [// Creating an instance of TabSplitterItem]                                                                                                         |
|                                                                                                                                                                                                        |
| [TabSplitterItem][ tabSplitterItem1 = [new] [TabSplitterItem]();] |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
| [// Adding header of the TabSplitterItem]                                                                                                            |
|                                                                                                                                                                                                        |
| [tabSplitterItem1.Header = [\"Window1.xaml\"];         ]                                                                                   |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
| [// Adding TabSplitter Item to TabSplitter]                                                                                                          |
|                                                                                                                                                                                                        |
| [tabSplitter.Items.Add(tabSplitterItem1);]                                                                                                                         |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
| [// Adding TabSplitter to Window ]                                                                                                                   |
|                                                                                                                                                                                                        |
| [this][.Content = tabsplitter;]                                                                                   |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

{border="0"}

Figure 1016: TabSplitter Item Added to TabSplitter Control

[]{#related-topics}

