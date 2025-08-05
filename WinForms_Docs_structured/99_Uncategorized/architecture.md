---
title: architecture.md
original_path: WinForms_Docs/99_Uncategorized/architecture.md
created_at: 2025-08-05
---








  









### Architecture {#architecture style="tab-stops: 0pt"}

[] 

The Grid Tree control derives from the WPF ContentControl, which allows it to support a ControlTemplate to define its content. By default, its content includes a Border object, which contains a **ScrollViewer** object that contains a **GridControlImpl** object. **GridControlImpl** is a **GridControlBase** derived class that provides the 'multi-column grid' functionality to the Grid Tree control.

 

For each node in the tree, there is a **GridTreeNode** object that holds the information of the node such as the underlying data item, whether the node is expanded, etc. The GridTreeNodes collection can be accessed by the **GridTreeControl.InternalGrid.Nodes** collection. InternalGrid is the **GridTreeControlImpl** object associated with the Grid Tree control.

 

The following screen shot illustrates the Grid Tree control architecture.

 

{border="0"}

[] 

Figure 187: GridTreeControl Architecture

[] 

Accessing the Underlying Grid control

[] 

The Grid Tree control is a ContentControl derived class. To get its grid-like behavior, the Grid Tree control has a Grid control derived property named **InternalGrid**. InternalGrid is a **GridTreeControlImpl** class, which is derived from the Grid control. The GridTreeControlImpl is a virtual Grid control, which uses the virtual events to bind to the **GridTreeControl.Nodes** collection. So, to access the underlying Grid control associated with the Grid Tree control, you can use the **GridTreeControl.InternalGrid** property.

 

All the properties exposed in Grid Tree control (with the exception of Internal Grid) are mirrored in GridTreeControlImpl. There are methods and properties exposed on the Internal Grid that are not exposed on the Grid Tree control itself. In particular, to control the look of the Expand cell, you need to use the Internal Grid as discussed below. The Internal Grid has many protected methods that provide access to the tree-like functionality. So, deriving GridTreeControlImpl gives you access to this functionality if you need to use it for any reason.

[]{#p269} 

[]{#related-topics}

