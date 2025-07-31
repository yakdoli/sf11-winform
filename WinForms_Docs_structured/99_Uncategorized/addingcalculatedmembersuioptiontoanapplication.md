---
title: addingcalculatedmembersuioptiontoanapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingcalculatedmembersuioptiontoanapplication.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Adding Calculated Members UI Option to an Application {#adding-calculated-members-ui-option-to-an-application style="tab-stops: 0pt"}

The following code sample explains how to enable or disable the Calculated Members UI option in an OlapClient application:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [////Enable the Calculated Members in current view of the OlapClient.]                                                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [this] [.olapClient1.IsCalculatedMembersEnabled = ] [true] [; ] |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [//if set false, then it will be disabled or all calculated members will be deleted from the current view of the OlapClient.] []                                  |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                            |
|                                                                                                                                                                             |
| [\'Enable the Calculated Members in ] [current view of the OlapClient.] |
|                                                                                                                                                                             |
| []                                                                                                                        |
|                                                                                                                                                                             |
|                     Me                                                                                                                                                      |
|                     .olapClient1.IsCalculatedMembersEnabled =                                                                                                               |
|                     True                                                                                                                                                    |
|                                                                                                                                                                             |
|                                                                                                                                                                             |
|                                                                                                                                                                             |
|                                                                                                                                                                             |
|                                                                                                                                                                             |
|                                                                                                                                                                             |
|                     ''''if set false, then it will be disabled or all calculated members will be deleted from the current view of the OlapClient.                           |
|                                                                                                                                                                             |
|                                                                                                                                                                             |
|                                                                                                                                                                             |
|                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------+
|                                                                       |
|                       [XAML]                                          |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                     <                                                 |
|                     CheckBox                                          |
|                      Name                                             |
|                     ="chk_CalcMember                                  |
|                     ToolTip                                           |
|                     ="Enable/Disable Calculated Members"              |
|                      Content                                          |
|                     ="Enable Calculated Members"                      |
|                      IsChecked                                        |
|                     ="{                                               |
|                     Binding                                           |
|                      ElementName                                      |
|                     =olapClient1,                                     |
|                      Path                                             |
|                     =IsCalculatedMembersEnabled}"/>                   |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
+-----------------------------------------------------------------------+

[] 

 

[]{#related-topics}

