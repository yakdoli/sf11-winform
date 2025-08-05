---
title: draganddropcustomization.md
original_path: WinForms_Docs/99_Uncategorized/draganddropcustomization.md
created_at: 2025-08-05
---






##### Drag and Drop Customization {#drag-and-drop-customization style="tab-stops: 0pt"}

Drag and Drop Customization

This feature provides support to customize the drag-and-drop option. We are able to customize the drop position by enabling and disabling the child and sibling drop. Node drag operations can be customized by enabling and disabling drag-and-drop across the control.

 

Use Case Scenarios

You can customize the drag-and-drop functionality.

 

Properties

+--------------------------+--------------------------------------------------------------------------------+-------------+-----------------------------------------------+----------------------------------------------------------+
| **Property**             | **Description**                                                                | **Type**    | **Data Type**                                 | **Reference**                                            |
+--------------------------+--------------------------------------------------------------------------------+-------------+-----------------------------------------------+----------------------------------------------------------+
| DragandDropAcrossControl | Allows drag-and-drop of TreeView control nodes to another TreeView or control. | Server side | Binary, true/false[ ] | [DragandDrop] |
|                          |                                                                                |             |                                               |                                                          |
|                          | The default value is true.                                                     |             |                                               |                                                          |
+--------------------------+--------------------------------------------------------------------------------+-------------+-----------------------------------------------+----------------------------------------------------------+
| DropChild                | Enables drop as a child functionality.                                         | Server side | Binary, true/false[ ] | [DragandDrop] |
|                          |                                                                                |             |                                               |                                                          |
|                          | The default value is true.                                                     |             |                                               |                                                          |
+--------------------------+--------------------------------------------------------------------------------+-------------+-----------------------------------------------+----------------------------------------------------------+
| DropSibling              | Enables drop as a sibling node functionality.                                  | Server side | Binary, true/false[ ] | [DragandDrop] |
|                          |                                                                                |             |                                               |                                                          |
|                          | The default value is true.                                                     |             |                                               |                                                          |
+--------------------------+--------------------------------------------------------------------------------+-------------+-----------------------------------------------+----------------------------------------------------------+

 

Sample Link

To view a sample:

1.   Open the Essential Tools sample browser from the dashboard. (Refer to the Samples and Location chapter).

2.   Navigate to **Tools.MVC** \> **TreeView** \> **Drag and Drop**[]

 

Adding Drag-and-Drop Customization to an Application

Using TreeViewBuilder

Drag-and-drop can be customized in the TreeView control by using TreeViewBuilder.

1.   Create a **view**.

2.   In the **view**, invoke the **TreeView** helper with the control ID.

