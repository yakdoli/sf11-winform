---
title: clientsidemethods24.md
original_path: WinForms_Docs/99_Uncategorized/clientsidemethods24.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Client Side Methods {#client-side-methods style="tab-stops: 0pt"}

The MaskEdit text box control supports rich set of client-side methods to control its behavior.

[] 

Methods

+---------------------+-----------------+-----------------+--------------------------------------------+
| Name                | Parameters      | Return type     | Description                                |
+---------------------+-----------------+-----------------+--------------------------------------------+
| get_StrippedValue   | NA              | string          | Returns the textbox value without literals |
+---------------------+-----------------+-----------------+--------------------------------------------+
| get_UnstrippedValue | NA              | string          | Returns the textbox value with literals    |
|                     |                 |                 |                                            |
|                     |                 |                 |                                            |
+---------------------+-----------------+-----------------+--------------------------------------------+
| get_Value           | NA              | string          | Returns the textbox value as it is         |
+---------------------+-----------------+-----------------+--------------------------------------------+
| get_WaterMarkText   | NA              | string          | Returns the current watermark text         |
+---------------------+-----------------+-----------------+--------------------------------------------+
| set_WaterMarkText   | string          | \-              | Sets the watermark text to the textbox     |
+---------------------+-----------------+-----------------+--------------------------------------------+
| Clear               | NA              | \-              | Clears the textbox                         |
|                     |                 |                 |                                            |
|                     |                 |                 |                                            |
+---------------------+-----------------+-----------------+--------------------------------------------+

 

The following steps, guides you in using the client side methods:

1.   In **View**, invoke the MaskEdit text box helper with the control ID as first argument.

**[]**  

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                             |
|                                                                                                                                                                                |
| [  ] [\<%] [{                                ] |
|                                                                                                                                                                                |
| [      Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"])]                                                        |
|                                                                                                                                                                                |
| **[.Mask([\"999-99-999\"])]** []                                               |
|                                                                                                                                                                                |
| [       }[%\>]]                                                                                                |
|                                                                                                                                                                                |
| **[ \[Razor\]]**                                                                                                                           |
|                                                                                                                                                                                |
| [    ] [\@{] []                                |
|                                                                                                                                                                                |
| [      Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"])]                                                        |
|                                                                                                                                                                                |
| **[.Mask([\"999-99-999\"])]** []                                               |
|                                                                                                                                                                                |
| [}] []                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.     In JavaScript, use the methods as they are given in the following code:

**[]**  

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]** [ ]                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| [        [function] Get_Values() {]                                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [            [var] value = \$find([\"myMaskEdit\"]).get_Value();]                                                                                  |
|                                                                                                                                                                                                                                    |
| [            [var] unstrippedValue = \$find([\"myMaskEdit\"]).get_UnstrippedValue();]                                                              |
|                                                                                                                                                                                                                                    |
| [            [var] strippedValue = \$find([\"myMaskEdit\"]).get_StrippedValue();]                                                                  |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [        [function] WaterMarkText() {]                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [var] waterMark = \$find([\"myMaskEdit\"]).get_WaterMarkText();]                                                                      |
|                                                                                                                                                                                                                                    |
| [            \$find([\"myMaskEdit\"]).set_WaterMarkText([\"EnterValue\"]);]                                                                      |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [        [function] Clear() {]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            \$find([\"myMaskEdit\"]).Clear();]                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [       [\</][script][\>]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

 

[]{#related-topics}

