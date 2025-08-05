---
title: throughdesigner54.md
original_path: WinForms_Docs/99_Uncategorized/throughdesigner54.md
created_at: 2025-08-05
---






#### Through Designer {#through-designer style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Tree nodes can be added to the control at design time as follows.

[] 

1.    Create an application in Visual Studio .NET.

[] 

2.   In the designer, drag and drop a TreeViewAdv control to your form, from the toolbox.

[] 

3.   Select the TreeViewAdv control in the form. In the**[ ]**properties, click the ellipsis button of the **Nodes** property to open the NodeCollection Editor. You can also open this editor using task window or by right clicking the control and selecting Node Editor.

[] 

4.   This TreeViewAdv NodeCollection Editor can also be invoked by clicking the Node Editor option, which appears when the TreeViewAdv control is right clicked at the design time. User can also add top level nodes by clicking the Add Node option. The below image illustrates the same. The nodes added can be customized using the NodeCollection Editor.

[] 

{border="0"}

[] 

Figure 1117: \"Add Node\" Design-Time Verb

[] 

5.   Click \"Add Node\". This will add a new top-level node.

[] 

6.   The node\'s properties will be displayed in the property grid to the right. Specify a custom label for the node by changing its **text** property as shown in the below image.

[] 

{border="0"}

[] 

Figure 1118: Collection Editor Property Grid

[] 

7.   Click \"Add Node\" to add another sibling to the selected node.

[] 

8.   Click \"Add Child\" to add a child node to the selected node.

[] 

9.   Repeat steps 5 and 6 as required in the application.

[] 

10.  Click \"Remove\" to delete a selected node.

[] 

11.  To move a node to a different parent, just drag-and-drop that node over the parent or besides the desired sibling.

[] 

12.  Click \"OK\" to save changes.

 

 

 

 

[]{#related-topics}

