---
title: groupevents1.md
original_path: WinForms_Docs/99_Uncategorized/groupevents1.md
created_at: 2025-08-05
---






##### Group Events {#group-events style="tab-stops: 0pt"}

[]{#p274}The following table lists the events that are associated with Grid Groups.

 


  ----------------- --------------------------------------------------------------------------------------------------------
  Event             Description
  GroupExpanding    This event is raised when a group is about to be expanded. This operation can be optionally canceled.
  GroupExpanded     This event is raised when a group is expanded.
  GroupCollapsing   This event is raised when a group is about to be collapsed. This operation can be optionally canceled.
  GroupCollapsed    This event is raised when a group is collapsed.
  ----------------- --------------------------------------------------------------------------------------------------------


[] 

GroupExpanding Event

 

The following code example illustrates how to handle the GroupExpanding event.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                       |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [// Subscribe to the event.]                                                                                                                                   |
|                                                                                                                                                                                                                  |
| [dataGrid.Model.Table.GroupExpanding+=[new] [GroupExpandingEventHandler](Table_GroupExpanding);]                                |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [// Handle the event.]                                                                                                                                         |
|                                                                                                                                                                                                                  |
| [void][ Table_GroupExpanding([object] sender, [GroupExpandingEventArgs] args)] |
|                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [args.Cancel = [true];]                                                                                                                                 |
|                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

GroupExpanded Event

 

The following code example illustrates how to handle the GroupExpanded event.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [// Subscribe to the event.]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| [dataGrid.Model.Table.GroupExpanded += [new] [GroupExpandedEventHandler](Table_GroupExpanded);]                                                                                            |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [// Handle the event.]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [void][ Table_GroupExpanded([object] sender, [GroupExpandedEventArgs] args)]                                                              |
|                                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [// Print the group caption text.]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [Console][.WriteLine([\"Expanded: \"]+ dataGrid.Model.Table.GroupModel.GetGroupCaptionText(([GridDataGroupItem])args.Group.Item));] |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

GroupCollapsing Event

 

The following code example illustrates how to handle the GroupCollapsing event.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                         |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [// Subscribe to the event.]                                                                                                                                     |
|                                                                                                                                                                                                                    |
| [dataGrid.Model.Table.GroupCollapsing+=[new] [GroupCollapsingEventHandler](Table_GroupCollapsing);]                               |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [// Handle the event.]                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [void][ Table_GroupCollapsing([object] sender, [GroupCollapsingEventArgs] args)] |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [args.Cancel = [true];]                                                                                                                                   |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

GroupCollapsed Event

 

The following code example illustrates how to handle the GroupCollapsed event.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [// Subscribe to the event.]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [dataGrid.Model.Table.GroupCollapsed+=[new] [GroupCollapsedEventHandler](Table_GroupCollapsed);]                                                                                            |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [// Handle the event.]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [void][ Table_GroupCollapsed([object] sender, [GroupCollapsedEventArgs] args)]                                                             |
|                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [// Print the group caption text.]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [Console][.WriteLine([\"Expanded: \"] + dataGrid.Model.Table.GroupModel.GetGroupCaptionText(([GridDataGroupItem])args.Group.Item));] |
|                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p275} 

 

[]{#related-topics}

