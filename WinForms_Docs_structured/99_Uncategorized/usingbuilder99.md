---
title: usingbuilder99.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder99.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the setting of the Syncfusion themes to Listbox using Builder.

1.   In **View** invoke the Listbox helper with the Control ID as first argument followed by the **AutoFormat** method with the desired theme as the argument.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                              |
|                                                                                                                                                                                                                         |
| [          ] [\<%] [Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                                                                                         |
| [           **.AutoFormat( [MobSkins].DarkNight)**]                                                                                                         |
|                                                                                                                                                                                                                         |
| [           .Items(items =\>]                                                                                                                                                       |
|                                                                                                                                                                                                                         |
| [           {]                                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [                   .Text([\"Windows 7\"]);]                                                                                                                |
|                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [                   .Text([\"Linux\"]);]                                                                                                                    |
|                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [                   .Text([\"Ubuntu\"]);]                                                                                                                   |
|                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [                   .Text([\"Solaris\"]);]                                                                                                                  |
|                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [                   .Text([\"Android\"]);]                                                                                                                  |
|                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [                   .Text([\"Eclipse\"]);]                                                                                                                  |
|                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [                   .Text([\"Unix\"]);]                                                                                                                     |
|                                                                                                                                                                                                                         |
| [           })]                                                                                                                                                                     |
|                                                                                                                                                                                                                         |
| [     .Render();]                                                                                                                                                                   |
|                                                                                                                                                                                                                         |
| [    [%\>]]                                                                                                                                             |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                        |
|                                                                                                                                                            |
| **[]**                                                                                                                 |
|                                                                                                                                                            |
| [        [\@{]]                                                                            |
|                                                                                                                                                            |
| [           ] [Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                            |
| [           **.AutoFormat( [MobSkins].DarkNight)**]                                            |
|                                                                                                                                                            |
| [           .Items(items =\>]                                                                                          |
|                                                                                                                                                            |
| [           {]                                                                                                         |
|                                                                                                                                                            |
| [               items.Add()]                                                                                           |
|                                                                                                                                                            |
| [                   .Text([\"Windows 7\"]);]                                                   |
|                                                                                                                                                            |
| [               items.Add()]                                                                                           |
|                                                                                                                                                            |
| [                   .Text([\"Linux\"]);]                                                       |
|                                                                                                                                                            |
| [               items.Add()]                                                                                           |
|                                                                                                                                                            |
| [                   .Text([\"Ubuntu\"]);]                                                      |
|                                                                                                                                                            |
| [               items.Add()]                                                                                           |
|                                                                                                                                                            |
| [                   .Text([\"Solaris\"]);]                                                     |
|                                                                                                                                                            |
| [               items.Add()]                                                                                           |
|                                                                                                                                                            |
| [                   .Text([\"Android\"]);]                                                     |
|                                                                                                                                                            |
| [               items.Add()]                                                                                           |
|                                                                                                                                                            |
| [                   .Text([\"Eclipse\"]);]                                                     |
|                                                                                                                                                            |
| [               items.Add()]                                                                                           |
|                                                                                                                                                            |
| [                   .Text([\"Unix\"]);]                                                        |
|                                                                                                                                                            |
| [           })]                                                                                                        |
|                                                                                                                                                            |
| [     .Render();]                                                                                                      |
|                                                                                                                                                            |
| [}]                                                                                                |
|                                                                                                                                                            |
| []                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

 

[] 

[ {border="0"} ]

Figure 68: ListBox[]

 

 

**[]**  

[]{#related-topics}

