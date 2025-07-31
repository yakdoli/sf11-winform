---
title: dockingevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\dockingevents.md
created_at: 2025-07-03
---






#### Docking Events {#docking-events style="tab-stops: 0pt"}

 

[]{#p84}The Essential Tools DockingManager provides the functionality for creating and working with enhanced docking windows that support attaching to a host form\'s border, dragging around and docking to different edges within the form and also be dragged off the host form and floated as an individual top-level window.

 

The Essential Tools docking framework allows just about any child control on a form to be made into a fully qualified docking window. The Docking manager provides programmatic access to the interaction between these dockable windows and other complex features like multiple docking levels, nested docking, tabbed docking, tear-off tabs, autohide mode, state persistence etc., by raising several events.

 

The list of events and a detailed explanation about each of them is given in the following sections.

 


+-----------------------------------+-----------------------------------------------------------------------------------------+
| Docking Events                    | Description                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| AutoHideAnimationStart            | The AutoHideAnimationStart event occurs just before the start of an autohide animation. |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| AutoHideAnimationStop             | The AutoHideAnimationStop event occurs                                                  |
|                                   |                                                                                         |
|                                   | immediately after the end of an autohide                                                |
|                                   |                                                                                         |
|                                   | animation.                                                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| AutoHideTabContextMenu            | This event occurs when the right mouse button is clicked over a AutoHideTabControl.     |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DockMenuClick                     | This event occurs when the redock context menu item has been clicked.                   |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ControlMaximized                  | This event occurs after the control is maximized.                                       |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ControlMaximizing                 | This event occurs before the control is going to maximize.                              |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ControlMinimized                  | This event occurs after the control is minimized.                                       |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ControlRestored                   | This event occurs after the control is restored.                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DockAllow                         | The DockAllow event occurs when a docking                                               |
|                                   |                                                                                         |
|                                   | window is dragged over a potential dock target.                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DockContextMenu                   | The DockContextMenu event occurs when the                                               |
|                                   |                                                                                         |
|                                   | right mouse button is clicked over a docking                                            |
|                                   |                                                                                         |
|                                   | window\'s caption.                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DockControlActivated              | The DockControlActivated event occurs when a                                            |
|                                   |                                                                                         |
|                                   | dockable control gets activated.                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DockControlDeactivated            | The DockControlDeactivated event occurs when a                                          |
|                                   |                                                                                         |
|                                   | dockable control gets deactivated.                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DockStateChanged                  | The DockStateChanged event occurs immediately                                           |
|                                   |                                                                                         |
|                                   | after a dock operation.                                                                 |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DockStateChanging                 | The DockStateChanging event occurs just before                                          |
|                                   |                                                                                         |
|                                   | a dock operation takes place.                                                           |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DockStateUnavailable              | The DockStateUnavailable event occurs if                                                |
|                                   |                                                                                         |
|                                   | serialized information is not available for a                                           |
|                                   |                                                                                         |
|                                   | dockable control when loading a persisted dock                                          |
|                                   |                                                                                         |
|                                   | state.                                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DockVisibilityChanged             | The DockVisibilityChanged event occurs after a                                          |
|                                   |                                                                                         |
|                                   | control\'s DockVisibility state has changed.                                            |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DockVisibilityChanging            | The DockVisibilityChanging event occurs during                                          |
|                                   |                                                                                         |
|                                   | a control\'s DockVisibility state is changing.                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DragAllow                         | The DragAllow event occurs when a docking                                               |
|                                   |                                                                                         |
|                                   | window is about to be dragged.                                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DragFeedbackStart                 | The DragFeedbackStart event occurs just before                                          |
|                                   |                                                                                         |
|                                   | the start of feedback of a drag operation.                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DragFeedbackStop                  | The DragFeedbackStop event occurs immediately                                           |
|                                   |                                                                                         |
|                                   | after the end of feedback of a drag operation.                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ImageListChanged                  | Occurs when the ImageList property changes.                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| InitializeControlOnLoad           | The InitializeControlOnLoad event occurs when                                           |
|                                   |                                                                                         |
|                                   | the DockingManager is not able to locate a                                              |
|                                   |                                                                                         |
|                                   | control during a LoadDockState call.                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| NewDockStateBeginLoad             | The NewDockStateBeginLoad event occurs just                                             |
|                                   |                                                                                         |
|                                   | before a new dock state is loaded.                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| NewDockStateEndLoad               | The NewDockStateEndLoad event occurs                                                    |
|                                   |                                                                                         |
|                                   | immediately after a new dock state has been                                             |
|                                   |                                                                                         |
|                                   | loaded.                                                                                 |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ProvideGraphicsItems              | The ProvideGraphicsItems event occurs whenever                                          |
|                                   |                                                                                         |
|                                   | a dockable control\'s caption needs to be painted.                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ProvidePersistenceID              | Lets you specify a unique ID used to distinguish                                        |
|                                   |                                                                                         |
|                                   | the persistence information of different instances                                      |
|                                   |                                                                                         |
|                                   | of the Form type.                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| TransferredToManager              | The TransferredToManager event occurs after a                                           |
|                                   |                                                                                         |
|                                   | dockable control that previously belonged to some                                       |
|                                   |                                                                                         |
|                                   | other DockingManager has been transferred to the                                        |
|                                   |                                                                                         |
|                                   | docking layout hosted by this DockingManager.                                           |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| TransferringFromManager           | The TransferringFromManager event occurs when                                           |
|                                   |                                                                                         |
|                                   | a dockable control hosted by this                                                       |
|                                   |                                                                                         |
|                                   | DockingManager is about to be transferred to the                                        |
|                                   |                                                                                         |
|                                   | docking layout hosted by some other                                                     |
|                                   |                                                                                         |
|                                   | DockingManager.                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------+


More:



























