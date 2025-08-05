---
title: usingbuilder45.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder45.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Using Builder {#using-builder style="tab-stops: 0pt"}

The steps to create the Chart control in the View are as follows:*[]*

[1.   ]Right-click the **Views/Home** folder.

[2.   ]Click **Add**, and then select **View**.

[3.   ]Name the View, **SimpleChart**.

[4.   ]Add the following code in the SimpleChart.cshtml file, to create the Chart control in the View page.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [  ] [ [@(]]                                                                         |
|                                                                                                                                                                                                                    |
| [         Html.MobSyncfusion().Chart(\"Chart\")]                                                                                                                  |
|                                                                                                                                                                                                                    |
| [              .Series(series =\>]                                                                                                                                |
|                                                                                                                                                                                                                    |
| [              {]                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| [                  series.Add().Name(\"Seires 1\").Type(SeriesType.Column).Points(p =\>]                                                                          |
|                                                                                                                                                                                                                    |
| [                  {]                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [                      p.Add(1, 75);]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [                      p.Add(2, 82);]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [                      p.Add(3, 87);]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [                      p.Add(4, 84);]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [                      p.Add(5, 84);]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [                      . . . ]                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [                  });]                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [              }).Axes(axes =\>]                                                                                                                                  |
|                                                                                                                                                                                                                    |
| [              {]                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| [                  axes.PrimaryX(xaxis =\>]                                                                                                                       |
|                                                                                                                                                                                                                    |
| [                  {]                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [                      xaxis.Title(\"X-Title\");]                                                                                                                 |
|                                                                                                                                                                                                                    |
| [                  }).PrimaryY(yaxis =\>]                                                                                                                         |
|                                                                                                                                                                                                                    |
| [                  {]                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [                      yaxis.Title(\"Y-Title\");]                                                                                                                 |
|                                                                                                                                                                                                                    |
| [                  });]                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [              }).Size(new System.Drawing.Size(700,500)).Text(\"Simple Chart\").Font(new ChartFont(\"Arial\", \"15px\", ChartFontStyle.Bold)).ElementSpacing(10)] |
|                                                                                                                                                                                                                    |
| [)] []                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[5.   ]Open \~/Controllers/HomeController.cs.

[6.   ]Add the action displayed below.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [///] [] [\<summary\>] []                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [///] [ Used to create the simple chart] []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [///] [] [\</summary\>] []                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [///] [] [\<returns\>] [View page, it displays the Chart] [\</returns\>] [] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [public] [ [ActionResult] ] [SimpleChart] [()]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [return] [ View();]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [}[]]                                                                                                                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

7.   Run the application.

[] 

The following screenshot illustrates the sample output.

[] 

[] 

 

{border="0"} *[]*

Figure 29: Chart control added to the application

***[]***  

[]{#related-topics}

