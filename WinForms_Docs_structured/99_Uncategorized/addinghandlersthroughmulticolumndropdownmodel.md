---
title: addinghandlersthroughmulticolumndropdownmodel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addinghandlersthroughmulticolumndropdownmodel.md
created_at: 2025-07-03
---






#### Adding Handlers through MultiColumnDropDownModel {#adding-handlers-through-multicolumndropdownmodel style="tab-stops: 0pt"}

 

Configure the **MultiColumnDropDownModel** as shown below to add the handlers.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [// Create instance to MultiColumnDropDown model and assign properties.][]                                |
|                                                                                                                                                                                                 |
| [            [MultiColumnDropDownModel] dropdown = [new] [MultiColumnDropDownModel]()] |
|                                                                                                                                                                                                 |
| [            {]                                                                                                                                             |
|                                                                                                                                                                                                 |
| [                Datasource = [new] [StudentDataContext]().JSONStudent.Skip(0).Take(30).ToList(),]             |
|                                                                                                                                                                                                 |
| [                Text = [\"\--Select\--\"],]                                                                                        |
|                                                                                                                                                                                                 |
| [                DisplayExpression = [new] [int]\[3\] { 2, 3, 5 },]                                               |
|                                                                                                                                                                                                 |
| [                Width = 500,]                                                                                                                              |
|                                                                                                                                                                                                 |
| [                AutoFormat = [Skins].Office2007Black,]                                                                             |
|                                                                                                                                                                                                 |
| [                InitiallyPopupShown=[true],]                                                                                          |
|                                                                                                                                                                                                 |
| [                **ClientSideOnBeforePopupShown = [\"OnBeforePopup\"],**]                                                           |
|                                                                                                                                                                                                 |
| **[                ClientSideOnPopupHidden = [\"popupHidden\"],]**                                                                  |
|                                                                                                                                                                                                 |
| **[                ClientSideOnPopupShown = [\"popupShown\"],]**                                                                    |
|                                                                                                                                                                                                 |
| **[                ClientSideOnSelect = [\"onRecordSelect\"],]**                                                                    |
|                                                                                                                                                                                                 |
| **[                ClientSideOnTextChanged = [\"onTextChanged\"]]**                                                                 |
|                                                                                                                                                                                                 |
| [            };]                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [       [function] OnBeforePopup(sender, args) {]                                                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//     args.get_SelectedRow() contains the selected record object (JSON).]]                                                                        |
|                                                                                                                                                                                                                                |
| [            [//     args.get_DisplayValue() contains the display value. ]]                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//     args.get_SelectedValue() contains the selected value.]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//     args.\_SelectedRow returns the selected record object (JSON).]]                                                                             |
|                                                                                                                                                                                                                                |
| [            [//     args.\_DisplayValue returns the display value.]]                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//     args.\_SelectedValue returns the selected Value.]]                                                                                          |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [   [function] popupHidden(sender, args) {]                                                                                                                           |
|                                                                                                                                                                                                                                |
| [       [//     args.get_SelectedRow() contains the selected record object (JSON).]]                                                                             |
|                                                                                                                                                                                                                                |
| [       [//     args.get_DisplayValue() contains the display value. ]]                                                                                           |
|                                                                                                                                                                                                                                |
| [       [//     args.get_SelectedValue() contains the selected value.]]                                                                                          |
|                                                                                                                                                                                                                                |
| [       [//     args.\_SelectedRow returns the selected record object (JSON).]]                                                                                  |
|                                                                                                                                                                                                                                |
| [       [//     args.\_DisplayValue returns the display value.]]                                                                                                 |
|                                                                                                                                                                                                                                |
| [       [//     args.\_SelectedValue returns the selected value.]]                                                                                               |
|                                                                                                                                                                                                                                |
| [   }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [   [function] popupShown(sender, args) {]                                                                                                                            |
|                                                                                                                                                                                                                                |
| [       [//     args.get_SelectedRow() contains the selected record object (JSON).]]                                                                             |
|                                                                                                                                                                                                                                |
| [       [//     args.get_DisplayValue() contains the display value. ]]                                                                                           |
|                                                                                                                                                                                                                                |
| [       [//     args.get_SelectedValue() contains the selected value.]]                                                                                          |
|                                                                                                                                                                                                                                |
| [       [//     args.\_SelectedRow returns the selected record object (JSON).]]                                                                                  |
|                                                                                                                                                                                                                                |
| [       [//     args.\_DisplayValue returns the display value.]]                                                                                                 |
|                                                                                                                                                                                                                                |
| [       [//     args.\_SelectedValue returns the selected value.]]                                                                                               |
|                                                                                                                                                                                                                                |
| [   }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [   [function] onRecordSelect(sender, args) {]                                                                                                                        |
|                                                                                                                                                                                                                                |
| [       [//     args.get_SelectedRow() contains the selected record object (JSON).]]                                                                             |
|                                                                                                                                                                                                                                |
| [       [//     args.get_DisplayValue() contains the display value. ]]                                                                                           |
|                                                                                                                                                                                                                                |
| [       [//     args.get_SelectedValue() contains the selected value.]]                                                                                          |
|                                                                                                                                                                                                                                |
| [       [//     args.\_SelectedRow returns the selected record object (JSON).]]                                                                                  |
|                                                                                                                                                                                                                                |
| [       [//     args.\_DisplayValue returns the display value.]]                                                                                                 |
|                                                                                                                                                                                                                                |
| [       [//     args.\_SelectedValue returns the selected value.]]                                                                                               |
|                                                                                                                                                                                                                                |
| [   }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [   [function] onTextChanged(sender, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [       [//     args.get_SelectedRow() contains the selected record object (JSON).]]                                                                             |
|                                                                                                                                                                                                                                |
| [       [//     args.get_DisplayValue() contains the display value. ]]                                                                                           |
|                                                                                                                                                                                                                                |
| [       [//     args.get_SelectedValue() contains the selected value.]]                                                                                          |
|                                                                                                                                                                                                                                |
| [       [//     args.\_SelectedRow returns the selected record object (JSON).]]                                                                                  |
|                                                                                                                                                                                                                                |
| [       [//     args.\_DisplayValue returns the display value.]]                                                                                                 |
|                                                                                                                                                                                                                                |
| [       [//     args.\_SelectedValue returns the selected value.]]                                                                                               |
|                                                                                                                                                                                                                                |
| [   }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [   [\</][script][\>]]                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

