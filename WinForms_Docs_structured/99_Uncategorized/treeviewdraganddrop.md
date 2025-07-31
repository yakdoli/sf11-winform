---
title: treeviewdraganddrop.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\treeviewdraganddrop.md
created_at: 2025-07-03
---






#### TreeView Drag and Drop   {#treeview-drag-and-drop style="tab-stops: 0pt"}

Drag and Drop support allows users to drag-and-drop the nodes within the TreeView control and also drag a particular node from one tree to another tree.

 

Use Case Scenarios

You can reorder nodes by using this drag-and-drop support.

You can move a particular node from one tree to another tree.

Properties

+---------------------------------------+----------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------+-------------------------------+
| **Property**                          | **Description**                                                            | **Type**                               | **Data Type**                                 | **Reference**                 |
+---------------------------------------+----------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------+-------------------------------+
| DragandDrop[] | It gives the functionality to drag-and-drop nodes in the TreeView control. | Server side [] | Binary, true/false[ ] | NA [] |
|                                       |                                                                            |                                        |                                               |                               |
|                                       | The default value is false.[]                      |                                        |                                               |                               |
+---------------------------------------+----------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------+-------------------------------+

 

Events

  **[Event ]**[]   **[Description ]**[]   **[Arguments ]**[]   **[Type ]**[]
  ------------------------------------------------------------ ------------------------------------------------------------------ ---------------------------------------------------------------- -----------------------------------------------------------
  ClientSideOnDragStarts                                       Raised when the drag starts.                                       obj, args                                                        Client Side
  ClientSideOnDragging                                         Raised during node dragging.                                       obj, args                                                        Client Side
  ClientSideOnDropping                                         Raised when the node is dropped.                                   obj, args                                                        Client Side
  ClientSideOnDropped                                          Triggered when dropped node is added in Target.                    obj, args                                                        Client Side

 

Sample Link

To view a sample:

1.   Open the Essential Tools sample browser from the dashboard. (Refer to the Samples and Location chapter).

2.   Navigate to **Tools.MVC** \> **TreeView** \> **Drag and Drop**[]

 

Adding Drag-and-Drop to an Application\
Using TreeViewBuilder

Implement the drag-and-drop option in the TreeView control by using TreeViewBuilder:

1.   Create a **view**.

2.   In the **view**, invoke the **TreeView** helper with the control ID.

3.   Set the **DragandDrop** property as **True**.


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().TreeView([\"myTreeView\"])**.**DragandDrop([true])][.Items(items =\>] |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                        { ]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                            items.Add().Text([\"Web Team\"]).Value([\"BI\"]).Children(child =\>]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                            {]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                                child.Add().Text([\"Smith\"]).Value([\"BIC\"]);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                                child.Add().Text([\"Johnson\"]).Value([\"BICl\"]);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                                child.Add().Text([\"Anderson\"]).Value([\"BIG\"]);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                            });]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                            items.Add().Text([\"Windows Team\"]).Value([\"R\"])]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [.Children(child =\>]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                            {]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                                child.Add().Text([\"Clark\"]).Value([\"REX\"]);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                                child.Add().Text([\"Wright\"]).Value([\"RED\"]);]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                                child.Add().Text([\"Lopez\"]).Value([\"REP\"]);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                            });]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [\...]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [\...]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [                        })]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [%\>][]                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\@{][Html.Syncfusion][.TreeView([\"myTreeView\"])**.**DragandDrop([true])][.Items(items =\>] |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                        { ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                            items.Add().Text([\"Web Team\"]).Value([\"BI\"]).Children(child =\>]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                            {]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                                child.Add().Text([\"Smith\"]).Value([\"BIC\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                                child.Add().Text([\"Johnson\"]).Value([\"BICl\"]);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                                child.Add().Text([\"Anderson\"]).Value([\"BIG\"]);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                            });]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                            items.Add().Text([\"Windows Team\"]).Value([\"R\"])]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                       |
| [.Children(child =\>]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                            {]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                                child.Add().Text([\"Clark\"]).Value([\"REX\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                                child.Add().Text([\"Wright\"]).Value([\"RED\"]);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                                child.Add().Text([\"Lopez\"]).Value([\"REP\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                            });]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\...]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\...]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                       |
| [                        })]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                       |
| [.Render();]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                       |
| [}][]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

4.   Build and run the application.

{border="0"} 

Figure 313: TreeView---Drag-and-Drop (Before and After)

 

Using TreeViewModel

Implement the drag-and-drop option in the TreeView control by using TreeViewModel:

1.   In the **controller**, create an object for the **TreeViewModel** class.

2.   Set the **DragandDrop** property as **True**.

3.   Pass the **TreeViewModel** class to the **ViewData**.

 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      **\[Controller\]**]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| [        [public] [ActionResult] Index()]                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [            [TreeViewModel] myModel = [new] [TreeViewModel]();]                                                                |
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
| [            myModel.][DragandDrop][ = [true];[     ]]   |
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


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().TreeView([\"myTreeView\"])][%\>][] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [@][Html.Syncfusion][.TreeView([\"myTreeView\"])][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

7.   Build and run the application.

{border="0"}  

Figure 314: TreeView---Drag and Drop (Before and After)

More:





