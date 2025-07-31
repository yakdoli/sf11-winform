---
title: creatingagroup.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingagroup.md
created_at: 2025-07-03
---








  









### Creating a Group {#creating-a-group style="tab-stops: 0pt"}

[] 

There are three ways to create a group in Essential Diagram Silverlight. You can create a group:

[] 

[·      ]Using Code Behind

[·      ]Using the Group Method

[] 

Grouping By Using Code Behind

[] 

The **Group** class enables to group nodes in Essential Diagram Silverlight. The **AddChild** method is used to add the elements to the group.

 

The following code example illustrates the creation of a group by using code behind.

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
| [public][ MainPage ()]                                                                                                               |
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

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [Public][ Control [As] [DiagramControl]]                                                                      |
|                                                                                                                                                                                                                                                 |
| [Public][ Model [As] [DiagramModel]]                                                                          |
|                                                                                                                                                                                                                                                 |
| [Public][ View [As] [DiagramView]]                                                                            |
|                                                                                                                                                                                                                                                 |
| [    [\'INSTANT VB WARNING: The following constructor is declared outside of its associated class:]]                                                                                  |
|                                                                                                                                                                                                                                                 |
| [    [\'ORIGINAL LINE: public MainPage ()]]                                                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [    [Public] [Sub] [New]()]                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [        Control = [New] [DiagramControl]()]                                                                                                                   |
|                                                                                                                                                                                                                                                 |
| [        Model = [New] [DiagramModel]()]                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [        View = [New] [DiagramView]()]                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        Control.View = View]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [        Control.Model = Model]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [        View.Bounds = [New] [Thickness](0, 0, 1000, 1000)]                                                                                                    |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [Dim] n [As] [New] [Node]([Guid].NewGuid(), [\"Start\"])]   |
|                                                                                                                                                                                                                                                 |
| [        n.Shape = [Shapes].FlowChart_Card]                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        n.Level = 1]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [        n.OffsetX = 150]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                 |
| [        n.OffsetY = 25]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [        n.Width = 150]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        n.Height = 75]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        [Dim] n1 [As] [New] [Node]([Guid].NewGuid(), [\"End\"])]    |
|                                                                                                                                                                                                                                                 |
| [        n1.Shape = [Shapes].RoundedRectangle]                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [        n1.Level = 1]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [        n1.OffsetX = 350]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        n1.OffsetY = 325]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        n1.Width = 100]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [        n1.Height = 75]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [        Model.Nodes.Add(n)]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [        Model.Nodes.Add(n1)]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [Dim] g [As] [New] [Group]([Guid].NewGuid(), [\"group1\"])] |
|                                                                                                                                                                                                                                                 |
| [        g.AddChild(n)]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        g.AddChild(n1)]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [        Model.Nodes.Add(g)]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [    [End] [Sub]][]                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates a group of two nodes created by using Code Behind.

[] 

{border="0"}

Figure 77: Group of Two Nodes**[]**

[] 

Grouping By Using the Group Command

The Group command is used to group two or more objects.

The following code example shows the grouping of objects using the Group command:

[] 

+-----------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                |
|                                                                                               |
| []                                          |
|                                                                                               |
| [diagramControl.Group.Execute(diagramView);] |
+-----------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                     |
|                                                                                                                                                    |
| []                                                                                               |
|                                                                                                                                                    |
| [diagramControl.Group.Execute(diagramView)][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The steps to create a group by using the Group command are as follows:

1.   Select the objects to be grouped.

{border="0"}

Figure 78: Selection of Objects to be Grouped[]

{border="0"}

Figure 79: Selected Objects

[] 

2.   Call the Group command. This creates a group.  

The new group is indicated by the selection rectangle, which is displayed around the objects in the group.

{border="0"}

Figure 80: Grouped Objects inside the Selection Rectangle[]

Selection in a Group

You can select a group by clicking any one of its children. Clicking consecutively on a child object selects the parent group in the order of its creation. Similarly, clicking consecutively on a child object selects the inner groups and eventually the object itself, and the cycle continues.

An object can belong to multiple groups and groups may have multiple subgroups.

The steps to select an object that has two groups are as follows:

1.   Click the brown node, to select the outer group.

{border="0"}

Figure 81: Outer Group Selected[]

2.   Click the brown node, to select the inner group of which it is a part.

{border="0"}

Figure 82: Inner Group Selected[]

3.   Click the brown node, to select the child after all its groups have been traversed.

{border="0"}

Figure 83: Selecting the Child Node Again

[]{#p62} 

[]{#related-topics}

