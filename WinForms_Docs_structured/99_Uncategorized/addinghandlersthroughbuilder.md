---
title: addinghandlersthroughbuilder.md
original_path: WinForms_Docs/99_Uncategorized/addinghandlersthroughbuilder.md
created_at: 2025-08-05
---






#### Adding Handlers through Builder {#adding-handlers-through-builder style="tab-stops: 0pt"}

 

The following code snippet illustrates adding handlers through **Builder**.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\][]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                      |
| [\<%][=][Html.Syncfusion().MultiColumnDropDown\<[Student]\>([\"MultiColumnDropdown\"])] |
|                                                                                                                                                                                                                                                                                      |
| [        .Datasource(([IEnumerable]) ViewData\[[\"data\"]\])]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                      |
| [        .DisplayExpression([new] [int]\[\] {2, 3, 5})]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                      |
| [        .Width(500)]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| [        .AutoFormat([Skins].Office2007Black)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                      |
| [        .Text([\"\--Select\--\"])              ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                      |
| **[        .ClientSideOnBeforePopupShown([\"OnBeforePopup\"])]**                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                      |
| **[        .ClientSideOnPopupHidden([\"popupHidden\"])]**                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                      |
| **[        .ClientSideOnPopupShown([\"popupShown\"])]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| **[        .ClientSideOnSelect([\"onRecordSelect\"])]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| **[        .ClientSideOnTextChanged([\"onTextChanged\"])        ]**                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [    [%\>]]                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\][]]**                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [@(][new][ [HtmlString](][Html.Syncfusion().MultiColumnDropDown\<[Student]\>([\"MultiColumnDropdown\"])] |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        .Datasource(([IEnumerable]) ViewData\[[\"data\"]\])]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        .DisplayExpression([new] [int]\[\] {2, 3, 5})]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        .Width(500)]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        .AutoFormat([Skins].Office2007Black)]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        .Text([\"\--Select\--\"])              ]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[        .ClientSideOnBeforePopupShown([\"OnBeforePopup\"])]**                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[        .ClientSideOnPopupHidden([\"popupHidden\"])]**                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[        .ClientSideOnPopupShown([\"popupShown\"])]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[        .ClientSideOnSelect([\"onRecordSelect\"])]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[        .ClientSideOnTextChanged([\"onTextChanged\"])]**[]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [.ToString())[)]]**[]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                         |
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
| [            [//     args.get_DisplayValue() contains the display value.]]                                                                                       |
|                                                                                                                                                                                                                                |
| [            [//     args.get_SelectedValue() contains the selected value.]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//     args.\_SelectedRow returns the selected record object (JSON).]]                                                                             |
|                                                                                                                                                                                                                                |
| [            [//     args.\_DisplayValue returns the display value.]]                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//     args.\_SelectedValue returns the selected value.]]                                                                                          |
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
| [       [//     args.get_DisplayValue() contains the display value. ]]                                                                                           |
|                                                                                                                                                                                                                                |
| [       [//     args.get_SelectedValue() contains the selected value.]]                                                                                          |
|                                                                                                                                                                                                                                |
| [       [//     args.\_SelectedRow returns the Selected record object (JSON).]]                                                                                  |
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
| [       [//     args.\_SelectedRow returns the Selected record object (JSON).]]                                                                                  |
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
| [       [//     args.\_SelectedRow returns the Selected record object (JSON).]]                                                                                  |
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

