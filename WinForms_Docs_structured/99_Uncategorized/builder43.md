---
title: builder43.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\builder43.md
created_at: 2025-07-03
---






#### Builder {#builder style="tab-stops: 0pt"}

[] 

To create a chart containing an Opposed Axis through Builder:

1.   In Controller, return view to the corresponding View page.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                           |
|                                                                                                                                  |
| [        [public] [ActionResult] SimpleChart()] |
|                                                                                                                                  |
| [        {            ]                                                                      |
|                                                                                                                                  |
| [            [return] View();]                                          |
|                                                                                                                                  |
| [        }]                                                                                  |
|                                                                                                                                  |
| []                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the Series to the ChartModel and set the series type to Line, and add the Points to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

5.   Set the OpposedPosition of the PrimaryYAxis to true.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View\[ASPX\]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                   |
| [    [\<%][=] Html.Chart([\"SimpleChart\"]).Series(series =\>{})]                                                                                                       |
|                                                                                                                                                                                                                                                                                                   |
| [              [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the remaining Points to the series and set some stylings you want to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]                                                    |
|                                                                                                                                                                                                                                                                                                   |
| **[                     .PrimaryYAxis(yaxis =\> {]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                   |
| **[                          yaxis.OpposedPosition([true]);]**                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                   |
| **[                      })]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                   |
| [    //\-\-\-\-\-\-\-\-\-\-\-\-- Set the required properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ] |
|                                                                                                                                                                                                                                                                                                   |
| [        ]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                   |
| [    [%\>][]]                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View\[cshtml\][]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                   |
| [    [\@{] Html.Chart([\"SimpleChart\"]).Series(series =\>{]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                   |
| [            })]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                   |
| [              [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the remaining points to the series and set some stylings you want to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]                                                    |
|                                                                                                                                                                                                                                                                                                   |
| **[                     .PrimaryYAxis(yaxis =\> {]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                   |
| **[                          yaxis.OpposedPosition([true]);]**                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                   |
| **[                      })]**[.Render();]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                   |
| [    //\-\-\-\-\-\-\-\-\-\-\-\-- Set the required properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ] |
|                                                                                                                                                                                                                                                                                                   |
| [        ]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                   |
| [    [}][]]                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

6.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 263: Column chart Opposed Y Axis

[] 

[]{#related-topics}

