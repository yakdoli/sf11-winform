---
title: clientsidemethods15.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsidemethods15.md
created_at: 2025-07-03
---






#### Client-Side Methods {#client-side-methods style="tab-stops: 0pt"}

 

The waiting pop-up control has a rich set of client-side methods to modify its behavior at run time.

**[]** 

**[Methods]**

 

  ----------------------------------- -------------------------------------------------------- ------------- ------------------------------------------------------ ----------------
  Name                                Parameters                                               Return type   Description                                            Reference Link
  ShowPopUp                           NA                                                       NA            Displays the waiting pop-up over the target element.   NA
  HidePopUp[]   NA                                                       NA            Hides the waiting pop-up.                              NA
  SetBackgroundColor                   Color -- the desired color name or hexadecimal value.   NA            Sets the background color of the pop-up panel.         NA
  SetTransparency                     Value -- the desired value of opacity in numbers.        NA            Sets the opacity of the pop-up panel.                  NA
  ----------------------------------- -------------------------------------------------------- ------------- ------------------------------------------------------ ----------------

[] 

The following steps explain how to use these methods.

1.   In **View**, create the target element over which the waiting pop-up is to be displayed.

2.   Invoke the waiting pop-up helper followed by the **TargetId** method with the ID of the target element as an argument.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [      [\<][div] [id][=\"targetArea\"] [style][=\"][width][: 300px; ][height][: 150px;\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][div][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            User Name:]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<%][=]Html.Syncfusion().TextBox([\"userName\"]) [%\>][\</][div][\>]]                                                    |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][div][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            Password:]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<%][=]Html.Syncfusion().Password([\"password\"]) [%\>][\</][div][\>]]                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| [      [\</][div][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [      [\<%][=]Html.Syncfusion().WaitingPopup([\"myPopup\"]).TargetId([\"targetArea\"]) [%\>]]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\][]**                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [      [\<][div] [id][=\"targetArea\"] [style][=\"][width][: 300px; ][height][: 150px;\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][div][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            User Name:]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [@]Html.Syncfusion().TextBox([\"userName\"])[\</][div][\>]]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][div][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            Password:]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [@]Html.Syncfusion().Password([\"password\"])[\</][div][\>]]                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [      [\</][div][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\@{][ Html.Syncfusion().WaitingPopup([\"myPopup\"]).TargetId([\"targetArea\"]).Render();[}]]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

3.   In JavaScript, use the methods as seen in the following code.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [        [function] Show() {]                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            \$find([\"myPopup\"]).ShowPopUp();]                                                                                                                    |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] Hide() {]                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            \$find([\"myPopup\"]).HidePopUp();]                                                                                                                    |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] Options() {]                                                                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//create an instance of the waiting pop-up client-side object]]                                                                                    |
|                                                                                                                                                                                                                                |
| [            [var] waitingObj = \$find([\"myPopup\"]);]                                                                                        |
|                                                                                                                                                                                                                                |
| [            [//code to set the background color]]                                                                                                               |
|                                                                                                                                                                                                                                |
| [            waitingObj.SetBackgroundColor([\"Blue\"]);]                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//code to set the transparency]]                                                                                                                   |
|                                                                                                                                                                                                                                |
| [            waitingObj.SetTransparency(5);]                                                                                                                                               |
|                                                                                                                                                                                                                                |
| [        }    ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [      [\</][script][\>]]                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application.

[]{#related-topics}

