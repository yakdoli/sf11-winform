---
title: watermarktext.md
original_path: WinForms_Docs/99_Uncategorized/watermarktext.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Watermark text {#watermark-text style="tab-stops: 0pt"}

MaskEdit textbox supports watermarking. A watermark text is a background text that appears in a text box without interfering the text entry or readability of the text entered in the textbox. It can be used to display a ready instruction or important information for the user. It appears as an auto text before the test is entered and disappears once the user starts entering text.

[] 

Properties

 

 

  --------------- ------------------------------------------ ------------------------ ------------------ ------------
  Name            Description                                Type of the property     Value it accepts   Dependency
  WaterMarkText   Sets the water mark text to be displayed   [string]{.UGHyperlink}   Alphanumeric       NA
  --------------- ------------------------------------------ ------------------------ ------------------ ------------

 

Using Builder

The following steps will guide you in setting the watermark text for the MaskEdit through the Builder:

1.   In **View**, invoke the MaskEdit textbox helper followed by the **WaterMarkText** method with the desired mask as argument.

[[ [] ]]{.underline}  

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| [  ] [\<%] [{]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                         |
| [        ] [Html.MobSyncfusion().MaskEditTextbox([\"maskCredit\"]).Mask([\"9999-9999-9999-9999\"]).**WaterMarkText**([\"9999-9999-9999-9999\"])] [] |
|                                                                                                                                                                                                                                                                                                                                         |
| [                          .Render();]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| [                      }[%\>]]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                         |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| [\@{] []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [        ] [Html.MobSyncfusion().MaskEditTextbox([\"maskCredit\"]).Mask([\"9999-9999-9999-9999\"]).**WaterMarkText**([\"9999-9999-9999-9999\"])] [] |
|                                                                                                                                                                                                                                                                                                                                         |
| [                          .Render();]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| [                      [}]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.underline}  

2.   Run the application.

 

Using Properties Model

The following steps will guide you in setting of the watermark text for the MaskEdit through the Properties model.

1.   In the **Controller**, create an instance of **MaskEditTextBoxModel**, set the **WaterMark** property and pass the instance through view specific data to View as given below:[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                      |
| [public] [ [ActionResult] Index()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                      |
| [            [MaskEditTextBoxModel] myModel = [new][MaskEditTextBoxModel]();]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [            myModel.Mask = [\"]] [9999-9999-9999-9999] [\"] [;]                                                             |
|                                                                                                                                                                                                                                                                                                                                      |
| **[            myModel.WaterMarkText = [\"]]** [9999-9999-9999-9999] **[\"]** **[;]** [] |
|                                                                                                                                                                                                                                                                                                                                      |
| [            ViewData\[[\"myMaskEdit\"]\] = myModel;]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                      |
| [            [return] View();]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                      |
| [        }] []                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

2.   In **View**, invoke the MaskEdit textbox helper with the ViewData key as the first argument.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** [  ] [\<%] [{                                ] |
|                                                                                                                                                                                                                                   |
| [    Html.MobSyncfusion().] [MaskEditTextbox] [([\"myMaskEdit\")]]                            |
|                                                                                                                                                                                                                                   |
| [                          .Render();]                                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| [       }[%\>]]                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| **[\[Razor\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [    ] [\@{] []                                                                                   |
|                                                                                                                                                                                                                                   |
| [           Html.MobSyncfusion().] [MaskEditTextbox] [([\"myMaskEdit\"])]                     |
|                                                                                                                                                                                                                                   |
| [                          .Render();]                                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| [       [}]] []                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: The second argument of the above MaskEdit textbox helper should match the view data key from the controller to fetch the properties.


3.   Run the application.

The following screenshot illustrates the output:

{border="0"}

Figure 250 MaskEdit textbox with Watermark text

 

[]{#related-topics}

