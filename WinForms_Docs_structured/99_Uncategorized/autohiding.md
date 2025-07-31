---
title: autohiding.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\autohiding.md
created_at: 2025-07-03
---






##### AutoHiding {#autohiding style="tab-stops: 0pt"}

[] 

Docking manager provides auto hide facility to the docked control. When the auto hide button (looks like a bell) is clicked, the docked controls will be hidden, and will be placed along the side of the container control on which it was placed. When mouse is moved over it, the auto hidden control will be displayed and the control will restore its appearance when the auto hidden button is clicked again.

 

The below image displays an autohidden docked control.

[] 

{border="0"}

[] 

Figure 52: AutoHidden Docked Control

**[]** 

The below properties controls the autohiding feature of the docked controls.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------+
| DockingManager Property           | Description                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| AutoHideActiveControl             | Gets or sets a value indicating whether to slide back selected auto hidden control.        |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| AutoHideInterval                  | Specifies the time interval for showing or hiding an autohidden control.                   |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| AutoHideSelectionStyle            | Specifies the selection style for the autohidden windows. The styles are,                  |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   | *MouseHover* - Allows the user to select an autohidden tab by mouse hovering over the tab. |
|                                   |                                                                                            |
|                                   | *Click* - Allows the user to select the autohidden tab by clicking on the tab.             |
+-----------------------------------+--------------------------------------------------------------------------------------------+


**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [this][.dockingManager1.AutoHideActiveControl = [true];]                                  |
|                                                                                                                                                                                                     |
| [this][.dockingManager1.AutoHideInterval = 500;]                                                               |
|                                                                                                                                                                                                     |
| [this][.dockingManager1.AutoHideSelectionStyle = Syncfusion.Windows.Forms.Tools.AutoHideSelectionStyle.Click;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                               |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [Me][.dockingManager1.AutoHideActiveControl = [True]]                                  |
|                                                                                                                                                                                                  |
| [Me][.dockingManager1.AutoHideInterval = 500]                                                               |
|                                                                                                                                                                                                  |
| [Me][.DockingManager1.AutoHideSelectionStyle = Syncfusion.Windows.Forms.Tools.AutoHideSelectionStyle.Click] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Displaying Full Caption In AutoHide Mode

[] 

Create a docked window with two listbox. Dock the controls. Tab the controls and set the **FullCaptionInAutoHideMode** property. Setting this property to true, will display the full caption text in the auto hidden tabgroup\'s page. It displays full caption within the application if necessary with a scrollbar, so that end user can scroll and view the hidden tab\'s full caption.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                          |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [this][.dockingManager1.FullCaptionsInAutoHideMode = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                   |
|                                                                                                                                                                      |
| []                                                                                                                 |
|                                                                                                                                                                      |
| [Me][.dockingManager1.FullCaptionsInAutoHideMode = [True]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 53: AutoHidden Tabs with truncated Caption Text

[] 

{border="0"}

**[]** 

Figure 54: AutoHidden Tabs with full Caption Display

**[]** 

Animation in Auto Hiding is discussed in Auto Hide Animation Speed topic and Dragging Autohidden tabs topic discusses how to drag the autohidden tabs.

[] 

See Also

[] 

[Context Menu]{.UGHyperlink}[, ]{.UGHyperlink}[Animation Events]{.UGHyperlink}[, ]{.UGHyperlink}[AutoHide TabContextMenu Event]{.UGHyperlink}[, ]{.UGHyperlink}[How to autohide a control when an application loads]{.UGHyperlink}[]{.UGHyperlink}

###### []{#_Auto_Hide_Animation}3.2.3.1.4.1 Auto Hide Animation Speed {#auto-hide-animation-speed style="tab-stops: 0pt"}

[]{#p51}[] 

DockingPanel allows you to change the speed at which your docking panes are displayed or auto hidden. You can easily change the delay of the auto hide windows as fast or as slow as you want, so that your window will hide / show at the perfect speed.

 

The speed of animation can be controlled by **AnimationSpeed** and **AnimationStep** Property.

 

AnimationSpeed property of the DockingManager indicates the speed of animation during auto hide or the timer interval in milli secs. AnimationStep indicates the step value for the animation. It is common to all the docked control. AnimationStep property can be implemented using the code below.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [//arg.Bounds give the bounds of the autohidden control as a rectangle object. ]                                                                                    |
|                                                                                                                                                                                                                       |
| [DockingManager][.AnimationStep = 1000;  ][//(arg.Bounds.Width)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [\'arg.Bounds give the bounds of the autohidden control as a rectangle object. ]                                                                                    |
|                                                                                                                                                                                                                       |
| [DockingManager][.AnimationStep = 1000;  ][\'(arg.Bounds.Width)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note: For a control to show animation in autohide mode, the animation step value should be more than the width of the particular hidden control.


###### []{#p52}3.2.3.1.4.2 Context Menu for AutoHidden Tabs {#context-menu-for-autohidden-tabs style="tab-stops: 0pt"}

[] 

This is discussed in Context Menu topic.

###### []{#p53}[]{#_Dragging_Autohidden_tabs}3.2.3.1.4.3 Dragging Autohidden tabs {#dragging-autohidden-tabs style="tab-stops: 0pt"}

[] 

The docked controls that are autohidden, can be dragged with their tabs, and can be docked or set to floating by setting **EnableDragAutoHiddenTabs** property to true.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [this][.dockingManager1.EnableDragAutoHiddenTabs = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [Me][.dockingManager1.EnableDragAutoHiddenTabs = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

