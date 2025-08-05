---
title: jquerytheme2.md
original_path: WinForms_Docs/02_Concepts/jquerytheme2.md
created_at: 2025-08-05
---






##### jQuery Theme {#jquery-theme style="tab-stops: 0pt"}

 

Aside from the Syncfusion themes, the slider control also supports all the default jQuery themes.**

**[Properties]**

**[]** 

+------------------+-----------------------------------+----------------------+---------------------------------------------------------------+----------------+
| **Name**         | **Description**                   | **Type of property** | **Value it accepts**                                          | **Dependency** |
+==================+===================================+======================+===============================================================+================+
| jQueryAutoFormat | Used to define the jQuery themes. | enum                 | [·      ]jQuerySkins.Smoothness  | NA             |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.UILightness |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.UIDarkness  |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.UIStart     |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.Redmond     |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.Cupertino   |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.SouthStreet |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.Blitzer     |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.Humanity    |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.HotSneaks   |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.ExciteBike  |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.Vader       |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.DotLuv      |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.MintChoc    |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.BlackTie    |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.Trontastic  |                |
|                  |                                   |                      |                                                               |                |
|                  |                                   |                      | [·      ]jQuerySkins.SwankyPurse |                |
+------------------+-----------------------------------+----------------------+---------------------------------------------------------------+----------------+

**[]** 

**[Using Builder]**[]

The following steps explain how to set jQuery themes through the builder.**

1.   In **View**, invoke the slider helper with the control ID as an argument, followed by the **jQueryAutoFormat** method with the desired theme as an argument.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])] |
|                                                                                                                                                                                                                                                                |
| **[.jQueryAutoFormat([jQuerySkins].MintChoc)]**[%\>]                                                             |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| **View\[cshtml\]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"])]                                                                |
|                                                                                                                                                                                                                                                               |
| **[.jQueryAutoFormat([jQuerySkins].MintChoc)]**[.Render();][}] |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

*[[[]]]{.underline}* 

**[]** 

Using Properties Model

 

The following steps explain how to set jQuery themes through the properties model.**

1.   In the controller, create an instance of **SliderModel**.

2.   Define the **jQueryAutoFormat** property and pass the instance through the **view-specific data** to the **View**.[]

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
| [            **myModel.jQueryAutoFormat = [jQuerySkins].MintChoc;**]                                      |
|                                                                                                                                                                                    |
| []                                                                                                                                |
|                                                                                                                                                                                    |
| [            [//Pass the instance through the view data to the view.]]                                      |
|                                                                                                                                                                                    |
| [            ViewData\[[\"mySlider\"]\] = myModel;]                                                       |
|                                                                                                                                                                                    |
| [            [return] View();]                                                                               |
|                                                                                                                                                                                    |
| [        }]                                                                                                                       |
|                                                                                                                                                                                    |
| []                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In **View**, invoke the slider helper with view data key as the control ID.**

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])[%\>]] |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| **View\[cshtml\]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"]).Render();[}]] |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

4.   Build and run the application.

 

The following figure shows the output of the slider with the jQuery theme.

 

{border="0"}

Figure 240: Slider with jQuery Theme

 

[]{#related-topics}

