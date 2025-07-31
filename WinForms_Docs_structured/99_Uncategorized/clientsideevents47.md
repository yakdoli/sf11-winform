---
title: clientsideevents47.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents47.md
created_at: 2025-07-03
---








  









### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

This section details the client-side events raised by the MultiColumnDropDown control.

Properties

 


  ------------------------------ --------------------------------------------------------------------------- ------------------------------- ------------------ ------------
  Name                           Description                                                                 Type of property                Value it accepts   Dependency
  ClientSideOnBeforePopupShown   Used to add the clientside ClientSideOnBeforePopupShown event to control.   [string]   alphanumeric       NA
  ClientSideOnPopupHidden        Used to add the clientside ClientSideOnPopupHidden event to control.        [string]   alphanumeric       NA
  ClientSideOnPopupShown         Used to add the clientside ClientSideOnPopupShown event to control.         [string]   alphanumeric       NA
  ClientSideOnSelect             Used to add the clientside ClientSideOnSelect event to control.             [string]   alphanumeric       NA
  ClientSideOnTextChanged        Used to add the clientside ClientSideOnTextChanged event to control.        [string]   alphanumeric       NA
  ------------------------------ --------------------------------------------------------------------------- ------------------------------- ------------------ ------------


 

Methods

 


+---------------------------------------+--------------------------------+-----------------------------+---------------------------------------------------------------------------+
| Method                                | Parameters                     | Return type                 | Descriptions                                                              |
+---------------------------------------+--------------------------------+-----------------------------+---------------------------------------------------------------------------+
| ClientSideOnBeforePopupShown(handler) | Function name in string format | IMultiColumnDropDownBuilder | Used to add the client-side OnBeforePopupShown event to the control.      |
|                                       |                                |                             |                                                                           |
|                                       |                                |                             |                                                                           |
|                                       |                                |                             |                                                                           |
|                                       |                                |                             |                                                                           |
+---------------------------------------+--------------------------------+-----------------------------+---------------------------------------------------------------------------+
| ClientSideOnPopupHidden(handler)      | Function name in string format | IMultiColumnDropDownBuilder | Used to add the client-side ClientSideOnPopupHidden event to the control. |
|                                       |                                |                             |                                                                           |
|                                       |                                |                             |                                                                           |
+---------------------------------------+--------------------------------+-----------------------------+---------------------------------------------------------------------------+
| ClientSideOnPopupShown(handler)       | Function name in string format | IMultiColumnDropDownBuilder | Used to add the client-side ClientSideOnPopupShown event to the control.  |
|                                       |                                |                             |                                                                           |
|                                       |                                |                             |                                                                           |
+---------------------------------------+--------------------------------+-----------------------------+---------------------------------------------------------------------------+
| ClientSideOnSelect(handler)           | Function name in string format | IMultiColumnDropDownBuilder | Used to add the client-side ClientSideOnSelect event to the control.      |
|                                       |                                |                             |                                                                           |
|                                       |                                |                             |                                                                           |
+---------------------------------------+--------------------------------+-----------------------------+---------------------------------------------------------------------------+
| ClientSideOnTextChanged(handler)      | Function name in string format | IMultiColumnDropDownBuilder | Used to add the client-side ClientSideOnTextChanged event to the control. |
|                                       |                                |                             |                                                                           |
|                                       |                                |                             |                                                                           |
+---------------------------------------+--------------------------------+-----------------------------+---------------------------------------------------------------------------+


 

Events

[] 


+------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Name                         | Description                                                                     | Arguments                                                                                                     |
+------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ClientSideOnBeforePopupShown | This event is raised just before the popup is shown.                            | get_SelectedRow() [// Contains the Selected record object (JSON).]                      |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | get_DisplayValue() [// Contains the display value.]                                     |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | get_SelectedValue() [// Contains the selected value.]                                   |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_SelectedRow [// Returns the Selected record object (JSON).][] |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_DisplayValue [// Returns the display value.][]                |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_SelectedValue [// Returns the selected Value.]                                        |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 |                                                                                                               |
+------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ClientSideOnPopupHidden      | This event is raised when the pop-up panel hides.                               | get_SelectedRow() [// Contains the Selected record object (JSON).]                      |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | get_DisplayValue() [// Contains the display value. ]                                    |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | get_SelectedValue() [// Contains the selected value.]                                   |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_SelectedRow [// Returns the Selected record object (JSON).][] |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_DisplayValue [// Returns the display value.][]                |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_SelectedValue [// Returns the selected Value.]                                        |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 |                                                                                                               |
+------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ClientSideOnPopupShown       | This event is raised when the pop-up panel displays.                            | get_SelectedRow() [// Contains the Selected record object (JSON).]                      |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | get_DisplayValue() [// Contains the display value. ]                                    |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | get_SelectedValue() [// Contains the selected value.]                                   |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_SelectedRow [// Returns the Selected record object (JSON).][] |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_DisplayValue [// Returns the display value.][]                |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_SelectedValue [// Returns the selected Value.]                                        |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 |                                                                                                               |
+------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ClientSideOnSelect           | This event is raised when you select the record from dropdown.                  | get_SelectedRow() [// Contains the Selected record object (JSON).]                      |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | get_DisplayValue() [// Contains the display value. ]                                    |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | get_SelectedValue() [// Contains the selected value.]                                   |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_SelectedRow [// Returns the Selected record object (JSON).][] |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_DisplayValue [// Returns the display value.][]                |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_SelectedValue [// Returns the selected Value.]                                        |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 |                                                                                                               |
+------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ClientSideOnTextChanged      | This event is raised when the value of the generic drop-down text box  changes. | get_SelectedRow() [// Contains the Selected record object (JSON).]                      |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | get_DisplayValue() [// Contains the display value.]                                     |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | get_SelectedValue() [// Contains the selected value.]                                   |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_SelectedRow [// Returns the Selected record object (JSON).][] |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_DisplayValue [// Returns the display value.][]                |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 | \_SelectedValue [// Returns the selected Value.]                                        |
|                              |                                                                                 |                                                                                                               |
|                              |                                                                                 |                                                                                                               |
+------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+


[] 

More:







