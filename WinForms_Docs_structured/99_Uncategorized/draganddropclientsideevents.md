---
title: draganddropclientsideevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\draganddropclientsideevents.md
created_at: 2025-07-03
---






#### Drag-and-Drop Client-Side Events {#drag-and-drop-client-side-events style="tab-stops: 0pt"}

Client-side events are triggered in response to specific actions on the client.

Use Case Scenarios

You are able to control the drag-and-drop functionality in the client-side by using the client-side events.

You are able to get the drag node, target node, and drop position using the client-side event arguments.

Events

  **[Event ]**[]   **[Description ]**[]   **[Arguments ]**[]   **[Type ]**[]
  ------------------------------------------------------------ ------------------------------------------------------------------ ---------------------------------------------------------------- -----------------------------------------------------------
  ClientSideOnDragStarts                                       Raised when the drag starts.                                       obj, args                                                        Client side
  ClientSideOnDragging                                         Raised during node drag.                                           obj, args                                                        Client side
  ClientSideOnDropping                                         Raised when the node drops.                                        obj, args                                                        Client side
  ClientSideOnDropped                                          Triggered when dropped node is added in target.                    obj, args                                                        Client side

 

Sample Link

To view a sample:

1.   Open the Essential Tools sample browser from the dashboard. Refer to the Samples and Location chapter.

2.   Navigate to **Tools.MVC** \> **TreeView** \> **Drag and Drop**[]

 

Adding Drag-and-Drop Client-Side Events to an Application

Using TreeViewBuilder

Manage client-side events of drag-and-drop in the TreeView control by using TreeViewBuilder.

1.   Create a **view**.

2.   In the **view**, invoke the **TreeView** helper with the control ID.

