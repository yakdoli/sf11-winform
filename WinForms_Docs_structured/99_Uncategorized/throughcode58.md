---
title: throughcode58.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode58.md
created_at: 2025-07-03
---






#### Through Code {#through-code style="TEXT-ALIGN: justify; tab-stops: 0pt"}

You can add Skin Manager to one of the controls in your form or to the entire control as needed by specifying the root control. You can specify the root control using the *Control* property.

 

To add Skin Manager to one of the controls, specify the control as root control. The following code illustrates this:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                  |
|                                                                                                                                                               |
| []                                                                                                        |
|                                                                                                                                                               |
| [SkinManager][.SetVisualStyle([this].buttonAdv1] |
|                                                                                                                                                               |
| [, [VisualTheme].Office2007Blue );]                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------+
| \[VB\]                                                                                                                             |
|                                                                                                                                    |
| [SkinManager.SetVisualStyle([Me].buttonAdv1, VisualTheme.Office2007Blue)] |
+------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

To add Skin Manager to the entire form, specify the form as root control. The following code illustrates this:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                             |
| [            [SkinManager].SetVisualStyle([this], [VisualTheme].Office2007Blue );] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                        |
|                                                                                                                                     |
| [            SkinManager.SetVisualStyle([Me], VisualTheme.Office2007Blue)] |
+-------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

 

[]{#related-topics}

