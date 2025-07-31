---
title: throughviewcustomization20.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughviewcustomization20.md
created_at: 2025-07-03
---






##### Through View Customization {#through-view-customization style="tab-stops: 0pt"}

 

Step 1:

View:

 

Add the below code in the aspx file.

The **Unit** property is used to set the unit value for the Rolling Gauge. Here you are adding the text box for updating the gauge unit value dynamically in its keyup event.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the rolling gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| [    [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                    |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [            [//Specifying the unit value for the gauge]]                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [          .Unit([\"KM\"])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [         .Value([\"100\"])]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                           |
| [          .SegmentCount(3)]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [         .Height(50)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [    [%\>]]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [    [\<%][\--Adding the text box for updating the gauge unit value in its keyup event\--][%\>]]                                    |
|                                                                                                                                                                                                                                                           |
| [    [\<%][=]Html.TextBox([\"Unit\"], [\"KM\"])[%\>]]                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [@\*][\--Rendering the rolling gauge\--][\*@][] |
|                                                                                                                                                                                                                                                           |
| [    [\@{] Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                                           |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [            [//Specifying the unit value for the gauge]]                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [          .Unit([\"KM\"])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [         .Value([\"100\"])]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                           |
| [          .SegmentCount(3)]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [         .Height(50).Render();         ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                           |
| [    [}]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [    [@\*][\--Adding the text box for updating the gauge unit value in its keyup event\--][\*@]]                                    |
|                                                                                                                                                                                                                                                           |
| [   [@]Html.TextBox([\"Unit\"], [\"KM\"])[]]                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 2:

[] 

Add the below script in the same aspx file.

In the below code, you are binding the **UpdateUnitValue** function with the keyup event of the textbox. In **UpdateUnitValue**  function, you are calling the RollingGauge's clientside **SetUnit** method to update the gauge value dynamically.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        \$(document).ready([function] () {]                                                                                                                          |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [//Binding the function for changing the gauge value dynamically with the keyup event.]]                                                                |
|                                                                                                                                                                                                                                |
| [            \$([\"#Unit\"]).bind([\"keyup\"], UpdateUnitValue);]                                                                            |
|                                                                                                                                                                                                                                |
| [        });]                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [//Function to handle the keyup event of textbox.]]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        [function] UpdateUnitValue() {]                                                                                                                              |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//Gets the current value of the textbox.]]                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [var] val = \$([\"#Unit\"]).val();]                                                                                               |
|                                                                                                                                                                                                                                |
| [            [//Gets the gauge object.]]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [var] RollingGaugeObj = \$find([\'Gauge\']);]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//Calling the SetValue function to update the rolling gauge value.]]                                                                               |
|                                                                                                                                                                                                                                |
| [            RollingGaugeObj.SetUnit(val);]                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        }            ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [    [\</][script][\>]]                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 2:

Controller:

 

Add the code below in the controller

 

+----------------------------------------------------------------------------------------------------------------------------+
| []                                                                                     |
|                                                                                                                            |
| [        [public] [ActionResult] Index()] |
|                                                                                                                            |
| [        {]                                                                            |
|                                                                                                                            |
| [            [return] View();]                                    |
|                                                                                                                            |
| [        }]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

Step 4:

 Run the code to achieve the below output.

 

{border="0"}

Figure 149: Dynamic Updation of Unit[]


 

{border="0"} Note: Change the unit value in the textbox, to update the rolling gauge unit value.


[] 

[]{#related-topics}

