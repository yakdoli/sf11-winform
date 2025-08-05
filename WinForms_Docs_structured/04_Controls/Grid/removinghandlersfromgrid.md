---
title: removinghandlersfromgrid.md
original_path: WinForms_Docs/04_Controls/Grid/removinghandlersfromgrid.md
created_at: 2025-08-05
---








  









### Removing Handlers from Grid {#removing-handlers-from-grid style="tab-stops: 0pt"}

 

The following code snippet illustrates remvoing handlers from grid object.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| [var][ gridObj = \$find([\"Grid1\"]);] |
|                                                                                                                                                    |
| **[           gridObj.remove_OnRowHover(OnRecordHover);]**                                                     |
|                                                                                                                                                    |
| **[           gridObj.remove_OnRowSelect(OnRecordSelect);]**                                                   |
|                                                                                                                                                    |
| **[           gridObj.remove_OnDoubleClick(OnRecordDoubleClick);]**                                            |
|                                                                                                                                                    |
| **[           gridObj.remove_OnRecordsUnselectionEvent(OnRecordUnSelect);]**                                   |
|                                                                                                                                                    |
| **[           gridObj.remove_OnLoad(OnLoad);]**                                                                |
|                                                                                                                                                    |
| **[           gridObj.remove_OnActionBegin(OnBegin);]**                                                        |
|                                                                                                                                                    |
| **[           gridObj.remove_OnActionSuccess(OnSuccess);]**                                                    |
|                                                                                                                                                    |
| **[           gridObj.remove_OnActionFailure(OnFailure);]**                                                    |
|                                                                                                                                                    |
| **[           gridObj.remove_OnRowsSelected(OnRowsSelected);]**                                                |
|                                                                                                                                                    |
| **[           gridObj.remove_OnDroppingTarget(OnRecordSelect);]**                                              |
|                                                                                                                                                    |
| **[           gridObj.remove_OnDropTargetCompleted(OnDropped);]**                                              |
|                                                                                                                                                    |
| **[           gridObj.remove_OnDroponGridRowsEvent(OnGridRowDrag);]**                                          |
|                                                                                                                                                    |
| **[           gridObj.remove_OnDragonGridRowEvent(OnGridrowsDrop);]**[]    |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