3.   Set the **DragandDrop** property as **True** and set values for other properties like **DragandDropAcrossControl**, **DropChild**, and **DropSibling** to customize them.


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().TreeView([\"myTreeView\"], [\"treeView\"])**.**DragandDrop([true])] |
|                                                                                                                                                                                                                                                                                                                                                         |
| [.DragandDropAcrossControl([true]).DropChild([false]).DropSibling([true])][ .Items(items =\>]                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                        { ]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                            items.Add().Text([\"Web Team\"]).Value([\"BI\"]).Children(child =\>]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                            {]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                                child.Add().Text([\"Smith\"]).Value([\"BIC\"]);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                                child.Add().Text([\"Johnson\"]).Value([\"BICl\"]);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                                child.Add().Text([\"Anderson\"]).Value([\"BIG\"]);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                            });]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                            items.Add().Text([\"Windows Team\"]).Value([\"R\"])]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [.Children(child =\>]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                            {]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                                child.Add().Text([\"Clark\"]).Value([\"REX\"]);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                                child.Add().Text([\"Wright\"]).Value([\"RED\"]);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                                child.Add().Text([\"Lopez\"]).Value([\"REP\"]);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                            });]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\...]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\...]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                         |
| [                        })]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                         |
| [%\>][]                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [\@{][ ]                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
| [Html.Syncfusion][.TreeView([\"myTreeView\"], [\"treeView\"])**.**DragandDrop([true])]  |
|                                                                                                                                                                                                                                                                |
| [.DropChild([false]).DropSibling([true]).DragandDropAcrossControl([true])][ .Items(items =\>] |
|                                                                                                                                                                                                                                                                |
| [                        { ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                |
| [                            items.Add().Text([\"Web Team\"]).Value([\"BI\"]).Children(child =\>]                                                             |
|                                                                                                                                                                                                                                                                |
| [                            {]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Smith\"]).Value([\"BIC\"]);]                                                                             |
|                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Johnson\"]).Value([\"BICl\"]);]                                                                          |
|                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Anderson\"]).Value([\"BIG\"]);]                                                                          |
|                                                                                                                                                                                                                                                                |
| [                            });]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [                            items.Add().Text([\"Windows Team\"]).Value([\"R\"])]                                                                             |
|                                                                                                                                                                                                                                                                |
| [.Children(child =\>]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [                            {]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Clark\"]).Value([\"REX\"]);]                                                                             |
|                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Wright\"]).Value([\"RED\"]);]                                                                            |
|                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Lopez\"]).Value([\"REP\"]);]                                                                             |
|                                                                                                                                                                                                                                                                |
| [                            });]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [\...]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [\...]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [                        })]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                |
| [.Render();][]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [}][]                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

4.   Build and run the application.

{border="0"} 

Figure 315: TreeView---Sibling Drop (Before and After)

 

Using TreeViewModel

Drag-and-drop can be customized in the TreeView control by using TreeViewModel.

1.   In the **controller**, create an object for the **TreeViewModel** class.

2.   Set the **DragandDrop** property as **True** and set values for other properties like **DragandDropAcrossControl**, **DropChild**, and **DropSibling** to customize them.

3.   Pass the **TreeViewModel** class to the **ViewData**.

 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [        [public] [ActionResult] Index()]                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [            [TreeViewModel] myModel = [new] [TreeViewModel]();]                                                                |
|                                                                                                                                                                                                                                                       |
| [            myModel.][DragandDrop][ = [true]; ]                              |
|                                                                                                                                                                                                                                                       |
| [            myModel.][DragandDropAcrossControl][ = [true];]                  |
|                                                                                                                                                                                                                                                       |
| [            myModel.][DropChild ][= [true];]                                 |
|                                                                                                                                                                                                                                                       |
| [            myModel.][DropSibling ][= [false];]                              |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [            [List]\<[TreeViewItem]\> list = [new] [List]\<[TreeViewItem]\>();] |
|                                                                                                                                                                                                                                                       |
| [            list.Add([new] [TreeViewItem] { Text = [\"Smith\"] });]                                                            |
|                                                                                                                                                                                                                                                       |
| [            list.Add([new] [TreeViewItem] { Text = [\"Johnson\"] });]                                                          |
|                                                                                                                                                                                                                                                       |
| [            list.Add([new] [TreeViewItem] { Text = [\"Anderson\"] });]                                                         |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [            myModel.Items.Add([new] [TreeViewItem]() { Text = [\"Web Team\"], Children = list });]                             |
|                                                                                                                                                                                                                                                       |
| [            myModel.Items.Add([new] [TreeViewItem]() { Text = [\"Windows Team\"] });]                                          |
|                                                                                                                                                                                                                                                       |
| [\...]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [\...]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [            ViewData\[[\"myTreeView\"]\] = myModel;]                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| [            [return] View();]                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [        }][]                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

4.   Create a **view**.

5.   In the **view**, invoke the **TreeView** helper with the control ID.

6.   From the **ViewData**, assign the **TreeViewModel** class to the **TreeView** helper.


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().TreeView][([\"myTreeView\"])][%\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [@][Html.Syncfusion().TreeView][([\"myTreeView\"])][] |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

7.   Build and run the application.

{border="0"}  

Figure 316: TreeView---Sibling Drop (Before and After)

[]{#related-topics}

