---
title: watermarking1.md
original_path: WinForms_Docs/99_Uncategorized/watermarking1.md
created_at: 2025-08-05
---






#### Watermarking {#watermarking style="tab-stops: 0pt"}

Mask Edit textbox supports watermarking. A watermark text is a background text that appears in a text box without interfering with text entry or readability of the text entered. It can be used to display a ready instruction or important information for the user. It appears as an auto text before the test is entered and disappears once the user starts entering text.

Properties

 

+---------------+------------------------------------------+--------------------------------------------------------------------------------------------------+------------------+-------------+
| Name          | Description                              | Type of property                                                                                 | Value it accepts | Dependency  |
+---------------+------------------------------------------+--------------------------------------------------------------------------------------------------+------------------+-------------+
| WaterMarkText | Sets the water mark text to be displayed | [[string]]{.UGHyperlink} | Alphanumeric     | NA          |
|               |                                          |                                                                                                  |                  |             |
|               |                                          | []                                                                          |                  |             |
+---------------+------------------------------------------+--------------------------------------------------------------------------------------------------+------------------+-------------+

 

Using Builder

The following steps explain the setting of the watermark text for the mask edit using Builder.

1.   In **View**, invoke the mask edit textbox helper followed by the **WaterMarkText** method with the desired mask as argument.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"])] |
|                                                                                                                                                                                                                                                                           |
| [.Mask([\"999-99-999\"])]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| **[.WaterMarkText([\"Enter a Value\"])]**[%\>]                                                                              |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [\@{][ ][Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"])] |
|                                                                                                                                                                                                                                                                           |
| [.Mask([\"999-99-999\"])]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| **[.WaterMarkText([\"Enter a Value\"])]**[.Render();][}]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

2.   Build and run the application

**[]** 

Using PropertiesModel

The following steps explain the setting of the watermark text for Mask Edit using the Properties model.

1.   In the **Controller**, create an instance of **MaskEditTextBoxModel**, set the **WaterMark** property and pass the instance through view specific data to View as given below.**

*[[[]]]{.underline}* 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                                   |
|                                                                                                                                                                                                      |
|                                                                                                                                                                                                      |
|                                                                                                                                                                                                      |
| [public][ [ActionResult] Index()]                             |
|                                                                                                                                                                                                      |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                                      |
| [            [//create an instance of MaskEditTextBoxModel]]                                                                  |
|                                                                                                                                                                                                      |
| [            [MaskEditTextBoxModel] myModel = [new] [MaskEditTextBoxModel]();] |
|                                                                                                                                                                                                      |
| [            myModel.Mask = [\"999-99-999\"];]                                                                              |
|                                                                                                                                                                                                      |
| **[            myModel.WaterMarkText = [\"Enter a Value\"];]**                                                              |
|                                                                                                                                                                                                      |
| [            ]                                                                                                                                      |
|                                                                                                                                                                                                      |
| [            [//pass the instance through view data to the view]]                                                             |
|                                                                                                                                                                                                      |
| [            ViewData\[[\"myMaskEdit\"]\] = myModel;]                                                                       |
|                                                                                                                                                                                                      |
| [            [return] View();]                                                                                                 |
|                                                                                                                                                                                                      |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                                      |
| []                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[[]]{.underline}* 

2.   In **View**, invoke the mask edit textbox helper with view data key as the Control ID.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"])[%\>]] |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                    |
| [\@{][ ][Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"]).Render();[}]] |
|                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

3.   Build and run the application.

The output is shown in the following screenshot.

{border="0"}

Figure 145: Mask Edit textbox with watermarking

[]{#related-topics}

