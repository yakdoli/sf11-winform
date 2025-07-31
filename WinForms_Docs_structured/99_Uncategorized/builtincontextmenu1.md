---
title: builtincontextmenu1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\builtincontextmenu1.md
created_at: 2025-07-03
---








  









### Built-In Context Menu {#built-in-context-menu style="TEXT-ALIGN: justify; tab-stops: 0pt"}

 

Essential Diagram for Windows Forms provides Built-in Context Menu support for Diagram.

 

All available tools for Diagram control, File options, Edit options, Action options, Layout, Connectors and Shapes will be listed in the Built-in Context Menu.

 

Use Case Scenarios

This feature enables easy access of frequently used options.

 

Properties

Table 3: Property[ ]Table


  --------------------------- -------------------------------------- ------ ----------- -----------------
  Property                    Description                            Type   Data Type   Reference links
  DefaultContextMenuEnabled   Used to enable default context menu.   NA     Boolean     NA
  --------------------------- -------------------------------------- ------ ----------- -----------------


[] 

Enabling Default Context Menu

You can enable the default context menu using the *DefaultContextMenuEnabled* property.

The following code illustrates how to enable the default context menu:

 

+---------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                              |
|                                                                                                                     |
|                                                                                                                     |
|                                                                                                                     |
| [//show default context menu]                                     |
|                                                                                                                     |
| [            diagram1.DefaultContextMenuEnabled = [true];] |
+---------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                       |
|                                                                                                                    |
| [\'show default context menu]                                    |
|                                                                                                                    |
| [            diagram1.DefaultContextMenuEnabled = [True]] |
+--------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 118: Default Context Menu\
\

[            ]

The following code illustrates how to disable the default context menu:

 

+----------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                           |
|                                                                                                                      |
| []                                                                 |
|                                                                                                                      |
| [//hide default context menu]                                      |
|                                                                                                                      |
| [            diagram1.DefaultContextMenuEnabled = [false];] |
+----------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                          |
|                                                                                                                     |
| []                                                                |
|                                                                                                                     |
| [\'hide default context menu]                                     |
|                                                                                                                     |
| [            diagram1.DefaultContextMenuEnabled = [False]] |
+---------------------------------------------------------------------------------------------------------------------+

 

 

 

Sample Link

To view a sample:

 

1.   Open the Syncfusion Dashboard.

2.   Click the **Windows Forms** drop-down list and select **Run Locally Installed Samples.**

3.   Navigate to **Diagram[ ]Samples \> Product Showcase \> Diagram Builder.**

                      

[]{#related-topics}

