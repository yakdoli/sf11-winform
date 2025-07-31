---
title: syncfusionthemes2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\syncfusionthemes2.md
created_at: 2025-07-03
---






##### Syncfusion Themes {#syncfusion-themes style="tab-stops: 0pt"}

The slider control supports fourteen built-in Syncfusion themes to enhance its look and feel.**

**[]** 

Properties

 

Table 5: Property Table

+-------------+---------------------------------------+------------------+--------------------------------------------------------------+-------------+
| Name        | Description                           | Type of property | Value it accepts                                             | Dependency  |
+-------------+---------------------------------------+------------------+--------------------------------------------------------------+-------------+
| AutoFormat  | Used to define the Syncfusion themes. | enum             | [·      ]Skins.Office2007Blue   | NA          |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Office2007Silver |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Office2007Black  |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Vista            |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Almond           |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Blueberry        |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Blend            |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Olive            |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Turquoise        |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Monochrome       |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Sandune          |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.VS2010           |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Marble           |             |
|             |                                       |                  |                                                              |             |
|             |                                       |                  | [·      ]Skins.Midnight         |             |
+-------------+---------------------------------------+------------------+--------------------------------------------------------------+-------------+

 

Using Builder

 

The following steps explain how to set Syncfusion themes through the builder.**

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **AutoFormat** method with the desired theme as an argument.

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])] |
|                                                                                                                                                                                                                         |
| **[.AutoFormat([Skins].Midnight)]**[%\>]                                                            |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                         |
|                                                                                                                                                                                                            |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"])]                                       |
|                                                                                                                                                                                                            |
| **[.AutoFormat([Skins].Midnight)]**[.Render();][}] |
|                                                                                                                                                                                                            |
| []                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

*[[[]]]{.underline}* 

Using Properties Model

The following steps explain how to set Syncfusion themes through the properties model.**

1.   In the controller, create an instance of **SliderModel**.

2.   Define the **AutoFormat** property and pass the instance through the view-specific data to the view.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                              |
|                                                                                                                                                                       |
| [public][ [ActionResult] Index()]                        |
|                                                                                                                                                                       |
| [        {]                                                                                                                       |
|                                                                                                                                                                       |
| [            [//Create an instance of TabModel.]]                                                           |
|                                                                                                                                                                       |
| [            [SliderModel] myModel = [new] [SliderModel]();] |
|                                                                                                                                                                       |
| [            **myModel.AutoFormat = [Skins].Midnight;**]                                                  |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [            [//Pass the instance through the view data to the view.]]                                      |
|                                                                                                                                                                       |
| [            ViewData\[[\"mySlider\"]\] = myModel;]                                                       |
|                                                                                                                                                                       |
| [            [return] View();]                                                                               |
|                                                                                                                                                                       |
| [        }]                                                                                                                       |
|                                                                                                                                                                       |
| []                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   In **View**, invoke the slider helper with the view data key as the control ID.**

**[]** 

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])[%\>]] |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                            |
|                                                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"]).Render();[}]] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

4.   Build and run the application.

 

The following figure shows the output of the slider with the set theme.

{border="0"}

Figure 239: Slider with Syncfusion Theme

 

[]{#related-topics}