3.   Set the **DragandDrop** property as **True** and set values for other client-side events.


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().TreeView([\"myTreeView"])**.**DragandDrop([true])] |
|                                                                                                                                                                                                                                                                                                                |
| [.ClientSideOnDragging([\"Drag\"]).ClientSideOnDragStarts([\"DragStart\"])]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                |
| [.ClientSideOnDropped([\"Drop\"]).ClientSideOnDropping([\"Dropping\"])]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| [.DragandDropAcrossControl([true])][.Items(items =\>]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                |
| [                        { ]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                |
| [                            items.Add().Text([\"Web Team\"]).Value([\"BI\"]).Children(child =\>]                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [                            {]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Smith\"]).Value([\"BIC\"]);]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Johnson\"]).Value([\"BICl\"]);]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Anderson\"]).Value([\"BIG\"]);]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                |
| [                            });]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [                            items.Add().Text([\"Windows Team\"]).Value([\"R\"])]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [.Children(child =\>]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [                            {]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Clark\"]).Value([\"REX\"]);]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Wright\"]).Value([\"RED\"]);]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                |
| [                                child.Add().Text([\"Lopez\"]).Value([\"REP\"]);]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [                            });]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [\...]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [\...]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [                        })]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                |
| [%\>][]                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [\@{][ ]                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [Html.Syncfusion][.TreeView([\"myTreeView\"])**.**DragandDrop([true])]                       |
|                                                                                                                                                                                                                                             |
| [.ClientSideOnDragging([\"Drag\"]).ClientSideOnDragStarts([\"DragStart\"])]                                                                |
|                                                                                                                                                                                                                                             |
| [.ClientSideOnDropped([\"Drop\"]).ClientSideOnDropping([\"Dropping\"])][.Items(items =\>] |
|                                                                                                                                                                                                                                             |
| [                        { ]                                                                                                                                                               |
|                                                                                                                                                                                                                                             |
| [                            items.Add().Text([\"Web Team\"]).Value([\"BI\"]).Children(child =\>]                                          |
|                                                                                                                                                                                                                                             |
| [                            {]                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [                                child.Add().Text([\"Smith\"]).Value([\"BIC\"]);]                                                          |
|                                                                                                                                                                                                                                             |
| [                                child.Add().Text([\"Johnson\"]).Value([\"BICl\"]);]                                                       |
|                                                                                                                                                                                                                                             |
| [                                child.Add().Text([\"Anderson\"]).Value([\"BIG\"]);]                                                       |
|                                                                                                                                                                                                                                             |
| [                            });]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                            items.Add().Text([\"Windows Team\"]).Value([\"R\"])]                                                          |
|                                                                                                                                                                                                                                             |
| [.Children(child =\>]                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [                            {]                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [                                child.Add().Text([\"Clark\"]).Value([\"REX\"]);]                                                          |
|                                                                                                                                                                                                                                             |
| [                                child.Add().Text([\"Wright\"]).Value([\"RED\"]);]                                                         |
|                                                                                                                                                                                                                                             |
| [                                child.Add().Text([\"Lopez\"]).Value([\"REP\"]);]                                                          |
|                                                                                                                                                                                                                                             |
| [                            });]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [\...]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [\...]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [                        })]                                                                                                                                                               |
|                                                                                                                                                                                                                                             |
| [.Render();]                                                                                                                                                                               |
|                                                                                                                                                                                                                                             |
| [}][]                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [   [\<][script] [type][=\"text/javascript\"\>]]                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [   [function] DragStart(arg1,arg2){]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                  |
| [       \$([\"#TA\"]).text([\"DragStart\\n\"] + \$([\"#TA\"]).text())]                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [   [function] Dropping(arg1, arg2) {]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [       \$([\"#TA\"]).text([\"Dropping\\n\"] + \$([\"#TA\"]).text())]                                                                                      |
|                                                                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [   [function] Drag(arg1, arg2) {]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [       \$([\"#TA\"]).text([\"Dragging\\n\"] + \$([\"#TA\"]).text())]                                                                                      |
|                                                                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [   [function] Drop(arg1) {]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                  |
| [       [if] (\$(arg1.get_target()).attr([\"id\"]) != ][\"TA\"][)] |
|                                                                                                                                                                                                                                                                                  |
| [           \$([\"#TA\"]).text([\"Drop\\n\"] + \$([\"#TA\"]).text());]                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [       ][else][]                                                                                                |
|                                                                                                                                                                                                                                                                                  |
| [           \$([\"#TA\"]).text(arg1.get_nodeText());]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [   [\</][script][\>] ]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

4.   Build and run the application.

{border="0"} 

Figure 329: TreeView---Drag and Drop (Before and After)

 

Using TreeViewModel

Manage client-side events of drag-and-drop in the TreeView control by using TreeViewModel:

1.   In the **controller**, create an object for the **TreeViewModel** class.

2.   Set the **DragandDrop** property as **True** and set values for other client-side events.

3.   Pass the **TreeViewModel** class to the **ViewData**.

 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                             |
| [        [public] [ActionResult] Index()]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                             |
| [            [TreeViewModel] myModel = [new] [TreeViewModel]();]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                             |
| [            myModel.][DragandDrop][ = [true]; ]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                             |
| [            myModel.][ClientSideOnDragging][ = ][\"Drag\"][;]         |
|                                                                                                                                                                                                                                                                                                                                             |
| [            myModel.][ClientSideOnDragStarts][ = ][\"DragStarts\"][;] |
|                                                                                                                                                                                                                                                                                                                                             |
| [            myModel.][ClientSideOnDropped][ = ][\"Dropped\"][;]       |
|                                                                                                                                                                                                                                                                                                                                             |
| [            myModel.][ClientSideOnDropping][ = ][\"Dropping\"][;]     |
|                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                             |
| [            [List]\<[TreeViewItem]\> list = [new] [List]\<[TreeViewItem]\>();]                                                                                       |
|                                                                                                                                                                                                                                                                                                                                             |
| [            list.Add([new] [TreeViewItem] { Text = [\"Smith\"] });]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                             |
| [            list.Add([new] [TreeViewItem] { Text = [\"Johnson\"] });]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                             |
| [            list.Add([new] [TreeViewItem] { Text = [\"Anderson\"] });]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                             |
| [            myModel.Items.Add([new] [TreeViewItem]() { Text = [\"Web Team\"], Children = list });]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                             |
| [            myModel.Items.Add([new] [TreeViewItem]() { Text = [\"Windows Team\"] });]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                             |
| [\...]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                             |
| [\...]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                             |
| [            ViewData\[[\"myTreeView\"]\] = myModel;]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                             |
| [            [return] View();]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                             |
| [        }][]                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

4.   Create a **view**.

5.   In the **view**, invoke the **TreeView** helper with the control ID.

6.   From the **ViewData**, assign the **TreeViewModel** class to the **TreeView** helper.


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().TreeView][([\"myTreeView\"], [\"treeView\"])][%\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                     |
| [@][Html.Syncfusion().TreeView][([\"myTreeView\"], [\"treeView\"])][] |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [   [\<][script] [type][=\"text/javascript\"\>]]                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [   [function] DragStart(arg1,arg2){]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                  |
| [       \$([\"#TA\"]).text([\"DragStart\\n\"] + \$([\"#TA\"]).text())]                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [   [function] Dropping(arg1, arg2) {]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [       \$([\"#TA\"]).text([\"Dropping\\n\"] + \$([\"#TA\"]).text())]                                                                                      |
|                                                                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [   [function] Drag(arg1, arg2) {]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [       \$([\"#TA\"]).text([\"Dragging\\n\"] + \$([\"#TA\"]).text())]                                                                                      |
|                                                                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [   [function] Drop(arg1) {]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                  |
| [       [if] (\$(arg1.get_target()).attr([\"id\"]) != ][\"TA\"][)] |
|                                                                                                                                                                                                                                                                                  |
| [           \$([\"#TA\"]).text([\"Drop\\n\"] + \$([\"#TA\"]).text());]                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [       ][else][]                                                                                                |
|                                                                                                                                                                                                                                                                                  |
| [           \$([\"#TA\"]).text(arg1.get_nodeText());]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [   [\</][script][\>] ]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

[] 

7.   Build and run the application.

{border="0"}  

Figure 330: TreeView---Drag and Drop (Before and After)

[]{#related-topics}

