---
title: anticlockwiserolling.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\anticlockwiserolling.md
created_at: 2025-07-03
---






##### AntiClockwiseRolling {#anticlockwiserolling style="tab-stops: 0pt"}

**[]** 

Rolling Gauge can be animated in Anticlockwise **Direction** by setting its **Direction** property to **Anticlockwise**.

 

###### 5.4.3.9.2.1 Through View Customization {#through-view-customization style="tab-stops: 0pt"}

 

Step 1:

View :

 

Rolling Gauge can be animated by recursively calling its ClientSide **SetValue()** function. Refer the below example to animate the rolling gauge.

Here, you are adding one button to start the Anticlockwise animation of rolling gauge. In the button click

event, you are recursively calling the ClientSide **SetValue()** function to animate the gauge.

Add the below code in your aspx file.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                              |
| [\<%][\--Rendering the rolling gauge\--][%\>][]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                              |
| [    [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                              |
| [         .Value([\"1000\"])]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                              |
| [      //][Setting the animation delay property to control the speed of the animation.][]                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                              |
| [         **.AnimationDelay(1000)**]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                              |
| [        //Setting the rolling direction to clockwise.][]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                              |
| **[         .Direction([Direction].AntiClockwise)]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                              |
| [          .IsAutomaticSegmentCountEnabled([true])]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [           .Height(50)]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| [         ]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                              |
| [    [%\>]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                              |
| [    [\<%][\--Adding the buttons for animating the gauge in its click event\--][%\>]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                              |
| [    ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                              |
| [        [\<][input] [type][=\"button\"] [id][=\"AntiClockwise\"] [value][=\"AntiClockwise Rolling\"] [/\>]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                              |
| [@\*][\--Rendering the rolling gauge\--][\*@][]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                              |
| [    [\@{] Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                              |
| [         .Value([\"1000\"])]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                              |
| [      //][Setting the animation delay property to control the speed of the animation.][]                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                              |
| [         **.AnimationDelay(1000)**]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                              |
| [        //Setting the rolling direction to clockwise.][]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                              |
| **[         .Direction([Direction].AntiClockwise)]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                              |
| [          .IsAutomaticSegmentCountEnabled([true])]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [           .Height(50).Render();         ]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                              |
| [    [}]]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                              |
| [    [@\*][\--Adding the buttons for animating the gauge in its click event\--][\*@]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                              |
| [    ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                              |
| [        [\<][input] [type][=\"button\"] [id][=\"AntiClockwise\"] [value][=\"AntiClockwise Rolling\"] [/\>]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

Step 2:

**[]** 

Add the below script in the same aspx file. In the button click event you are recursively calling the **Rolling()** function using **window.setInterval() method**. In the Rolling function, you are calling the Client side **SetValue()** function to update the gauge value dynamically.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [        [var] gauge_Value = 1000;]                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [        \$(document).ready([function] () {]                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//Binding the Rolling function for animating the gauge, with the button click event.]]                                                             |
|                                                                                                                                                                                                                                |
| [            \$([\"#AntiClockwise\"]).bind([\'click\'], [function] () {]                                                |
|                                                                                                                                                                                                                                |
| [                [//Recursively calling the Rolling function using window.setInterval() method.]]                                                                |
|                                                                                                                                                                                                                                |
| [                window.setInterval(Rolling, [\"1000\"]);]                                                                                                          |
|                                                                                                                                                                                                                                |
| [            });]                                                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [        });]                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| [        [//Function to handle the clockwise rolling.]]                                                                                                          |
|                                                                                                                                                                                                                                |
| [        [function] Rolling() {]                                                                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//Incrementing the gauge value.]]                                                                                                                  |
|                                                                                                                                                                                                                                |
| [            gauge_Value += 1;]                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [              //Converting the value to string.][]                                                                                  |
|                                                                                                                                                                                                                                |
| [            [var] value = String(gauge_Value);]                                                                                                                      |
|                                                                                                                                                                                                                                |
| [            [var] RollingGaugeObj = \$find([\'Gauge\']);]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//Calling the SetValue function to update the gauge value dynamically.]]                                                                           |
|                                                                                                                                                                                                                                |
| **[            RollingGaugeObj.SetValue(value);]**                                                                                                                                         |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        }            ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [    [\</][script][\>]]                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Controller:

Add the code below in the controller.

 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                         |
|                                                                                                                                                |
| [public][ [ActionResult] Index()] |
|                                                                                                                                                |
| [        {]                                                                                                |
|                                                                                                                                                |
| [            [return] View();]                                                        |
|                                                                                                                                                |
| [        }]                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 4:

Run the above code. You will get the following output.

 

{border="0"}

Figure 163: Rolling Gauge --AntiClockwise Animation**[]**


 

{border="0"} Note: Click AntiClockwise Rolling to animate the Rolling Gauge in AntiClockwise Direction.


**[]** 

###### 5.4.3.9.2.2 Through RollingGaugeModel {#through-rollinggaugemodel style="tab-stops: 0pt"}

[] 

Step 1:

View :

 

Add the below code in the aspx file. Here, you are adding one button to start the Anticlockwise animation of rolling gauge. In the button click event, you are recursively calling the ClientSide **SetValue()** function to animate the gauge.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| [@\*][\--Rendering the rolling gauge\--][\*@][]                                                                          |
|                                                                                                                                                                                                                                                                                                                                    |
| [@][Html.Syncfusion().RollingGauge([\"Gauge\"],[\"GaugeModel\"])][]                                  |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [        [@\*][\--Adding the buttons for animating the gauge in its click event\--][\*@]]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                    |
| [    ]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                    |
| [        [\<][input] [type][=\"button\"] [id][=\"Clockwise\"] [value][=\"Clockwise Rolling\"] [/]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

 

Add the below code in the same aspx file.

 

Add the below script in the same aspx file. In the button click event you are recursively calling the **Rolling()** function using **window.setInterval()** method. In the Rolling function, you are calling the Client side **SetValue()** function to update the gauge value dynamically.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [        [var] gauge_Value = 1000;]                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [        \$(document).ready([function] () {]                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//Binding the Rolling function for animating the gauge, with the button click event.]]                                                             |
|                                                                                                                                                                                                                                |
| [            \$([\"#AntiClockwise\"]).bind([\'click\'], [function] () {]                                                |
|                                                                                                                                                                                                                                |
| [                [//Recursively calling the Rolling function using window.setInterval() method.]]                                                                |
|                                                                                                                                                                                                                                |
| [                window.setInterval(Rolling, [\"1000\"]);]                                                                                                          |
|                                                                                                                                                                                                                                |
| [            });]                                                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [        });]                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| [        [//Function to handle the clockwise rolling.]]                                                                                                          |
|                                                                                                                                                                                                                                |
| [        [function] Rolling() {]                                                                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//Incrementing the gauge value.]]                                                                                                                  |
|                                                                                                                                                                                                                                |
| [            gauge_Value += 1;]                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [              //Converting the value to string.][]                                                                                  |
|                                                                                                                                                                                                                                |
| [            [var] value = String(gauge_Value);]                                                                                                                      |
|                                                                                                                                                                                                                                |
| [            [var] RollingGaugeObj = \$find([\'Gauge\']);]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//Calling the SetValue function to update the gauge value dynamically.]]                                                                           |
|                                                                                                                                                                                                                                |
| [            RollingGaugeObj.SetValue(value);]                                                                                                                                             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        }            ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [    [\</][script][\>]]                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 3:

Controller:

 

Add the below code in your controller.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [public][ [ActionResult] Index()]                                      |
|                                                                                                                                                                                     |
| [        {]                                                                                                                                     |
|                                                                                                                                                                                     |
| [           [RollingGaugeModel] roll_Gauge = [new] [RollingGaugeModel]();] |
|                                                                                                                                                                                     |
| [            [//Setting the animation delay property to control the speed of the animation.]]                             |
|                                                                                                                                                                                     |
| **[           roll_Gauge.AnimationDelay = 1000;]**                                                                                              |
|                                                                                                                                                                                     |
| [            [//Setting the rolling direction to clockwise.]]                                                             |
|                                                                                                                                                                                     |
| [           **roll_Gauge.Direction = [Direction].AntiClockwise;**]                                                      |
|                                                                                                                                                                                     |
| [            roll_Gauge.Value = [\"1000\"];]                                                                            |
|                                                                                                                                                                                     |
| [            roll_Gauge.IsAutomaticSegmentCountEnabled = [true];]                                                          |
|                                                                                                                                                                                     |
| [            roll_Gauge.Height = 50;]                                                                                                           |
|                                                                                                                                                                                     |
| [            roll_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                              |
|                                                                                                                                                                                     |
| [            ViewData\[[\"GaugeModel\"]\] = roll_Gauge;]                                                                |
|                                                                                                                                                                                     |
| [            [return] View();]                                                                                             |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [        }]                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 4:

Run the above code. You will get the below output.

[] 

{border="0"}

Figure 164: Rolling Gauge --AntiClockwise Animation**[]**


 

{border="0"} Note: Click AntiClockwise Rolling to animate the Rolling Gauge in AntiClockwise Direction.


 

[]{#related-topics}

