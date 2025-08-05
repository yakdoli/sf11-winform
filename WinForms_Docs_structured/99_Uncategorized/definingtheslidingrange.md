---
title: definingtheslidingrange.md
original_path: WinForms_Docs/99_Uncategorized/definingtheslidingrange.md
created_at: 2025-08-05
---






#### Defining the Sliding Range {#defining-the-sliding-range style="tab-stops: 0pt"}

[] 

The slider allows you to customize the range of values that can be selected through the control.**[]**

**[]** 

Properties

 

 


  --------- ------------------------------------------------------------------------------------------------------------------- ------------------ ------------------- ------------
  Name      Description                                                                                                         Type of property   Value it accepts    Dependency
  Minimum   Sets the minimum allowable value.                                                                                   int                0 to int.MaxValue   NA
  Maximum   Sets the maximum allowable value.                                                                                   int                0 to int.MaxValue   NA
  Step      Sets the step value by which the value increases or decreases when the arrow key is press or the handle is moved.   int                0 to int.MaxValue   NA
  Value     Sets the value of the slider when loading.                                                                          int                0 to int.MaxValue   NA
  --------- ------------------------------------------------------------------------------------------------------------------- ------------------ ------------------- ------------


*[[]]{.underline}* 

Using Builder

The following steps explain how to set the range of the slider through the builder.

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **Minimum**, **Maximum**, **Step**, and **Value** methods with the desired values as arguments.

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])] |
|                                                                                                                                                                                                                         |
| **[.Minimum(0)]**                                                                                                                                                                   |
|                                                                                                                                                                                                                         |
| **[.Maximum(100)]**                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| **[.Value(50)]**                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| **[.Step(10)]**[%\>]                                                                                                        |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                   |
|                                                                                                                                                                      |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"])] |
|                                                                                                                                                                      |
| **[.Minimum(0)]**                                                                                                                |
|                                                                                                                                                                      |
| **[.Maximum(100)]**                                                                                                              |
|                                                                                                                                                                      |
| **[.Value(50)]**                                                                                                                 |
|                                                                                                                                                                      |
| **[.Step(10)]**[.Render();][}]       |
|                                                                                                                                                                      |
| []                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain how to set the range of the slider through the properties model.**

1.   In the controller, create an instance of **SliderModel**.

2.   Set the **Minimum**, **Maximum**, **Step** and **Value** properties and pass the instance through the view-specific data to the view.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                              |
|                                                                                                                                                                       |
| [public][ [ActionResult] Index()]                        |
|                                                                                                                                                                       |
| [        {]                                                                                                                       |
|                                                                                                                                                                       |
| [            [//Create an instance of TabModel.]]                                                           |
|                                                                                                                                                                       |
| [            [SliderModel] myModel = [new] [SliderModel]();] |
|                                                                                                                                                                       |
| [            **myModel.Minimum = 0;**]                                                                                            |
|                                                                                                                                                                       |
| **[            myModel.Maximum = 100;]**                                                                                          |
|                                                                                                                                                                       |
| **[            myModel.Value = 50;]**                                                                                             |
|                                                                                                                                                                       |
| **[            myModel.Step = 10;]**[]                                                        |
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
| **[]**                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   In View, invoke the slider helper with the view data key as the control ID.**

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])[%\>]] |
|                                                                                                                                                                                                                                                          |
| **[[[]]]{.underline}**                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                              |
|                                                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"]).Render();[}]] |
|                                                                                                                                                                                                               |
| **[[[]]]{.underline}**                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

4.   Build and run the application.

The following figure shows the slider output.

 

{border="0"}

Figure 236:Slider with Customized Range

 

[]{#related-topics}

