---
title: addinghandlersthroughgridclientobject.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\addinghandlersthroughgridclientobject.md
created_at: 2025-07-03
---








  









### Adding Handlers through Grid Client Object: {#adding-handlers-through-grid-client-object style="tab-stops: 0pt"}

 

The following code snippet illustrates adding handlers in client script.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                 |
|                                                                                                                                                        |
| [    var][ gridObj = \$find([\"Grid1\"]);] |
|                                                                                                                                                        |
| **[           gridObj.add_OnRowHover(OnRecordHover);]**                                                            |
|                                                                                                                                                        |
| **[           gridObj.add_OnRowSelect(OnRecordSelect);]**                                                          |
|                                                                                                                                                        |
| **[           gridObj.add_OnDoubleClick(OnRecordDoubleClick);]**                                                   |
|                                                                                                                                                        |
| **[           gridObj.add_OnRecordsUnselectionEvent(OnRecordUnSelect);]**                                          |
|                                                                                                                                                        |
| **[           gridObj.add_OnLoad(OnLoad);           ]**                                                            |
|                                                                                                                                                        |
| **[           gridObj.add_OnActionBegin(OnBegin);]**                                                               |
|                                                                                                                                                        |
| **[           gridObj.add_OnActionSuccess(OnSuccess);]**                                                           |
|                                                                                                                                                        |
| **[           gridObj.add_OnActionFailure(OnFailure);]**                                                           |
|                                                                                                                                                        |
| **[           gridObj.add_OnRowsSelected(OnRowsSelected);]**                                                       |
|                                                                                                                                                        |
| **[           gridObj.add_OnDroppingTarget(OnRecordSelect);]**                                                     |
|                                                                                                                                                        |
| **[           gridObj.add_OnDropTargetCompleted(OnDropped);]**                                                     |
|                                                                                                                                                        |
| **[           gridObj.add_OnDroponGridRowsEvent(OnGridRowDrag);]**                                                 |
|                                                                                                                                                        |
| **[           gridObj.add_OnDragonGridRowEvent(OnGridrowsDrop);]**[]           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

