---
title: creategroup.md
original_path: WinForms_Docs/99_Uncategorized/creategroup.md
created_at: 2025-08-05
---








  









### Create Group {#create-group style="tab-stops: 0pt"}

The following are the three ways to create a group in Essential Diagram WPF.

[·      ]By using Code Behind

[·      ]By using the Group Command

[·      ]By using the Context Menu

[] 

Grouping By Using Code Behind

The **Group** class enables to group nodes in Essential Diagram WPF. The **AddChild** method is used to add the elements to the group.

 

The following code example illustrates how to create a group by using code behind.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [public][ [DiagramControl] Control;]                                                                         |
|                                                                                                                                                                                                                           |
| [public][ [DiagramModel] Model;]                                                                             |
|                                                                                                                                                                                                                           |
| [public][ [DiagramView] View;]                                                                               |
|                                                                                                                                                                                                                           |
| [public][ Window1 ()]                                                                                                                |
|                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [    Control = [new] [DiagramControl] ();]                                                                                               |
|                                                                                                                                                                                                                           |
| [    Model = [new] [DiagramModel] ();]                                                                                                   |
|                                                                                                                                                                                                                           |
| [    View = [new] [DiagramView] ();]                                                                                                     |
|                                                                                                                                                                                                                           |
| [    Control.View = View;]                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| [    Control.Model = Model;]                                                                                                                                                          |
|                                                                                                                                                                                                                           |
| [    View.Bounds = [new] [Thickness](0, 0, 1000, 1000);]                                                                                 |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [    [Node] n = [new] [Node]([Guid].NewGuid(), [\"Start\"]);]    |
|                                                                                                                                                                                                                           |
| [    n.Shape = [Shapes].FlowChart_Card;]                                                                                                                      |
|                                                                                                                                                                                                                           |
| [    n.Level = 1;]                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [    n.OffsetX = 150;]                                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [    n.OffsetY = 25;]                                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [    n.Width = 150;]                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [    n.Height = 75;]                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [    [Node] n1 = [new] [Node]([Guid].NewGuid(), [\"End\"]);]     |
|                                                                                                                                                                                                                           |
| [    n1.Shape = [Shapes].RoundedRectangle;]                                                                                                                   |
|                                                                                                                                                                                                                           |
| [    n1.Level = 1;]                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [    n1.OffsetX = 350;]                                                                                                                                                               |
|                                                                                                                                                                                                                           |
| [    n1.OffsetY = 325;]                                                                                                                                                               |
|                                                                                                                                                                                                                           |
| [    n1.Width = 100;]                                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [    n1.Height = 75;]                                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [    Model.Nodes.Add(n);]                                                                                                                                                             |
|                                                                                                                                                                                                                           |
| [    Model.Nodes.Add(n1);]                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [    [Group] g = [new] [Group]([Guid].NewGuid(), [\"group1\"]);] |
|                                                                                                                                                                                                                           |
| [    g.AddChild(n);]                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [    g.AddChild(n1);]                                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [    Model.Nodes.Add(g);]                                                                                                                                                             |
|                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [Public][ Control [As] [DiagramControl]]                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| [Public][ Model [As] [DiagramModel]]                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [Public][ View [As] [DiagramView]]                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [\'INSTANT VB WARNING: The following constructor is declared outside of its associated class:][]                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [        ]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [        [\'ORIGINAL LINE: public Window1 ()]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [        [Public] [Sub] [New]()]                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [            Control = [New] [DiagramControl]()]                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [            Model = [New] [DiagramModel]()]                                                                                                                                                |
|                                                                                                                                                                                                                                                                              |
| [            View = [New] [DiagramView]()]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [            Control.View = View]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| [            Control.Model = Model]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [            View.Bounds = [New] [Thickness](0, 0, 1000, 1000)]                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [            [Dim] n [As] [New] [Node]([Guid].NewGuid(), [\"Start\"])]                            |
|                                                                                                                                                                                                                                                                              |
| [            n.Shape = [Shapes].FlowChart_Card]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [            n.Level = 1]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                              |
| [            n.OffsetX = 150]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [            n.OffsetY = 25]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| [            n.Width = 150]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [            n.Height = 75]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [            ]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                              |
| [            Dim][ n1 [As] [New] [Node]([Guid].NewGuid(), [\"End\"])] |
|                                                                                                                                                                                                                                                                              |
| [            n1.Shape = [Shapes].RoundedRectangle]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [            n1.Level = 1]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [            n1.OffsetX = 350]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                              |
| [            n1.OffsetY = 325]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                              |
| [            n1.Width = 100]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| [            n1.Height = 75]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| [            Model.Nodes.Add(n)]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [            Model.Nodes.Add(n1)]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [            [Dim] g [As] [New] [Group]([Guid].NewGuid(), [\"group1\"])]                          |
|                                                                                                                                                                                                                                                                              |
| [            g.AddChild(n)]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [            g.AddChild(n1)]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| [            Model.Nodes.Add(g)]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [        [End] [Sub]][]                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates a group of two nodes created by using code behind.

[] 

{border="0"}

Figure 99: Group of Two Nodes[]

[] 

Grouping By Using the Group Command

The **Group** command is used to group two or more objects.

 

The following code example illustrates how to group objects by using the Group command.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [DiagramCommandManager][.Group.Execute(diagramView.Page, diagramView);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [DiagramCommandManager][.Group.Execute(diagramView.Page, diagramView)][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following steps illustrate how to create a group by using the Group command.

[] 

1.   Select the objects to be grouped.

[] 

{border="0"}

Figure 100: Selection of Objects to be Grouped[]

[] 

{border="0"}

Figure 101: Selected Objects[]

[] 

2.   Invoke the Group command. This creates a group.

[] 

The new group is indicated by the selection rectangle which is displayed surrounding the objects in the group.

 

{border="0"}

Figure 102: Grouped Objects inside the Selection Rectangle[]

**[]** 

Grouping By Using the Context Menu

You can also invoke the **Group** command by using the context menu which is displayed on right-clicking a particular Node or Line Connector.

[] 

{border="0"}

Figure 103: Grouping By Using the Context Menu[]

[] 


{border="0"}Note: The Group command is enabled only when two or more objects are selected.


[] 

See Also

 Refer Concepts and Features -\> Nodes -\> Node Resize -\> Resize Single Node on Multiple Selection[]

 

[]{#related-topics}

