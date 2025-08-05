---
title: databindingandselectionmodes.md
original_path: WinForms_Docs/03_Data_Binding/databindingandselectionmodes.md
created_at: 2025-08-05
---






#### Data binding and Selection Modes {#data-binding-and-selection-modes style="tab-stops: 0pt"}

[] 

Data Binding

 

Data binding is used in Web pages that contain interactive components such as forms, calculators, tutorials, and games. Pages are displayed incrementally so that portions of a page can be used even before the entire page has finished downloading. Data binding helps in populating the Grid List control with large amounts of data. This can be achieved by using DataSource property which allows the system to acquire data from the Data Source Object (DSO).

 

The following code example illustrates data binding for Grid List control by using DataSource property.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| **[]**                                                                                                                                |
|                                                                                                                                                                                         |
| [ArrayList][ array = [new] [ArrayList]();        ] |
|                                                                                                                                                                                         |
| [array.Add([new] MyClass(001,[\"John David\"]));]                                                      |
|                                                                                                                                                                                         |
| [array.Add([new] MyClass(002,[\"Tom\"]));]                                                             |
|                                                                                                                                                                                         |
| [array.Add([new] MyClass(003,[\"Bretney\"]));]                                                         |
|                                                                                                                                                                                         |
| [array.Add([new] MyClass(004,[\"Jessy\"]));]                                                           |
|                                                                                                                                                                                         |
| [array.Add([new] MyClass(005,[\"Bruch\"]));]                                                           |
|                                                                                                                                                                                         |
| [array.Add([new] MyClass(006,[\"Johny\"]));]                                                           |
|                                                                                                                                                                                         |
| [this][.gridlistControl1.DataSource = array;]                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                              |
|                                                                                                                                                                                 |
| []                                                                                                                             |
|                                                                                                                                                                                 |
| [Dim][ array [As] ArrayList = [New] ArrayList()] |
|                                                                                                                                                                                 |
| [array.Add([New] \[MyClass\](1, [\"John David\"]))]                                            |
|                                                                                                                                                                                 |
| [array.Add([New] \[MyClass\](2, [\"Tom\"]))]                                                   |
|                                                                                                                                                                                 |
| [array.Add([New] \[MyClass\](3, [\"Bretney\"]))]                                               |
|                                                                                                                                                                                 |
| [array.Add([New] \[MyClass\](4, [\"Jessy\"]))]                                                 |
|                                                                                                                                                                                 |
| [array.Add([New] \[MyClass\](5, [\"Bruch\"]))]                                                 |
|                                                                                                                                                                                 |
| [array.Add([New] \[MyClass\](6, [\"Johny\"]))]                                                 |
|                                                                                                                                                                                 |
| [Me][.gridlistControl1.DataSource = array]                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Selection Modes

 

The selection behavior for Grid List control can be specified by using SelectionMode property. There are 3 types of selection behaviors:

[] 

[·      ]**One**--Allows the user to select only one item.

[·      ]**MultiSimple**--Allows the user to select multiple items.

[·      ]**MultiExtended**--Allows the user to select multiple items using SHIFT, CTRL, and

[·      ]  arrow keys etc.          

[] 

The following code example illustrates setting of various selection behaviors for the Grid List control.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [this][.gridListControl1.SelectionMode = [SelectionMode].One;]           |
|                                                                                                                                                                                       |
| [this][.gridListControl1.SelectionMode = [SelectionMode].MultiSimple;]   |
|                                                                                                                                                                                       |
| [this][.gridListControl1.SelectionMode = [SelectionMode].MultiExtended;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                               |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [Me][.gridListControl1.SelectionMode = [SelectionMode.One]]           |
|                                                                                                                                                                                  |
| [Me][.gridListControl1.SelectionMode = [SelectionMode.MultiSimple]]   |
|                                                                                                                                                                                  |
| [Me][.gridListControl1.SelectionMode = [SelectionMode.MultiExtended]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p522} 

 

[]{#related-topics}

