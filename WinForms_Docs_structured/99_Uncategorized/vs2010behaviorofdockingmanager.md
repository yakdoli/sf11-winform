---
title: vs2010behaviorofdockingmanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\vs2010behaviorofdockingmanager.md
created_at: 2025-07-03
---






#### VS2010 Behavior of Docking Manager {#vs2010-behavior-of-docking-manager style="tab-stops: 0pt"}

This feature enables the user to drag the TDI Windows, which will automatically generate the Float window which will then be dropped at any corner of the docked windows or dropped at any specific TDI Index.

 

Use Case Scenarios

Users can drag the TDI window which will automatically generate the Float window which can be dropped at any corner of the docked windows instead of using Context Menu to choose Floating and then Dockable to achieve the above operation.

 

Properties

Table 12: Properties Table


  ------------------------- ----------------------------------------------------------------------------------- --------------------- ----------- -----------------
  Property                  Description                                                                         Type                  Data Type   Reference links
  IsVS2010DraggingEnabled   Gets or sets a value indicating whether the VS2010 behavior can be enabled or not   Dependency Property   Boolean      
  ------------------------- ----------------------------------------------------------------------------------- --------------------- ----------- -----------------


 

Adding VS2010 Behavior to an Application

The VS2010 behavior can be enabled by setting **[IsVS2010DraggingEnabled]** property to true which will enable the VS2010 drag and drop support of TDI Windows. The default value is set to false.

The property in Docking Manager and can be set in the following ways:

[·      ]Through XAML

[·      ]Through Code behind

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [   \[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [        ][\<][syncfusion][:][DockingManager][ UseDocumentContainer][=\"True\"][ Grid.RowSpan][=\"2\"][   IsVS2010DraggingEnabled][=\"True\"\>][]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            ][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            ][\<][StackPanel][ syncfusion][:][DockingManager.Header][=\"Tabbed Window 1\"][ syncfusion][:][DockingManager.State][=\"Document\"/\>][]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            ][\<][ContentControl][ syncfusion][:][DockingManager.Header][=\"Tabbed Window 2\"][ syncfusion][:][DockingManager.State][=\"Document\"/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            ][\<][ContentControl][ syncfusion][:][DockingManager.Header][=\"Tabbed Window 3\"][ syncfusion][:][DockingManager.State][=\"Document\"/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            ][\<][ContentControl][ syncfusion][:][DockingManager.Header][=\"Tabbed Window 4\"][ syncfusion][:][DockingManager.State][=\"Document\"/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            ][\<][ContentControl][ syncfusion][:][DockingManager.Header][=\"Tabbed Window 5\"][ syncfusion][:][DockingManager.State][=\"Document\"/\>]                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [        ][\</][syncfusion][:][DockingManager][\>]                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [  ][\[C#\] []]                                                                                |
|                                                                                                                                                                                                                |
| [            DockingManager][ dockingManager = [new] [DockingManager]();] |
|                                                                                                                                                                                                                |
| [            dockingManager.IsVS2010DraggingEnabled = [true]; ][]                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

