---
title: showhidecolumns.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\showhidecolumns.md
created_at: 2025-07-03
---








  









### Show / Hide Columns {#show-hide-columns style="tab-stops: 0pt"}

[] 

This section deals with controlling the visibility of the columns in the GridGroupingControl. This can be done either on the server-side or client-side.

[] 

Server-Side Show / Hide Column

[] 

[Through Designer]

[] 

As discussed earlier, the columns bound to the GridGroupingControl will be present in VisibleColumns Collection. Thus, in order to hide a particular column, you have to remove it from the VisibleColumns Collection.

[] 

{border="0"}

Figure 54

[] 

**GridVisibleColumnDescriptor** Collection Editor can be accessed using the **VisibleColumns** property of the TableDescriptor.

[] 

Through Code

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [// Hide]                                                                                                                                       |
|                                                                                                                                                                                                   |
| [this][.GridGroupingControl1.TableDescriptor.VisibleColumns.Remove([\"Country\"]); ] |
|                                                                                                                                                                                                   |
| [// Show]                                                                                                                                       |
|                                                                                                                                                                                                   |
| [this][.GridGroupingControl1.TableDescriptor.VisibleColumns.Add([\"Country\"]); ]    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                           |
|                                                                                                                                                                                               |
| [\' Hide]                                                                                                                                   |
|                                                                                                                                                                                               |
| [Me][.GridGroupingControl1.TableDescriptor.VisibleColumns.Remove([\"Country\"]) ] |
|                                                                                                                                                                                               |
| [\' Unhide]                                                                                                                                 |
|                                                                                                                                                                                               |
| [Me][.GridGroupingControl1.TableDescriptor.VisibleColumns.Add([\"Country\"])]     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Client-Side Show / Hide Column

[] 

On the client-side, columns can be shown or hidden using the following APIs.

[] 

[·      ]ShowColumn(columnindex)

[·      ]HideColumn(columnindex)

[] 

The following code example illustrates this.

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[JScript\]]**                                                        |
|                                                                                                                            |
| []                                                                       |
|                                                                                                                            |
| [var gridTable = GetEGridTable( \$get(\'\<%= GridGroupingControl1.ClientID %\>\') ); ] |
|                                                                                                                            |
| [gridTable.HideColumn( val );]                                                         |
|                                                                                                                            |
| [gridTable.ShowColumn( val );]                                                         |
+----------------------------------------------------------------------------------------------------------------------------+

[]{#p42} 

[]{#related-topics}

