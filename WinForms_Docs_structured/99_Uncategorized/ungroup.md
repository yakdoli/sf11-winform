---
title: ungroup.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\ungroup.md
created_at: 2025-07-03
---








  









### Ungroup {#ungroup style="tab-stops: 0pt"}

[] 

Ungrouping a group deletes the group and removes all the child elements from the group. Once a group is ungrouped, the child elements behave as individual entities.

 

There are three ways to ungroup a group in Essential Diagram Silverlight. You can ungroup a group:

[] 

[·      ]By using Code Behind

[·      ]By using the Ungroup Method

[] 

By Using Code Behind

**[]** 

The **RemoveChild** method is used to remove elements from a group.

 

For example, the following code illustrates the removal of node n from a group by using code behind.

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
| [    Control = [new] [DiagramControl]();]                                                                                                |
|                                                                                                                                                                                                                           |
| [    Model = [new] [DiagramModel]();]                                                                                                    |
|                                                                                                                                                                                                                           |
| [    View = [new] [DiagramView]();]                                                                                                      |
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
| [    n.Shape = [Shapes].FlowChart_Start;]                                                                                                                     |
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
| [    n1.Shape = [Shapes].FlowChart_Start;]                                                                                                                    |
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
| [    g.RemoveChild(n);]                                                                                                                                                               |
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
| [        n.Shape = [Shapes].FlowChart_Start]                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [        n.Level = 1]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [        n.OffsetX = 150]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                 |
| [        n.OffsetY = 25]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [        n.Width = 150]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        n.Height = 75]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        [Dim] n1 [As] [New] [Node]([Guid].NewGuid(), [\"End\"])]    |
|                                                                                                                                                                                                                                                 |
| [        n1.Shape = [Shapes].FlowChart_Start]                                                                                                                                       |
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
| [        g.RemoveChild(n)]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [    [End] [Sub]][]                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates a group of two nodes created by using Code Behind.

[] 

By Using the Ungroup Command

**[]** 

The **Ungroup** command is used to ungroup two or more objects.

 

The following code example describes the ungrouping of objects by using the Ungroup command.

[] 

+-------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                  |
|                                                                                                 |
| **[]**                                        |
|                                                                                                 |
| [diagramControl.UnGroup.Execute(diagramView);] |
+-------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                       |
|                                                                                                                                      |
| **[]**                                                                             |
|                                                                                                                                      |
| [diagramControl.UnGroup.Execute(diagramView)][] |
+--------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following steps describe the ungrouping of a group using the Ungroup command.

[] 

1.   Select the group to be ungrouped.

[] 

{border="0"}

Figure 91: Selecting a Group**[]**

**[]** 

2.   Call the Ungroup command. This ungroups the nodes.

[] 

As soon as the group is ungrouped, the selection rectangle disappears indicating that the group has been ungrouped.

[] 

{border="0"}

Figure 92: Objects Ungrouped**[]**

[] 

[]{#related-topics}

