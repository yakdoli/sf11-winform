---
title: addinghandlersthroughgridpropertiesmodel.md
original_path: WinForms_Docs/04_Controls/Grid/addinghandlersthroughgridpropertiesmodel.md
created_at: 2025-08-05
---








  









### Adding Handlers through GridPropertiesModel {#adding-handlers-through-gridpropertiesmodel style="tab-stops: 0pt"}

 

The following code snippet illustrates adding handlers through **GridPropertiesModel**.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [GridPropertiesModel][\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [                DataSource = [new] [NorthwindDataContext]().Orders,]                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [                Caption=[\"Orders\"],]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [                AllowPaging=[true],]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [                AllowSorting=[true],]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [                AllowFiltering=[true],]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [                AutoFormat=[Skins].Sandune,]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                              |
| [                **ClientSideRecordHoverEvent=[\"OnRecordHover\"],**]                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| **[                ClientSideRecordSelectionEvent=[\"OnRecordSelect\"],]**                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| **[                ClientSideRecordsUnselectionEvent = [\"OnRecordUnSelect\"],]**                                                                                                                                |
|                                                                                                                                                                                                                                                                              |
| **[                ClientSideDoubleClickEvent = [\"OnRecordDoubleClick\"],]**                                                                                                                                    |
|                                                                                                                                                                                                                                                                              |
| **[                OnActionBegin = [\"OnBegin\"],]**                                                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| **[                OnActionFailure = [\"OnFailure\"],]**                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| **[                OnActionSuccess = [\"OnSuccess\"],]**                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| **[                OnLoad = [\"OnLoad\"],]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| **[                OnRowDragStarted = [\"OnRowsSelected\"],]**                                                                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| **[                OnRowDropped = [\"OnDropped\"],]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| **[                OnRowDropping = [\"OnDropping\"],]**                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| **[                OnGridRowDragEvent = [\"OnGridRowDrag\"],]**                                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| **[                OnGridRowsDropEvent = [\"OnGridrowsDrop\"]]**                                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

