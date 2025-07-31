---
title: usingbuilder92.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder92.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how to set the styles for the Listbox control:

1.   In **View**, invoke the Listbox helper with the Control ID as the first argument followed by the **ListStyleand ListItemStyle** methods with the desired value as an argument.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [    ] [\<%] [=] [ Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                                                                                                                                         |
| **[            .ListStyle([ListStyle].Numbered)]**                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| **[            .ListItemStyle([ListItemStyle].Option)]**                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [           .Items(items =\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [           {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Windows 7\"]);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Linux\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Ubuntu\"]);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Solaris\"]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Android\"]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Eclipse\"]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Unix\"]);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [           })]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [     ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [    [%\>]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                     |
|                                                                                                                                                         |
| **[]**                                                                                                              |
|                                                                                                                                                         |
| [    [\@{]]                                                                             |
|                                                                                                                                                         |
| [        ] [Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                         |
| **[            .ListStyle([ListStyle].Numbered)]**                                          |
|                                                                                                                                                         |
| **[            .ListItemStyle([ListItemStyle].Option)]**                                    |
|                                                                                                                                                         |
| [           .Items(items =\>]                                                                                       |
|                                                                                                                                                         |
| [           {]                                                                                                      |
|                                                                                                                                                         |
| [               items.Add()]                                                                                        |
|                                                                                                                                                         |
| [                   .Text([\"Windows 7\"]);]                                                |
|                                                                                                                                                         |
| [               items.Add()]                                                                                        |
|                                                                                                                                                         |
| [                   .Text([\"Linux\"]);]                                                    |
|                                                                                                                                                         |
| [               items.Add()]                                                                                        |
|                                                                                                                                                         |
| [                   .Text([\"Ubuntu\"]);]                                                   |
|                                                                                                                                                         |
| [               items.Add()]                                                                                        |
|                                                                                                                                                         |
| [                   .Text([\"Solaris\"]);]                                                  |
|                                                                                                                                                         |
| [               items.Add()]                                                                                        |
|                                                                                                                                                         |
| [                   .Text([\"Android\"]);]                                                  |
|                                                                                                                                                         |
| [               items.Add()]                                                                                        |
|                                                                                                                                                         |
| [                   .Text([\"Eclipse\"]);]                                                  |
|                                                                                                                                                         |
| [               items.Add()]                                                                                        |
|                                                                                                                                                         |
| [                   .Text([\"Unix\"]);]                                                     |
|                                                                                                                                                         |
| [           })]                                                                                                     |
|                                                                                                                                                         |
| [.Render();]                                                                                                        |
|                                                                                                                                                         |
| [    [}]] []                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

 

[] 

[ {border="0"} ]

Figure 59: Numbered List[]

 

**[]**  

[]{#related-topics}

