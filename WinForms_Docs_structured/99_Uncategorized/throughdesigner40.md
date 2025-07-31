---
title: throughdesigner40.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughdesigner40.md
created_at: 2025-07-03
---






#### Through Designer {#through-designer style="tab-stops: 0pt"}

[]{#p43}**** 

*** ***The docking window\'s WYSIWYG designer makes the implementation of a docking windows layout a highly intuitive process. Complex layouts can be designed by dragging-and-dropping the docking manager, without having to write a single line of code.

[] 

The following steps outline the sequence of steps involved in setting up a simple docking windows (listbox for ex) layout using the designer.

[] 

1.   Open the host form within the windows forms designer and add the controls that should be implemented as docking windows.

2.   Drag a DockingManager control from the toolbox onto the form. The docking manager is implemented as an extender provider and will add the **EnableDocking on dockingManager** property to all the child controls that are dropped in the form as shown in the image below.

[] 

{border="0"}

***[]*** 

Figure 38: EnableDocking on dockingManager property added to the Properties Grid of the ListBox Control

[] 

3.   Turn on the **EnableDocking on dockingManager** property for those controls that should be hosted as docking windows. Setting this property will immediately transform the control into a docking window by creating a dockable container and adding the control to it. The control is now a full-featured docking window that is docked to the form\'s left border, by default as in the image displayed below.

[] 

{border="0"}

***[]*** 

Figure 39: ListBox control transformed into a Docking Window

[] 

4.   DockingManager provides docking specific properties to the docked controls, which will be listed under the Syncfusion Docking category of those controls. These properties lets you specify icons for the caption, edit the caption labels, auto hide the controls and so on.

[] 

{border="0"}

[] 

Figure 40: Properties of Docked Control

[] 

5.   DockingManager comes with enormous appearance properties, whose settings will be applied to all the docked controls.

**[]** 

{border="0"}

**[]** 

Figure 41: Properties of Docked Control

**[]** 

6.   The form\'s docking layout can be set up by dragging the dock-enabled controls and redocking or floating them at the desired locations by using **DragProviderStyle** property.

[] 

{border="0"}

***[]*** 

Figure 42: Floating the ListBox control by using the DragProviderStyle property

[] 

7.   Use the AutoHideOnLoad and HiddenOnLoad extended properties for setting the autohidden and hidden dock states for the controls.

[] 

{border="0"}

[] 

Figure 43: AutoHidden Control

**[]** 

See Also

[] 

[Through Code]{.UGHyperlink}[, ]{.UGHyperlink}[Concepts and Features]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

