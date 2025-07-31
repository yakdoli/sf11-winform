---
title: groups.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\groups.md
created_at: 2025-07-03
---








  









## Groups {#groups style="tab-stops: 0pt"}

 

[]{#p60}Essential Diagram Silverlight provides support to group and ungroup nodes. The Grouping feature comes in handy when you want to apply the same edits to a number of objects and yet retain their individuality. All the operations performed on the group also affect the individual items in the group. However any item in the group can also be edited individually. On ungrouping, the items in the group again act as individual entities.

 

A Group is essentially just another node added, which acts as a container for other objects. Therefore a group node is referred to as the parent node, and the grouped objects are referred to as the children of the group.

 

The Group class is inherited from the Node class. Therefore all the node properties apply to a group too.

 

The following table lists the methods that are used for grouping.

[] 


  ------------------------------------- ---------------------------------------------------------------------------------------------------------------------------
  Method                                Description
  Group.AddChild(INodeGroup child)      Adds the specified INodeGroup object to the group. INodeGroup provides an interface to the nodes and the connectors.
  Group.RemoveChild(INodeGroup child)   Removes the specified INodeGroup object from the group. INodeGroup provides an interface to the nodes and the connectors.
  ------------------------------------- ---------------------------------------------------------------------------------------------------------------------------


[] 

 

More:











