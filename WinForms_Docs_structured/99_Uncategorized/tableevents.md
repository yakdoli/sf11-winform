---
title: tableevents.md
original_path: WinForms_Docs/99_Uncategorized/tableevents.md
created_at: 2025-08-05
---






##### Table Events {#table-events style="tab-stops: 0pt"}

[] 

The Table Style events are as follows:

[] 

**BackColorChanged**--Occurs when the value of Control\'s BackColor property changes.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [this][.groupingEngine.TableControl.BackColorChanged+=[new] [EventHandler](TableControl_BackColorChanged);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                               |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [AddHandler][ groupingEngine.TableControl.BackColorChanged, [AddressOf] TableControl_BackColorChanged] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**BackgroundImageChanged**-Occurs when the value of Control\'s BackgroundImage property changes.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [this][.groupingEngine.TableControl.BackgroundImageChanged+=[new] [EventHandler](TableControl_BackgroundImageChanged);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [AddHandler][ groupingEngine.TableControl.BackgroundImageChanged, [AddressOf] TableControl_BackgroundImageChanged] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**BindingContextChanged-**Occurs when the value of Control\'s BindingContextChanged property.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                         |
| [this][.groupingEngine.TableControl.BindingContextChanged+=[new] [EventHandler](TableControl_BindingContextChanged);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                            |
| [AddHandler][ groupingEngine.TableControl.BindingContextChanged, [AddressOf] TableControl_BindingContextChanged] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**QueryAllowDragColumn**-Occurs when the user hovers the mouse over a column header or clicks on it. In your event handler, you can determine if the selected column can be dragged.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [this][.groupingEngine.TableControl.QueryAllowDragColumn+=[new] [GridQueryAllowDragColumnEventHandler](TableControl_QueryAllowDragColumn);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                          |
| [AddHandler][ groupingEngine.TableControl.QueryAllowDragColumn, [AddressOf] TableControl_QueryAllowDragColumn] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The event handler receives an argument of type GridQueryAllowDragColumnEventArgs containing data related to this event.

 

The following **GridQueryAllowDragColumnEventArgs** properties provide information specific to this event.

[] 

[·      ]**AllowDrag**-You can disallow dragging the column when you assign it to False.

[·      ]**Column**--Get the column Name.

[·      ]**Reason**--Provide reason why the event is raised.

[] 

**QueryAllowGroupByColumn**-Occurs when the user drags a column header over the GroupDropArea. In your event handler, you can determine if the grid can be grouped by the selected column.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| [this][.groupingEngine.TableControl.QueryAllowGroupByColumn+=[new] [GridQueryAllowGroupByColumnEventHandler](TableControl_QueryAllowGroupByColumn);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [AddHandler][ groupingEngine.TableControl.QueryAllowGroupByColumn, [AddressOf] TableControl_QueryAllowGroupByColumn] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The event handler receives an argument of type GridQueryAllowGroupByColumnEventArgs containing data related to this event.

 

The following GridQueryAllowGroupByColumnEventArgs properties provide information specific to this event.

[] 

[·      ]**AllowGroupByColumn**-You can disallow grouping by the column when you assign False to it.

[·      ]**Column**--Get the column Name.

[·      ]**Reason**--Provide reason why the event is raised.

 

**QueryAllowSortColumn-**Occurs when the user hovers the mouse over a column header or clicks on it. In your event handler you can determine if the selected column can be sorted.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [this][.groupingEngine.TableControl.QueryAllowSortColumn+=[new] [GridQueryAllowSortColumnEventHandler](TableControl_QueryAllowSortColumn);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                          |
| [AddHandler][ groupingEngine.TableControl.QueryAllowSortColumn, [AddressOf] TableControl_QueryAllowSortColumn] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The event handler receives an argument of type GridQueryAllowSortColumnEventArgs containing data related to this event.

 

The following GridQueryAllowSortColumnEventArgs properties provide information specific to this event.

[] 

[·      ]**AllowSort**-You can disallow sorting by the column when you assign False to it.

[·      ]**CellClickEventArgs**-You can check the CellClickEventArgs to find out which mouse button was clicked or the exact position of the mouse pointer.

[·      ]**Column**--Get the column Name.

 

**Resize**-Occurs when control is resized.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [this][.groupingEngine.TableControl.Resize+=[new] [EventHandler](TableControl_Resize);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                          |
|                                                                                                                                                                                              |
| [AddHandler][ groupingEngine.TableControl.Resize, [AddressOf] TableControl_Resize] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**ResizingColumns** -- Occurs when the user resizes a selected range of columns.

 

The event handler receives an argument of type GridResizingColumnsEventArgs containing data related to this event.

 

The following **GridResizingColumnsEventArgs** properties provide information specific to this event.

[] 

[·      ]**Width**-The new width of the columns.

[·      ]**Reason**-The originating reason for this event.

[·      ]**SizeIndicatorBorder**-The appearance of the line that indicates the new size.

[·      ]**Point**-The mouse location.

[] 

**TextChanged**-Occurs when value of Control\'s text property changes.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [this][.groupingEngine.TableControl.TextChanged+=[new] [EventHandler](TableControl_TextChanged);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                     |
|                                                                                                                                                                                                        |
| []                                                                                                                                                    |
|                                                                                                                                                                                                        |
| [AddHandler][ groupingEngine.TableControl.TextChanged, [AddressOf] TableControl_TextChanged] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**TopRowChanged** - Occurs after the grid has been scrolled when the top row index is changed.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                             |
| [this][.groupingEngine.TableControl.TopRowChanged+=[new] Syncfusion.Windows.Forms.Grid.[GridRowColIndexChangedEventHandler](TableControl_TopRowChanged);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                                            |
| []                                                                                                                                                        |
|                                                                                                                                                                                                            |
| [AddHandler][ groupingEngine.TableControl.TopRowChanged, [AddressOf] TableControl_TopRowChanged] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The event handler receives an argument of type GridRowColIndexChangedEventArgs containing data related to this event.

 

The following GridRowColIndexChangedEventArgs properties provide information specific to this event.

[] 

[·      ]**SavedValue**-The saved Syncfusion.Windows.Forms.Grid.GridControlBase.TopRowIndex or Syncfusion.Windows.Forms.Grid.GridControlBase.LeftColIndex  value.

[·      ]**Success**-Indicates if operation was ended successfully or was aborted.

[] 

In this section, you will learn about the following events.

[] 

 

[]{#p486} 

 

###### 4.3.4.13.1.1        CurrentRecordContextChange Event {#currentrecordcontextchange-event style="tab-stops: 0pt"}

[] 

It occurs before and after the status of the current record, when it is changed.

 

The event handler receives an argument of type **CurrentRecordContextChangeEventArgs** containing data related to this event.

[] 


  ----------- --------------------------------------------------------------------------------
   Property   Description
  Action      Specifies how the current record context changes.
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Record      Specifies the affected record.
  Success     Specifies if the operation was completed successfully or failed.
  Table       Specifies the table that Grouping.Table.SelectedRecords collection belongs to.
  ----------- --------------------------------------------------------------------------------


[] 

You can handle this event and get the updated expression field value. The following code example illustrates this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [private][ [void] gridGroupingControl1_CurrentRecordContextChange([object] sender, [CurrentRecordContextChangeEventArgs] e) ] |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [   [if] (e.Action == [CurrentRecordAction].EndEditComplete)]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                      |
| [   [Console].WriteLine(e.Record);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] gridGroupingControl1_CurrentRecordContextChange([ByVal] sender [As] [Object], [ByVal] e [As] CurrentRecordContextChangeEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [    [If] e.Action = CurrentRecordAction.EndEditComplete [Then]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [        Console.WriteLine(e.Record)]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [    [End] [If]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p487} 

 

###### 4.3.4.13.1.2        GroupAdded Event {#groupadded-event style="tab-stops: 0pt"}

[] 

It occurs when a new group is added in the table after the table was categorized and when a record is changed. This event does not occur during the categorization of the table.

 

The event handler receives an argument of type **GroupEventArgs** containing data related to this event.

[] 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Group       Gets the affected group.
  ----------- -----------------------------------------------------------------------


[] 

You can handle this event to make the child groups that are not initially expanded. The following code example illustrates this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [private][ [void] gridGroupingControl1_GroupAdded([object] sender, [GroupEventArgs] e)] |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [    e.Group.IsExpanded = [false];]                                                                                                                                                   |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] gridGroupingControl1_GroupAdded([ByVal] sender [As] [Object], [ByVal] e [As] GroupEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                   |
| [e.Group.IsExpanded = [False]]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p488} 

 

###### []{#_GroupCollapsing_Event}4.3.4.13.1.3        GroupCollapsing Event {#groupcollapsing-event style="tab-stops: 0pt"}

 

It occurs before a group is collapsed.

 

The event handler receives an argument of type **GroupEventArgs** containing data related to this event.

[] 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Group       Gets the affected group.
  ----------- -----------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [this][.gridGroupingControl1.GroupCollapsing += [new] [GroupEventHandler]([this].gridGroupingControl1_GroupCollapsing);] |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [private][ [void] gridGroupingControl1_GroupCollapsing([object] sender, [GroupEventArgs] e)]                             |
|                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [    [foreach]([Record] r [in] e.Group.Records)]                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [    [Console].WriteLine([\"Collapsing event \"]+r.Info);]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [AddHandler][ gridGroupingControl1.GroupCollapsing, [AddressOf] gridGroupingControl1_GroupCollapsing]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] gridGroupingControl1_GroupCollapsing([ByVal] sender [As] [Object], [ByVal] e [As] GroupEventArgs) ] |
|                                                                                                                                                                                                                                                                                                                                         |
| [For][ [Each] r [As] Record [In] e.Group.Records]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\"Collapsing event \"]+r.Info)]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                         |
| [Next][ r]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p489} 

 

###### []{#_GroupCollapsed_Event}4.3.4.13.1.4        GroupCollapsed Event {#groupcollapsed-event style="tab-stops: 0pt"}

 

It occurs when a group is collapsed.

 

The event handler receives an argument of type **GroupEventArgs** containing data related to this event.

[] 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Group       Gets the affected group.
  ----------- -----------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [this][.gridGroupingControl1.GroupCollapsed += [new] [GroupEventHandler]([this].gridGroupingControl1_GroupCollapsed);] |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [private][ [void] gridGroupingControl1_GroupCollapsed([object] sender, [GroupEventArgs] e)]                            |
|                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [    [foreach]([Record] r [in] e.Group.Records)]                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [    [Console].WriteLine([\"Collapsed event \"]+r.Info);]                                                                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
| [AddHandler][ gridGroupingControl1.GroupCollapsed, [AddressOf] gridGroupingControl1_GroupCollapsed]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] gridGroupingControl1_GroupCollapsed([ByVal] sender [As] [Object], [ByVal] e [As] GroupEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                       |
| [For][ [Each] r [As] Record [In] e.Group.Records]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                       |
| [Console.WriteLine([\"Collapsed event \"]+r.Info)]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                       |
| [Next][ r]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p490} 

 

###### []{#_GroupExpanding_Event}4.3.4.13.1.5        GroupExpanding Event {#groupexpanding-event style="tab-stops: 0pt"}

[] 

It occurs before a group is expanded.

 

The event handler receives an argument of type **GroupEventArgs** containing the data related to this event.

[] 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Group       Gets the affected group.
  ----------- -----------------------------------------------------------------------


 

You can allow the user to expand the group, by clicking the plus/minus button. The following code example illustrates this.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [bool][ IsClickExpand = [false];]                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [private][ [void] gridGroupingControl1_GroupExpanding([object] sender, [GroupEventArgs] e)] |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [    [if] (IsClickExpand)]                                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [    IsClickExpand = [false];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [    [else]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [    e.Cancel = [true];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ IsClickExpand [As] [Boolean] = [False]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] gridGroupingControl1_GroupExpanding([ByVal] sender [As] [Object], [ByVal] e [As] GroupEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                       |
| [    [If] IsClickExpand [Then]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                       |
| [        IsClickExpand = [False]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                       |
| [    [Else]]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                       |
| [        e.Cancel = [True]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
| [    [End] [If]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p491} 

 

###### []{#_GroupExpanded_Event}4.3.4.13.1.6        GroupExpanded Event {#groupexpanded-event style="tab-stops: 0pt"}

[] 

It occurs when a group is expanded.

 

The event handler receives an argument of type **GroupEventArgs** containing data related to this event.

[] 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Group       Gets the affected group.
  ----------- -----------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.GroupExpanded += [new] GroupEventHandler([this].gridGroupingControl1_GroupExpanded);] |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [private][ [void] gridGroupingControl1_GroupExpanded([object] sender, GroupEventArgs e)]                           |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [foreach][(Record r [in] e.Group.Records)]                                                                                              |
|                                                                                                                                                                                                                                                   |
| [Console.WriteLine(\"Expanded event \"+ r.Info);]                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
| [AddHandler][ gridGroupingControl1.GroupExpanded, [AddressOf] gridGroupingControl1_GroupExpanded]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] gridGroupingControl1_GroupExpanded([ByVal] sender [As] [Object], [ByVal] e [As] GroupEventArgs) ] |
|                                                                                                                                                                                                                                                                                                                                       |
| [For][ [Each] r [As] Record [In] e.Group.Records]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                       |
| [Console.WriteLine(\"Expanded event \"+ r.Info)]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
| [Next][ r]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p492} 

 

###### 4.3.4.13.1.7        GroupRemoving Event {#groupremoving-event style="tab-stops: 0pt"}

[] 

It occurs before a group is removed after the table was categorized and when a record is changed. This event does not occur during the categorization of the table.

 

The event handler receives an argument of type **GroupEventArgs** containing data related to this event.

[] 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Group       Gets the affected group.
  ----------- -----------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [this][.gridGroupingControl1.GroupExpanded += [new] [GroupEventHandler]([this].gridGroupingControl1_GroupExpanded);] |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [private][ [void] gridGroupingControl1_GroupExpanded([object] sender, [GroupEventArgs] e)]                           |
|                                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [    [foreach]([Record] r [in] e.Group.Records)]                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [    [Console].WriteLine([\"Expanded event \"]+ r.Info);]                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [AddHandler][ gridGroupingControl1.GroupRemoving, [AddressOf] gridGroupingControl1_GroupRemoving]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] gridGroupingControl1_GroupRemoving([ByVal] sender [As] [Object], [ByVal] e [As] GroupEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                      |
| [For][ [Each] r [As] Record [In] e.Group.Records]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                      |
| [Console.WriteLine(\"Expanded event \"+ r.Info)]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [Next][ r]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p493} 

 

###### 4.3.4.13.1.8        GroupSummaryInvalidated Event {#groupsummaryinvalidated-event style="tab-stops: 0pt"}

[] 

It occurs when a summary has been marked dirty.

 

The event handler receives an argument of type **GroupEventArgs** containing data related to this event.

 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Group       Gets the affected group.
  ----------- -----------------------------------------------------------------------


 

You can handle this event to get the updated summary value in a grid. The following code example illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [private][ [void] gridGroupingControl1_GroupSummaryInvalidated([object] sender, [GroupEventArgs] e)] |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [    e.Group.ParentTable.SummariesDirty = [true];]                                                                                                                                                 |
|                                                                                                                                                                                                                                                             |
| [    [GridGroupingControl] grid = sender [as] [GridGroupingControl];]                                                                              |
|                                                                                                                                                                                                                                                             |
| [    [GridTableControl] tc = grid.GetTableControl(e.Group.ParentTableDescriptor.Name);]                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [    tc.RefreshRange([GridRangeInfo].Cell(8, 3));]                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [    [// Get the updated summary in a Text Box.]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                             |
| [    textbox1.Text = tc.Model\[8, 3\].Text;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] gridGroupingControl1_GroupSummaryInvalidated([ByVal] sender [As] [Object], [ByVal] e [As] GroupEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                |
| [    e.Group.ParentTable.SummariesDirty = [True]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                |
| [    [Dim] grid [As] GridGroupingControl = [CType](IIf([TypeOf] sender [Is] GridGroupingControl, sender, [Nothing]), GridGroupingControl)]                                   |
|                                                                                                                                                                                                                                                                                                                                                |
| [    [Dim] tc [As] GridTableControl = grid.GetTableControl(e.Group.ParentTableDescriptor.Name)]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                |
| [    tc.RefreshRange(GridRangeInfo.Cell(8, 3))]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| [    ]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                |
| [    \' Get the updated summary in a Text Box.]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                |
| [    textbox1.Text = tc.Model(8, 3).Text]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p494} 

 

###### 4.3.4.13.1.9        RecordExpanding Event {#recordexpanding-event style="tab-stops: 0pt"}

[] 

It occurs before a record with nested table is expanded.

 

The event handler receives an argument of type **RecordEventArgs** containing data related to this event.

[] 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Record      Gets the affected record.
  ----------- -----------------------------------------------------------------------


[] 

The parent records that have no child record can be prevented from expanding by handling the Table.RecordExpanding event and by setting the e.Cancel to true, when there is no child records for a parent record.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [private][ [void] Table_RecordExpanding([object] sender, [RecordEventArgs] e)]          |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [    [if](e.Record.GetRelatedChildTable([new] [RelationDescriptor]([\"ParentToChild\"])).GetRecordCount() == 0)] |
|                                                                                                                                                                                                                                                |
| [    e.Cancel = [true];]                                                                                                                                                              |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [Private][ [Sub] Table_RecordExpanding([ByVal] sender [As] [Object], [ByVal] e [As] RecordEventArgs)] |
|                                                                                                                                                                                                                                                                                                                          |
| [    [If] e.Record.GetRelatedChildTable([New] RelationDescriptor([\"ParentToChild\"])).GetRecordCount() = 0 [Then]]                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| [        e.Cancel = [True]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                          |
| [    [End] [If]]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p495} 

 

###### 4.3.4.13.1.10      RecordValueChanging Event {#recordvaluechanging-event style="tab-stops: 0pt"}

 

It occurs when a RecordFieldCell cell\'s value is changed and before Record.SetValue is returned.

 

The event handler receives an argument of type **RecordValueChangingEventArgs** containing data related to this event.

[] 


  ----------------- -----------------------------------------------------------------------
   Property         Description
  Cancel            Gets or sets a value indicating whether the event should be canceled.
  Column            Specifies the column.
  FieldDescriptor   Specifies the field descriptor.
  NewValue          Specifies the new value to save.
  Record            Specifies the record.
  ----------------- -----------------------------------------------------------------------


[] 

You can handle this event to compare the old and new values of the cell when cursor leaves the cell. The following code example illustrates this.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [private][ [void] gridGroupingControl1_RecordValueChanging([object] sender, [RecordValueChangingEventArgs] e)] |
|                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [    [Console].WriteLine([\" New Value: {0} \"], e.NewValue);]                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [    [Console].WriteLine([\" Old Value: {0} \"], e.Record.GetValue(e.Column));]                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                          |
| [Private][ [Sub] gridGroupingControl1_RecordValueChanging([ByVal] sender [As] [Object], [ByVal] e [As] RecordValueChangingEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                          |
| [    Console.WriteLine([\" New Value: {0} \"], e.NewValue)]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                          |
| [    Console.WriteLine([\" Old Value: {0} \"], e.Record.GetValue(e.Column))]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p496} 

 

###### 4.3.4.13.1.11      RecordValueChanged Event {#recordvaluechanged-event style="tab-stops: 0pt"}

 

It occurs when a RecordFieldCell cell\'s value is changed and after Record.SetValue is returned.

 

The event handler receives an argument of type **RecordValueChangedEventArgs** containing data related to this event.

[] 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Action      Specifies how the current record context changes.
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Record      Specifies the affected record.
  Success     Specifies if the operation was completed successfully or failed.
  Table       Specifies the affected table.
  ----------- -----------------------------------------------------------------------


 

You can handle this event to save the current record value. The following code example illustrates this.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [private][ [void] gridGroupingControl1_RecordValueChanged([object] sender, [RecordValueChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [    [Record] r = e.Record ;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                     |
| [    [if](e.Column != [\"Column2\"])    ]                                                                                                                                          |
|                                                                                                                                                                                                                                                                     |
| [    r.SetValue([\"Column2\"],[\"\"]); ]                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] gridGroupingControl1_RecordValueChanged([ByVal] sender [As] [Object], [ByVal] e [As] RecordValueChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                        |
| [    [Dim] r [As] Record = e.Record]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                        |
| [    [If] e.Column \<\> [\"Column2\"] [Then]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                        |
| [        r.SetValue([\"Column2\"], [\"\"])]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                        |
| [    [End] [If]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p497} 

 

###### []{#_SortingItemsInGroup_Event}4.3.4.13.1.12      SortingItemsInGroup Event {#sortingitemsingroup-event style="tab-stops: 0pt"}

[] 

It occurs before the records for a group are sorted.

 

The event handler receives an argument of type GroupEventArgs containing data related to this event.

**[]** 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Group       Gets the affected group.
  ----------- -----------------------------------------------------------------------


**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [void][ Table_SortingItemsInGroup([object] sender, [GroupEventArgs] e)] |
|                                                                                                                                                                                                           |
| [{]                                                                                                                                                                   |
|                                                                                                                                                                                                           |
| [Console][.WriteLine([\"Before Sorting the records in the group: \"]+ e.Group.Info);]     |
|                                                                                                                                                                                                           |
| [}]                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] Table_SortingItemsInGroup([ByVal] sender [As] [Object], [ByVal] e [As] GroupEventArgs)] |
|                                                                                                                                                                                                                                                                                                                             |
| [Console.WriteLine([\"Before Sorting the records in the group: \"]+ e.Group.Info)]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p498} 

 

###### []{#_SortedItemsInGroup_Event}4.3.4.13.1.13      SortedItemsInGroup Event {#sorteditemsingroup-event style="tab-stops: 0pt"}

[] 

It occurs after the records for a group are sorted.

 

The event handler receives an argument of type ** GroupEventArgs** containing data related to this event.

[] 


  ----------- -----------------------------------------------------------------------
   Property   Description
  Cancel      Gets or sets a value indicating whether the event should be canceled.
  Group       Gets the affected group.
  ----------- -----------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                                          |
| []                                                                                                                                                     |
|                                                                                                                                                                                                          |
| [void][ Table_SortedItemsInGroup([object] sender, [GroupEventArgs] e)] |
|                                                                                                                                                                                                          |
| [{]                                                                                                                                                                  |
|                                                                                                                                                                                                          |
| [Console][.WriteLine([\"After Sorting the records in the group: \"]+ e.Group.Info);]     |
|                                                                                                                                                                                                          |
| [}]                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] Table_SortedItemsInGroup([ByVal] sender [As] [Object], [ByVal] e [As] GroupEventArgs)] |
|                                                                                                                                                                                                                                                                                                                            |
| [Console.WriteLine([\"After Sorting the records in the group: \"]+ e.Group.Info)]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p499} 

 

###### 4.3.4.13.1.14      SourceListListChanged Event {#sourcelistlistchanged-event style="tab-stops: 0pt"}

 

It occurs before the table processes the System.ComponentModel.IBindingList.ListChanged event of attached source list.

 

The event handler receives an argument of type **TableListChangedEventArgs** containing data related to this event.

[] 


  ---------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   Property                          Description
  ListChangedType                    Gets the type of change.
  NavigateCurrentRecordWhenDeleted   Specifies whether the current record should be moved to the previous visible record when ItemDeleted notification is received for the current record.
  NewIndex                           Gets the index of the item affected by change.
  OldIndex                           Gets the old index of an item that has been moved.
  PropertyDescriptor                 Gets the PropertyDescriptor that was added, changed or deleted.
  ShouldIgnoreReset                  Specifies whether ListChangedType.Reset notification should be ignored.
  ShouldInvalidateCounters           Specifies whether counters need to be marked dirty when ListChanged event is handled.
  ShouldInvalidateGroupSortOrder     Specifies whether changes to the current record affect the sort order of the current group.
  ShouldInvalidateScreen             Specifies whether grid should repaint the record when changes to the record were made in the underlying data source and ListChangedType.ItemChanged notification was raised.
  ShouldInvalidateSummaries          Specifies whether summaries need to be marked dirty when ListChanged event is handled.
  ShouldReevaluateSortPosition       Specifies whether changes to the current record affects the sort order of the current group.
  ShouldResetCurrentRecord           Specifies whether current record should be reset when ItemChanged notification is received for the current record.
  ---------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

You can handle this event to retrieve the ListChangedType. The following code example illustrates this.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [private][ [void] gridGroupingControl1_SourceListListChanged([object] sender, [TableListChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [Console][.WriteLine([\"ListChangedType :\"] +e.ListChangedType.ToString() );]                                                                       |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] gridGroupingControl1_SourceListListChanged([ByVal] sender [As] [Object], [ByVal] e [As] TableListChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                         |
| [    Console.WriteLine([\"ListChangedType :\"] & e.ListChangedType.ToString())]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p500} 

 

[]{#related-topics}

