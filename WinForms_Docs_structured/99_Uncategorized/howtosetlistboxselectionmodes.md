---
title: howtosetlistboxselectionmodes.md
original_path: WinForms_Docs/99_Uncategorized/howtosetlistboxselectionmodes.md
created_at: 2025-08-05
---






#### How to set ListBoxSelectionModes {#how-to-set-listboxselectionmodes style="tab-stops: 0pt"}

[] 

To set the ListBoxSelectionModes property that determines the selection behavior, use the following code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| []                                                                                                                                |
|                                                                                                                                                                                     |
| [//Selecting Single record]                                                                                                       |
|                                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.One;]           |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [//Selecting MultiRecords]                                                                                                        |
|                                                                                                                                                                                     |
| [ [this].gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiSimple;]                              |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [//Selecting MultiExtendedRecords]                                                                                                |
|                                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiExtended;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [\'Selecting Single record]                                                                                                    |
|                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.One]           |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [\'Selecting MultiRecords]                                                                                                     |
|                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiSimple]   |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [\'Selecting MultiExtendedRecords]                                                                                             |
|                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiExtended] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p692} 

 

[]{#related-topics}

