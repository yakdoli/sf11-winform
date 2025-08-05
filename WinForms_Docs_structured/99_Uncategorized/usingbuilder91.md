---
title: usingbuilder91.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder91.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the adding Listbox to an application using Builder:

1.   In **View**, invoke the Listbox helper with the Control ID as the first argument and add the list items with the help of items Add() method and configure item properties as required.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [    ] [\<%] [Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                                                                                   |
| [          ** .Items(items =\>**]                                                                                                                                             |
|                                                                                                                                                                                                                   |
| **[           {]**                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| **[               items.Add()]**                                                                                                                                              |
|                                                                                                                                                                                                                   |
| **[                   .Text([\"Windows 7\"]);]**                                                                                                      |
|                                                                                                                                                                                                                   |
| **[               items.Add()]**                                                                                                                                              |
|                                                                                                                                                                                                                   |
| **[                   .Text([\"Linux\"]);]**                                                                                                          |
|                                                                                                                                                                                                                   |
| **[               items.Add()]**                                                                                                                                              |
|                                                                                                                                                                                                                   |
| **[                   .Text([\"Ubuntu\"]);]**                                                                                                         |
|                                                                                                                                                                                                                   |
| **[               items.Add()]**                                                                                                                                              |
|                                                                                                                                                                                                                   |
| **[                   .Text([\"Solaris\"]);]**                                                                                                        |
|                                                                                                                                                                                                                   |
| **[               items.Add()]**                                                                                                                                              |
|                                                                                                                                                                                                                   |
| **[                   .Text([\"Android\"]);]**                                                                                                        |
|                                                                                                                                                                                                                   |
| **[               items.Add()]**                                                                                                                                              |
|                                                                                                                                                                                                                   |
| **[                   .Text([\"Eclipse\"]);]**                                                                                                        |
|                                                                                                                                                                                                                   |
| **[               items.Add()]**                                                                                                                                              |
|                                                                                                                                                                                                                   |
| **[                   .Text([\"Unix\"]);]**                                                                                                           |
|                                                                                                                                                                                                                   |
| **[           })]**                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [     .Render();]                                                                                                                                                             |
|                                                                                                                                                                                                                   |
| [    [%\>]]                                                                                                                                       |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [    ] [\@{] [Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                                                                                   |
| [           **.Items(items =\>**]                                                                                                                                             |
|                                                                                                                                                                                                                   |
| **[               {]**                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| **[                   items.Add()]**                                                                                                                                          |
|                                                                                                                                                                                                                   |
| **[                       .Text([\"Windows 7\"]);]**                                                                                                  |
|                                                                                                                                                                                                                   |
| **[                   items.Add()]**                                                                                                                                          |
|                                                                                                                                                                                                                   |
| **[                       .Text([\"Linux\"]);]**                                                                                                      |
|                                                                                                                                                                                                                   |
| **[                   items.Add()]**                                                                                                                                          |
|                                                                                                                                                                                                                   |
| **[                       .Text([\"Ubuntu\"]);]**                                                                                                     |
|                                                                                                                                                                                                                   |
| **[                   items.Add()]**                                                                                                                                          |
|                                                                                                                                                                                                                   |
| **[                       .Text([\"Solaris\"]);]**                                                                                                    |
|                                                                                                                                                                                                                   |
| **[                   items.Add()]**                                                                                                                                          |
|                                                                                                                                                                                                                   |
| **[                       .Text([\"Android\"]);]**                                                                                                    |
|                                                                                                                                                                                                                   |
| **[                   items.Add()]**                                                                                                                                          |
|                                                                                                                                                                                                                   |
| **[                    .Text([\"Eclipse\"]);]**                                                                                                       |
|                                                                                                                                                                                                                   |
| **[                   items.Add()]**                                                                                                                                          |
|                                                                                                                                                                                                                   |
| **[                     .Text([\"Unix\"]);]**                                                                                                         |
|                                                                                                                                                                                                                   |
| **[               })]**                                                                                                                                                       |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [           .Render();]                                                                                                                                                       |
|                                                                                                                                                                                                                   |
| [    [}]]                                                                                                                                         |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

The output is shown in the following screenshot.[]

[ {border="0"} ]

Figure 57: ListBox[]

 

**[]**  

[]{#related-topics}

