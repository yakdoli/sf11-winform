---
title: throughviewcustomization21.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughviewcustomization21.md
created_at: 2025-07-03
---






##### Through View Customization {#through-view-customization style="tab-stops: 0pt"}

[] 

Step 1:

View:

 

Add the below code in the aspx file.

The **SegmentCount** property is used to set the segment count value for Rolling Gauge. Here we are adding the text box for updating the segment count value dynamically in its keyup event.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| [   [\<%][\--Rendering the rolling gauge\--][%\>]]                                                      |
|                                                                                                                                                                                                                               |
| [    [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                        |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [         .Value([\"Gauge\"])]                                                                                                                                    |
|                                                                                                                                                                                                                               |
| [             [//Setting the segment count value.]]                                                                                                                 |
|                                                                                                                                                                                                                               |
| [          .SegmentCount(5)]                                                                                                                                                              |
|                                                                                                                                                                                                                               |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                       |
|                                                                                                                                                                                                                               |
| [         .Height(50)]                                                                                                                                                                    |
|                                                                                                                                                                                                                               |
| [         ]                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| [    [%\>]]                                                                                                                                                   |
|                                                                                                                                                                                                                               |
| [    [\<%][\--Adding the text box for updating the gauge unit value in its keyup event\--][%\>]]        |
|                                                                                                                                                                                                                               |
| [    [\<%][=]Html.TextBox([\"SegmentCount\"], [\"5\"])[%\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [   [@\*][\--Rendering the rolling gauge\--][\*@]]                                               |
|                                                                                                                                                                                                                        |
| [    [\@{] Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                        |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [         .Value([\"Gauge\"])]                                                                                                                             |
|                                                                                                                                                                                                                        |
| [             [//Setting the segment count value.]]                                                                                                          |
|                                                                                                                                                                                                                        |
| [          .SegmentCount(5)]                                                                                                                                                       |
|                                                                                                                                                                                                                        |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                |
|                                                                                                                                                                                                                        |
| [         .Height(50).Render();         ]                                                                                                                                          |
|                                                                                                                                                                                                                        |
| [    [}]]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [    [@\*][\--Adding the text box for updating the gauge unit value in its keyup event\--][\*@]] |
|                                                                                                                                                                                                                        |
| [    [@]Html.TextBox([\"SegmentCount\"], [\"5\"])[]]                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

[] 

Add the below script in the same aspx file.

In the below code, you are binding the **UpdateSegmentCount** function with the keyup event of the textbox. In the **UpdateSegmentCount ()** function, we are calling the RollingGauge clientside **SetSegmentCount** method to update the SegmentCount value dynamically.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
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
| [            \$([\"#SegmentCount\"]).bind([\"keyup\"], UpdateSegmentCount);]                                                                 |
|                                                                                                                                                                                                                                |
| [        });]                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [//Function to handle the keyup event of textbox.]]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        [function] UpdateSegmentCount() {]                                                                                                                           |
|                                                                                                                                                                                                                                |
| [           ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| [            [//Gets the current value of the textbox.]]                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [var] count = \$([\"#SegmentCount\"]).val();]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [var] Seg_count = parseInt(count);]                                                                                                                      |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//Gets the gauge object.]]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [var] RollingGaugeObj = \$find([\'Gauge\']);]                                                                                     |
|                                                                                                                                                                                                                                |
| [            RollingGaugeObj.\_Value = [\"Gauge\"];]                                                                                                                |
|                                                                                                                                                                                                                                |
| [            [//Calling the SetSegmentCount function to update the rolling gauge Segment based in its count.]]                                                   |
|                                                                                                                                                                                                                                |
| [            RollingGaugeObj.SetSegmentCount(Seg_count);]                                                                                                                                  |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| [    [\</][script][\>]]                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Controller:

 

Add the code below in the controller

 

+----------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                 |
|                                                                                                                            |
| [        [public] [ActionResult] Index()] |
|                                                                                                                            |
| [        {]                                                                            |
|                                                                                                                            |
| [            [return] View();]                                    |
|                                                                                                                            |
| [        }]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

Step 4:

Run the code to achieve the below output.

 

{border="0"}

Figure 151: Dynamic Updation of SegmentCount**[]**

[                               ]

[]{#related-topics}

