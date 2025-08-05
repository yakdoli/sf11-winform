---
title: sortcolumnchangingcommand.md
original_path: WinForms_Docs/99_Uncategorized/sortcolumnchangingcommand.md
created_at: 2025-08-05
---






##### SortColumnChangingCommand {#sortcolumnchangingcommand style="tab-stops: 0pt"}

SortColumnChangingCommand allows customizing the sort columns at run time and this command get hooked before the column is sorted. SortColumnsChanging event accepts an argument of type GridDataSortColumnsChangingEventArgs. The GridDataSortColumnsChangingEventArgs contains the following customization properties. Now you can make use of this

  ------------------------------- ----------------------------------------------------------------------------------------------
  Property                        Description
  AddedItems                      Gives the Collection of GridDataSortColumns that are newly added to the GridDataControl.
  RemovedItems                    Gives the Collection of GridDataSortColumns that are removed from the GridDataControl.
  NotifyCollectionChangedAction   Gives the Action that are going to perform in the SortColumns Collection in GridDataControl.
  ------------------------------- ----------------------------------------------------------------------------------------------

 

Properties

Table 45: Property Table


  --------------------------- -------------------------------------------------------------------------------- --------------------- ----------- -----------------
  Property                    Description                                                                      Type                  Data Type   Reference links
  QueryCellInfoCommand        Gets or sets the command to invoke when QueryCellInfo event is triggered.        Dependency Property   ICommand     
  SortColumnChangingCommand   Gets or sets the command to invoke when SortColumnChanging event is triggered.   Dependency Property   ICommand     
  --------------------------- -------------------------------------------------------------------------------- --------------------- ----------- -----------------



 


[]{#related-topics}

