---
title: builder49.md
original_path: WinForms_Docs/99_Uncategorized/builder49.md
created_at: 2025-08-05
---






#### Builder {#builder style="tab-stops: 0pt"}

[] 

To create legend customization in any chart through Builder:

1.   In Controller, return view to the corresponding View page.

[] 


\[C#\]

[        [public] [ActionResult] SimpleChart()]

[        {            ]

[            [return] View();]

[        }]


[] 

2.   In the View Page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

5.   Set the Legend related properties, as shown in the code snippet displayed below.

[] 


View \[ASPX\]

[    [\<%][=] Html.Chart([\"SimpleChart\"])]

[      [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the Series, add the points to the series and set some stylings you want to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]

**[              .ShowLegend([true])]**

**[              .LegendsPlacement(Syncfusion.Windows.Forms.Chart.[ChartPlacement].Outside)]**

**[              .LegendPosition(Syncfusion.Windows.Forms.Chart.[ChartDock].Top)]**

**[              .Legend(legend =\>{]**

**[                  legend.Alignment(Syncfusion.Windows.Forms.Chart.[ChartAlignment].Center);]**

**[              })]**

**[]** 

[    //\-\-\-\-\-\-\-\-\-\-\-\-- Set the required properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ]

**[]** 

[    [%\>]]


[] 


View \[cshtml\]

[    [\@{] Html.Chart([\"SimpleChart\"])]

[      [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the Series, add the points to the series and set some stylings you want to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]

**[              .ShowLegend([true])]**

**[              .LegendsPlacement(Syncfusion.Windows.Forms.Chart.[ChartPlacement].Outside)]**

**[              .LegendPosition(Syncfusion.Windows.Forms.Chart.[ChartDock].Top)]**

**[              .Legend(legend =\>{]**

**[                  legend.Alignment(Syncfusion.Windows.Forms.Chart.[ChartAlignment].Center);]**

**[              })]**[.Render();]

**[]** 

[    //\-\-\-\-\-\-\-\-\-\-\-\-- Set needed properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ]

**[]** 

[    [}]]


 

 

6.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 302: Legend Position Top, Alignment Center, and Placement as Outside

[]{#related-topics}

