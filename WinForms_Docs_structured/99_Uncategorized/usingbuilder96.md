---
title: usingbuilder96.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder96.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how you can enable the filtering feature using the EnableFiltering method:

1.   In **View**, invoke the Listbox Helper with the control ID as the first argument followed by the **EnableFiltering()**with the desired value as an argument.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [    ] [\<%] [Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                                                                                   |
| [          .**EnableFiltering([true])**]                                                                                                                 |
|                                                                                                                                                                                                                   |
| [           .Items(items =\>]                                                                                                                                                 |
|                                                                                                                                                                                                                   |
| [           {]                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| [               items.Add()]                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| [                   .Text([\"Windows 7\"]);]                                                                                                          |
|                                                                                                                                                                                                                   |
| [               items.Add()]                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| [                   .Text([\"Linux\"]);]                                                                                                              |
|                                                                                                                                                                                                                   |
| [               items.Add()]                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| [                   .Text([\"Ubuntu\"]);]                                                                                                             |
|                                                                                                                                                                                                                   |
| [               items.Add()]                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| [                   .Text([\"Solaris\"]);]                                                                                                            |
|                                                                                                                                                                                                                   |
| [               items.Add()]                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| [                   .Text([\"Android\"]);]                                                                                                            |
|                                                                                                                                                                                                                   |
| [               items.Add()]                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| [                   .Text([\"Eclipse\"]);]                                                                                                            |
|                                                                                                                                                                                                                   |
| [               items.Add()]                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| [                   .Text([\"Unix\"]);]                                                                                                               |
|                                                                                                                                                                                                                   |
| [           })]                                                                                                                                                               |
|                                                                                                                                                                                                                   |
| [     .Render();]                                                                                                                                                             |
|                                                                                                                                                                                                                   |
| [    [%\>]]                                                                                                                                       |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                     |
|                                                                                                                                                         |
| **[]**                                                                                                              |
|                                                                                                                                                         |
| [    [\@{]]                                                                             |
|                                                                                                                                                         |
| [        ] [Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                         |
| [          **.EnableFiltering([true])**]                                                       |
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
| [               items.Add()]                                                                                        |
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
| [               items.Add()]                                                                                        |
|                                                                                                                                                         |
| [                   .Text([\"Unix\"]);]                                                     |
|                                                                                                                                                         |
| [           })]                                                                                                     |
|                                                                                                                                                         |
| [.Render();]                                                                                                        |
|                                                                                                                                                         |
| [    [}]]                                                                               |
|                                                                                                                                                         |
| []                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   Build and run the application.

 

[] 

{border="0"}

Figure 10 :ListBox - Filtering[]

 

 

{border="0"}

Figure 11 :ListBox -- Filtered Items[]

 

**[]**  

[]{#related-topics}

