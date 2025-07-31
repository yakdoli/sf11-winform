---
title: navigationpanedropdownclickevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\navigationpanedropdownclickevent.md
created_at: 2025-07-03
---






##### NavigationPaneDropDownClick Event {#navigationpanedropdownclick-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

It occurs when the user clicks on the GroupBar control\'s Navigation Pane DropDown button. This event is applicable for the Stacked GroupBar i.e. the **StackedMode** property of the GroupBar should be set to True. The event handler receives an argument of type NavigationPaneDropDownClickEventArgs containing data related to this event.

 

The following event property is associated with the **NavigationPaneDropDownClickEventArgs**.

[] 


  --------------------- ----------------------------------------------------------------------------------------
  Member                Description
  ContextMenuProvider   Returns the menu provider object used by the GroupBar for creating it\'s context menu.
  --------------------- ----------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [private][ [void] groupBar1_NavigationPaneDropDownClick([object] sender, [NavigationPaneDropDownClickEventArgs] e)] |
|                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [  // NavigationPaneDropDownClick Event has a property called ContextMenuProvider which returns the object   ]                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [// used for creating the context menu.]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [Console][.Write([\" NavigationPaneDropDownClick Event is raised \"]);]                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [Console][.Write([\"ContextMenuProvider :\"] + e.ContextMenuProvider.ToString());]                                                                          |
|                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] groupBar1_NavigationPaneDropDownClick([ByVal] sender [As] [Object], [ByVal] e [As] NavigationPaneDropDownClickEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                               |
| [// NavigationPaneDropDownClick Event has a property called ContextMenuProvider which returns the object   ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                               |
| [// used for creating the context menu.]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Console.Write([\" NavigationPaneDropDownClick Event is raised \"])]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Console.Write([\"ContextMenuProvider :\"] + e.ContextMenuProvider.ToString())]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p624} 

 

[]{#related-topics}

