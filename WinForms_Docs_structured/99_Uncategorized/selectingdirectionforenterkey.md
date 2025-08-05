---
title: selectingdirectionforenterkey.md
original_path: WinForms_Docs/99_Uncategorized/selectingdirectionforenterkey.md
created_at: 2025-08-05
---








  









### Selecting Direction for ENTER key {#selecting-direction-for-enter-key style="tab-stops: 0pt"}

By default, when ENTER is pressed, the **RecordSelectionDown** action takes place. The direction of the ENTER key can be set to one of the following options: **Up**, **Down**, **Right**, and **Left**.

Include the following code snippet in the view page to set the direction when ENTER is pressed.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [Sys.Application.add_load([function] () {]                                                                                                                            |
|                                                                                                                                                                                                                                |
| [           [var] gridObj = \$find([\"OrderGrid\"]);]                                                                                          |
|                                                                                                                                                                                                                                |
| [           gridObj.set_enterKey([\"Right\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                |
| [       })]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [\</][script][\>][]                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Run the project. The grid will appear as shown below.

 

 

{border="0"}

Figure 291: Selecting Direction "Right" for ENTER Key

 

[]{#related-topics}

