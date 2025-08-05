---
title: sliderrange.md
original_path: WinForms_Docs/99_Uncategorized/sliderrange.md
created_at: 2025-08-05
---






#### Slider*[ ]*[]{#_Range_Slider}Range {#slider-range style="tab-stops: 0pt"}

The slider control supports setting a range of values that can be selected within the two handles.

**[]** 

**[Properties]**

**[]** 

Table 4: Property Table

  -------- --------------------------------------------- -------------------------------------- ---------------------------- ------------
  Name     Description                                   Type of property                       Value it accepts             Dependency
  Range    Sets the range of the slider.                 [object]     True/False                   NA
  Values   Sets the default values of the two handles.   [int\[2\]]   Array of positive integers   NA
  -------- --------------------------------------------- -------------------------------------- ---------------------------- ------------

*[[]]{.underline}* 

Using Builder

The following steps explain how to create a slider range through the builder.**

1.   In View, invoke the slider helper with the control ID as an argument followed by the Range and Values methods with the desired options as arguments.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider1\"]) ] |
|                                                                                                                                                                                                                           |
| [.**Range([true])**]                                                                                                                                             |
|                                                                                                                                                                                                                           |
| **[.Values([new] [int]\[\]{25,50})]**[%\>]                                          |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| [\@{][ Html.Syncfusion().Slider([\"mySlider1\"]) ]                                                         |
|                                                                                                                                                                                                                                |
| [.**Range([true])**]                                                                                                                                                  |
|                                                                                                                                                                                                                                |
| **[.Values([new] [int]\[\]{25,50})]**[.Render();][}] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain how to create a slider range through the properties model.**

1.   In the controller, create an instance of **SliderModel**.

2.   Set the **Range** and **Values** properties and pass the instance through the **view-specific data** to the **view**.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                 |
|                                                                                                                                                                                    |
| [public][ [ActionResult] Index()]           |
|                                                                                                                                                                                    |
| [        {]                                                                                                                       |
|                                                                                                                                                                                    |
| [            [//Create an instance of TabModel.]]                                                           |
|                                                                                                                                                                                    |
| [            [SliderModel] myModel = [new] [SliderModel]();] |
|                                                                                                                                                                                    |
| **[            myModel.Range = [true];]**                                                                    |
|                                                                                                                                                                                    |
| **[            myModel.Values = [new] [int]\[\] { 25, 50 };]**                          |
|                                                                                                                                                                                    |
| []                                                                                                                                |
|                                                                                                                                                                                    |
| [            [//Pass the instance through the view data to the view.]]                                      |
|                                                                                                                                                                                    |
| [            ViewData\[[\"mySlider\"]\] = myModel;]                                                       |
|                                                                                                                                                                                    |
| [            [return] View();]                                                                               |
|                                                                                                                                                                                    |
| [        }]                                                                                                                       |
|                                                                                                                                                                                    |
| []                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In **View**, invoke the slider helper with the view data key as the control ID.**

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])[%\>]] |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[[\
\
]]{.underline}*

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"]).Render();[}]] |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

4.   Build and run the application.

The following figure shows the slider output with the specified range.

{border="0"}

Figure 238: Slider Range

[]{#related-topics}

