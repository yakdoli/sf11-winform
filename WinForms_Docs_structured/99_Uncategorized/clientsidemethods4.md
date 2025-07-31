---
title: clientsidemethods4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsidemethods4.md
created_at: 2025-07-03
---






#### Client Side Methods {#client-side-methods style="tab-stops: 0pt"}

Mask Edit text box supports a rich set of client side methods to control its behavior.

**[]** 

Methods

**[]** 

  ------------------------------------------------- -------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------- --------------------------------------------
  Name                                              Parameters                                                                                         Return type                                                                                        Description
  get_StrippedValue**[]**     NA                                                                                                 [[string]]{.UGHyperlink}   Returns the textbox value without literals
  get_UnstrippedValue**[]**   NA                                                                                                 [[string]]{.UGHyperlink}   Returns the textbox value with literals
  get_Value**[]**             NA                                                                                                 [[string]]{.UGHyperlink}   Returns the textbox value as it is
  get_WaterMarkText**[]**     NA                                                                                                 [[string]]{.UGHyperlink}   Returns the current watermark text
  set_WaterMarkText                                 [[string]]{.UGHyperlink}   [-]                                                                           Sets the watermark text to the textbox
  Clear                                             NA                                                                                                 \-                                                                                                 Clears the textbox
  ------------------------------------------------- -------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------- --------------------------------------------

 

The following steps explain the use of client side methods of mask edit textbox to an application using Builder.

1.   In **View**, invoke the mask edit textbox helper followed by the **Mask** method with the desired mask as argument.

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"])] |
|                                                                                                                                                                                                                                                                           |
| **[.Mask([\"999-99-999\"])]**[%\>]                                                                                          |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                             |
| [\@{][ Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"])]                                   |
|                                                                                                                                                                                                                                             |
| **[.Mask([\"999-99-999\"])]**[.Render();][}] |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In the Javascript, use the methods as given below:

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Javascript\]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                       |
| [        [function] Get_Values() {]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                       |
| [            [var] value = \$find([\"myMaskEdit\"]).get_Value();]                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [            [var] unstrippedValue = \$find([\"myMaskEdit\"]).get_UnstrippedValue();]                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [var] strippedValue = \$find([\"myMaskEdit\"]).get_StrippedValue();]                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [        [function] WaterMarkText() {]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [            [var] waterMark = \$find([\"myMaskEdit\"]).get_WaterMarkText();]                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [            \$find([\"myMaskEdit\"]).set_WaterMarkText([\"EnterValue\"]);]                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [        [function] Clear() {]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [            \$find([\"myMaskEdit\"]).Clear();]                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [       [\</][script][\>]]                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.

[]{#related-topics}

