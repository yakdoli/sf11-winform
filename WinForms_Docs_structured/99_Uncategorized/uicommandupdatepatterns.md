---
title: uicommandupdatepatterns.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\uicommandupdatepatterns.md
created_at: 2025-07-03
---






#### UI Command Update Patterns {#ui-command-update-patterns style="tab-stops: 0pt"}

[] 

The UI Command Update mechanism can be defined as the way in which, an application updates the state of the UI elements (BarItems in this case), as the state of the application changes.

 

Different frameworks support different ways of UI state update mechanism. Each has its own merits and demerits and each one is appropriate in some scenarios and not so in the other.

 

The **XP Menus framework**[ ]supports multiple patterns of UI Command Update mechanism, which are discussed below.

[] 

[·      ]**Supply-Push Approach**

[] 

In this approach, the state of the BarItem is changed as and when the corresponding application state changes. This is what the XP Menus framework expects you to do by default; it will not commence the[ ][UpdateUI]{.UGHyperlink}[ ]event under any circumstances.

[] 

[·      ]**Demand-Pull Approach**

**[]** 

This approach can be difficult, as it is sometimes cumbersome to keep track of state changes in the application and update the UI state appropriately.

 

So, the framework provides two other alternative ways to update the BarItem states.

[] 

Fast Updates

[] 

If updating the BarItem states is a trivial operation, use this approach, which is also how MFC does it. In this approach, the **UpdateUI**[ ]event will be called when the ParentBarItem hosting this BarItem is dropped-down, when the BarItem is hosted in a toolbar and when the application goes into an idle state or when a shortcut corresponding to this item is about to be processed. You can turn on this behavior throughout the menu structure by setting the[ ]**BarManager.UpdateUIMFCStyle**[ ]to **True**[. ]For XPToolbars and ParentBarItems that are outside the scope of a BarManager, set the **UpdateUIMFCStyle**[ ]property in those instances explicitly.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                     |
|                                                                                                                                                                    |
| **[]**                                                                                                           |
|                                                                                                                                                                    |
| [this][.mainFrameBarManager1.UpdateUIMFCStyle = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| **[]**                                                                                                         |
|                                                                                                                                                                  |
| [Me][.mainFrameBarManager1.UpdateUIMFCStyle  = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Slow Updates

[] 

If updating the BarItem states is not a trivial operation, then use this approach. In this approach, turn on the[ ]**UpdateUIOnAppIdle**[ ]property of the BarItem whose state has changed one or more times and the framework will then initiate its **UpdateUI**[ ]event the next time the application goes into an idle state.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                                         |
| **[]**                                                                                                |
|                                                                                                                                                         |
| [this][.barItem1.UpdateUIOnAppIdle = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                   |
|                                                                                                                                                      |
| **[]**                                                                                             |
|                                                                                                                                                      |
| [Me][.barItem1.UpdateUIOnAppIdle = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[UpdateUI Event]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

