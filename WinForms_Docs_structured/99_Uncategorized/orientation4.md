---
title: orientation4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\orientation4.md
created_at: 2025-07-03
---






#### Orientation {#orientation style="tab-stops: 0pt"}

The slider control supports both horizontal and vertical orientations.

**[]** 

Properties

 

Table 3: Proterty Table

+-------------+-------------------------------------+------------------+-------------------------------------------+-------------+
| Name        | Description                         | Type of property | Value it accepts                          | Dependency  |
+-------------+-------------------------------------+------------------+-------------------------------------------+-------------+
| Orientation | Sets the orientation of the slider. | enum             | jQueryModel.SliderOrientation.Horizontal, | NA          |
|             |                                     |                  |                                           |             |
|             |                                     |                  | jQueryModel.SliderOrientation.Vertical    |             |
+-------------+-------------------------------------+------------------+-------------------------------------------+-------------+

*[[]]{.underline}* 

Using Builder

The following steps explain how to set slider orientation using Builder.**

1.   In **View**, invoke the slider helper with the control ID as an argument, followed by the **Orientation** method with the desired orientation as an argument.

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])] |
|                                                                                                                                                                                                                         |
| [.Orientation([jQueryModel].[SliderOrientation].Vertical)[%\>]]                                         |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                      |
|                                                                                                                                                                                         |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"])]                    |
|                                                                                                                                                                                         |
| [.Orientation([jQueryModel].[SliderOrientation].Vertical).Render();[}]] |
|                                                                                                                                                                                         |
| []                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

 

**[Using Properties Model]**[]

The following steps explain how to set slider orientation through the properties model.**

1.   In the controller, create an instance of **SliderModel**.

2.   Define the **Orientation** property and pass the instance through the view-specific data to the view.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                              |
|                                                                                                                                                                       |
| [public][ [ActionResult] Index()]                        |
|                                                                                                                                                                       |
| [        {]                                                                                                                       |
|                                                                                                                                                                       |
| [            [//Create an instance of TabModel]]                                                            |
|                                                                                                                                                                       |
| [            [SliderModel] myModel = [new] [SliderModel]();] |
|                                                                                                                                                                       |
| [            myModel.Orientation = [jQueryModel].[SliderOrientation].Vertical;]   |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [            [//Pass the instance through view data to the view]]                                           |
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

3.   In **View**, invoke the slider helper with the view data key as the control ID.**

*[[]]{.underline}* 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])[%\>]] |
|                                                                                                                                                                                                                                                          |
| **[[[]]]{.underline}**                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

*[[]]{.underline}* 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                            |
|                                                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"]).Render();[}]] |
|                                                                                                                                                                                                               |
| **[[[]]]{.underline}**                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

4.   Build and run the application.

The following figure shows the orientation output of the slider.

 

{border="0"}

Figure 237: Slider with Vertical Orientation

 

[]{#related-topics}

