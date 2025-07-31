---
title: tablesforpropertiesm3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tablesforpropertiesm3.md
created_at: 2025-07-03
---








  





### Tables for Properties, Methods, and Events {#tables-for-properties-methods-and-events style="TEXT-ALIGN: justify; tab-stops: 0pt"}

Properties

Table 9: FilterBar Support Table

  ---------------------------------- -------------------------------------------------------------------------------------------------- ------------------------------------------ ------------------ ------------------------------------------
  Property                           Description                                                                                        Data Type                                  Default Value      Class Name
  PivotControl                       Gets or sets the PivotAnalysis (IPivotControl) control.                                            IPivotControl                              null                
  CustomSummaryBaseCollection        Gets or sets the CustomSummaryBaseCollection to use in the Pivot Computation Information dialog.   Enum                                       Count              SummaryType
  ShowDisplayFieldsOnly              Gets or sets a value indicating whether to show only DisplayFields.                                bool                                       false               
  PivotTableFieldList                Gets or sets the PivotTableField ListBox.                                                          ListBox                                    ListBox            ListBox
  PivotCalculationList               Gets or sets the PivotCalculation ListBox.                                                         ListBox                                    ListBox            ListBox
  PivotColumnList                    Gets or sets the PivotColumn ListBox.                                                              ListBox                                    ListBox            ListBox
  PivotRowList                       Gets or sets the PivotRow ListBox.                                                                 ListBox                                    ListBox            ListBox
  FilterList                         Gets or sets the Filters Listbox.                                                                  ListBox                                    ListBox            ListBox
  ShowCalculationsAsColumnCheckBox   Gets or sets the ShowCalculationAsColumn CheckBox.                                                 Checkbox                                   Checkbox (true)    Checkbox
  DeferLayoutUpdateCheckBox          Gets or sets the DeferLayoutUpdate check box.                                                      Checkbox                                   Checkbox (false)   Checkbox
  DeferLayoutUpdateButton            Gets or sets the DeferLayoutUpdate button.                                                         Button                                     Button             Button
  Filters                            Gets or sets the filters collection.                                                               ObservableCollection\<FilterExpression\>   null               ObservableCollection\<FilterExpression\>
  PivotTableFields                   Gets or sets the PivotTableFields.                                                                 ObservableCollection\<PivotTableField\>    null               ObservableCollection\<PivotTableField\>
  ---------------------------------- -------------------------------------------------------------------------------------------------- ------------------------------------------ ------------------ ------------------------------------------

[]{#_Tokens_to_filter} 

Events

Table 10: Pivot Schema Designer Events Table

  ---------------- ------------------------------------------------------------------- ----------- ---------------
  Events           Description                                                         Data Type   Default Value
  CommandExecute   Raises whenever a command is executed in the PivotSchemaDesigner.   Event       null
  ---------------- ------------------------------------------------------------------- ----------- ---------------

[] 

[]{#related-topics}

