---
title: customthemes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\customthemes.md
created_at: 2025-07-03
---






##### Custom Themes {#custom-themes style="tab-stops: 0pt"}

[] 

The custom theme feature allows you to control background color, indicator image, and transparency.

Properties

 

  ----------------- ------------------------------------------------- ------------------------------------ ----------------------------------------------------------------------------------------- -------------------------------------------------------------
  Name              Description                                       Type of property                     Value it accepts                                                                          Dependency
  BackgroundColor   Sets the background color for the pop-up panel.   [struct]   [Members of System.Drawing.][Color]   NA
  Transparency      Set the opacity of the pop-up panel.              [double]   0 to 100                                                                                  NA
  ImageUrl          Set the URL of the pop-up indicator image.        [string]   url                                                                                       This property is not applicable for Waiting pop-up in HTML5
  ----------------- ------------------------------------------------- ------------------------------------ ----------------------------------------------------------------------------------------- -------------------------------------------------------------

**[]** 

Using Builder

 

The following steps explain how to define custom themes for the waiting pop-up through the builder.

1.   In **View**, create the target element over which the waiting pop-up is to be displayed.

2.   Invoke the waiting pop-up helper followed by the **BackgroundColor**, **ImageUrl**, and **Transparency** methods with the desired options as arguments.

**[]** 

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][div][ [id][=\"targetArea\"] [style][=\"][width][: 300px; ][height][: 150px;\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [\<][div][\>]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            User Name:]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<%][=]Html.Syncfusion().TextBox([\"userName\"]) [%\>][\</][div][\>]]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [\<][div][\>]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            Password:]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<%][=]Html.Syncfusion().Password([\"password\"]) [%\>][\</][div][\>]]                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      [\</][div][\>]]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().WaitingPopup([\"myPopup\"])]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [.TargetId([\"targetArea\"])]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [.**BackgroundColor(System.Drawing.[Color].DarkGreen)**]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[.Transparency(4)]**                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[.ImageUrl(Url.Content([\"\~/Content/ajax-loader2.gif\"]))]**[%\>]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][div][ [id][=\"targetArea\"] [style][=\"][width][: 300px; ][height][: 150px;\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [\<][div][\>]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            User Name:]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [@]Html.Syncfusion().TextBox([\"userName\"])[\</][div][\>]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [\<][div][\>]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            Password:]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [@]Html.Syncfusion().Password([\"password\"])[\</][div][\>]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      [\</][div][\>]]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\@{][ Html.Syncfusion().WaitingPopup([\"myPopup\"])]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [.TargetId([\"targetArea\"])]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [.**BackgroundColor(System.Drawing.[Color].DarkGreen)**]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[.Transparency(4)]**                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[.ImageUrl(Url.Content([\"\~/Content/ajax-loader2.gif\"]))]**[.Render();][}]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

**[]** 

Using Properties Model

[] 

The following steps explain how to define custom themes for the waiting pop-up through the poperties model.**[]**

1.   In the controller, create an instance of **WaitingPopupModel**. **

2.   Define the **BackgroundColor**, **ImageUrl**, and **Transparency** properties and pass the instance through the **view-specific data** to the **view**.**

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                          |
|                                                                                                                                                                                   |
| [public][ [ActionResult] Index()]                                    |
|                                                                                                                                                                                   |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                   |
| [            [//Create an instance of WatingPopupModel]]                                                                |
|                                                                                                                                                                                   |
| [            [WaitingPopupModel] myModel = [new] [WaitingPopupModel]();] |
|                                                                                                                                                                                   |
| [            myModel.TargetId = [\"targetArea\"];]                                                                    |
|                                                                                                                                                                                   |
| [            **myModel.BackgroundColor = System.Drawing.[Color].DarkGreen;**]                                         |
|                                                                                                                                                                                   |
| **[            myModel.Transparency = 4;]**                                                                                                   |
|                                                                                                                                                                                   |
| **[            myModel.ImageUrl = Url.Content([\"\~/Content/ajax-loader2.gif\"]);]**                                  |
|                                                                                                                                                                                   |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                   |
| [            [//Pass the instance through view data to the view]]                                                       |
|                                                                                                                                                                                   |
| [            ViewData\[[\"myPopup\"]\] = myModel;]                                                                    |
|                                                                                                                                                                                   |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                   |
| [        }]                                                                                                                                   |
|                                                                                                                                                                                   |
| []                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

3.   In **View**, create the target element over which the waiting pop-up is to be displayed.**

4.   Invoke the waiting pop-up helper with the view data key as the control ID.**

**[]** 

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][div][ [id][=\"targetArea\"] [style][=\"][width][: 300px; ][height][: 150px;\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [\<][div][\>]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            User Name:]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<%][=]Html.Syncfusion().TextBox([\"userName\"]) [%\>][\</][div][\>]]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [\<][div][\>]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            Password:]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<%][=]Html.Syncfusion().Password([\"password\"]) [%\>][\</][div][\>]]                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      [\</][div][\>]]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().WaitingPopup([\"myPopup\"])[%\>]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][div][ [id][=\"targetArea\"] [style][=\"][width][: 300px; ][height][: 150px;\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [\<][div][\>]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            User Name:]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [@]Html.Syncfusion().TextBox([\"userName\"])[\</][div][\>]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [\<][div][\>]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            Password:]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [@]Html.Syncfusion().Password([\"password\"])[\</][div][\>]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      [\</][div][\>]]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\@{][ Html.Syncfusion().WaitingPopup([\"myPopup\"]).Render();[}]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

5.   Build and run the application.

The following screenshot shows the output of the waiting pop-up control with a custom theme.

 

{border="0"}

Figure 339: Waiting Popup with Custom Theme

 

[]{#related-topics}

