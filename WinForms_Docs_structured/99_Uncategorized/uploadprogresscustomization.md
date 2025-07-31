---
title: uploadprogresscustomization.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\uploadprogresscustomization.md
created_at: 2025-07-03
---






##### UploadProgress Customization {#uploadprogress-customization style="tab-stops: 0pt"}

[] 

Setting Target Control

[] 

UploadProgress allows you to specify the target control for which the progress control should be triggered displaying the details of the process on completion. To specify the target control, the **Triggers** property must be set to the id of that control.

[] 


  ---------- -------------------------------------------------------------------------------------------
  Property   Description
  Triggers   Specifies the id of the controls (space separated) to trigger the UploadProgress control.
  ---------- -------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                          |
|                                                                                                           |
| **[]**                                                                |
|                                                                                                           |
| [uploadprogress1.Triggers = [\"uploadbox1\"];] |
+-----------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                    |
|                                                                                                                                                                     |
| **[]**                                                                                                                          |
|                                                                                                                                                                     |
| [Private][ uploadprogress1.Triggers = [\"uploadbox1\"]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Popup Settings

[] 

The progress control can either be shown initially or it could be popped up only after some action is performed on the target control.

[] 

The Upload Progress control can be closed once the file upload is complete and the details of the process are displayed. For this, the **ClosePopup** property must be enabled. By disabling the property, the control will remain displaying the details of the upload process, unless it is closed manually.

[] 


  ------------ --------------------------------------------------------------------------------------------------------------------------------------
  Property     Description
  ClosePopup   Gets/sets the boolean value, whether to close the uploadprogress popup after the upload process is complete. Default value is false.
  Inline       Gets/sets the boolean value whether to display the control inline or as a popup.
  ------------ --------------------------------------------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                |
|                                                                                                 |
| **[]**                                                      |
|                                                                                                 |
| [uploadprogress1.Inline = [false];]    |
|                                                                                                 |
| [uploadprogress1.ClosePopup = [true];] |
+-------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                          |
|                                                                                                                                                           |
| **[]**                                                                                                                |
|                                                                                                                                                           |
| [Private][ uploadprogress1.Inline = [False]]    |
|                                                                                                                                                           |
| [Private][ uploadprogress1.ClosePopup = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Styles

[] 

Styles can be applied to the control through css setting thereby easily customizing your control using style sheets.

[] 


  ---------- -----------------------------------------------------------------------------
  Property   Description
  UserCSS    Specifies the user defined css style settings to be applied to the control.
  ---------- -----------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                               |
|                                                                                                |
| **[]**                                                     |
|                                                                                                |
| [uploadprogress1.UserCSS = [\"\"];] |
+------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                         |
|                                                                                                                                                          |
| **[]**                                                                                                               |
|                                                                                                                                                          |
| [Private][ uploadprogress1.UserCSS = [\"\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

