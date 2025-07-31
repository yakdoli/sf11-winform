---
title: nodelabel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nodelabel.md
created_at: 2025-07-03
---








  









### Node Label {#node-label style="tab-stops: 0pt"}

[A label is a single line or multiple lines of text that are displayed over a node. This label can be used to display text on the node that can be edited at run time. Several properties have been provided to change the alignment and appearance settings of the label. ]

[] 

  Property                                                                                  Description                                                                                                                                                                          Type                                  Data Type
  ----------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------- -----------------------------------------------
  [IsLabelEditable][]   [Gets or sets a value indicating whether the node\'s label can be edited. The default value is set to True.][]   [Server side]   [Binary, true or false]
  [Label]                                                             [Gets or sets the node label.]                                                                                                                                 [Server side]   [string]
  [LabelVisibility]                                                   [Gets or sets the label visibility.]                                                                                                                           [Server side]   [Binary, true or false]

 

Set a label for the node using the **Label** property. The default value is an empty string. By default, the label is displayed at the center position. A label\'s visibility can be changed using the **LabelVisibility** property. The default value is **true**.

More:







