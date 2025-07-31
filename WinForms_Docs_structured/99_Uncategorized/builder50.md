---
title: builder50.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\builder50.md
created_at: 2025-07-03
---






#### Builder {#builder style="tab-stops: 0pt"}

[] 

To apply skins in any chart through Builder:

1.   In Controller, return view to the corresponding View page.

[] 


\[C#\]

[        [public] [ActionResult] SimpleChart()]

[        {            ]

[            [return] View();]

[        }]


[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

5.   Set the **Skins** property to any ChartModel Skins IEnumerable.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[cshtml\]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [    [\@{] Html.Chart([\"SimpleChart\"])]                                                                                                                                 |
|                                                                                                                                                                                                                                                                   |
| [      [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the Series, add the points to the series and set some stylings you want to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]                                   |
|                                                                                                                                                                                                                                                                   |
| **[.Skins([ChartModelSkins].Office2007Blue)][]**                                                                                                 |
|                                                                                                                                                                                                                                                                   |
| [    //\-\-\-\-\-\-\-\-\-\-\-\-- Set needed properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ] |
|                                                                                                                                                                                                                                                                   |
| **[             .]**[Render();]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [    [}]][]                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Build and run the application, to get the following output.

[] 

{border="0"}

Figure 305: Office 2007 Blue Skin

[]{#related-topics}

