---
title: usingbuilder93.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder93.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how you can implement the nested list:

1.   In **View**, invoke the Listbox helper with the Control ID as the first argument and add the child items for specific items through the Children()

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [    ] [\<%] [=] [ Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                                                                                                                                         |
| [            .ListStyle([ListStyle].Numbered)]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [            .ListItemStyle([ListItemStyle].Option)]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [           .Items(items =\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [           {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Windows\"])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [                   **.Children(child=\>**]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| **[                       {]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| **[                           child.Add().Text([\"Windows XP\"]);]**                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| **[                           child.Add().Text([\"Windows Vista\"]);]**                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| **[                           child.Add().Text([\"Windows 7\"]);]**                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| **[                       });]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Linux\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Ubuntu\"]);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Solaris\"]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Android\"])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| **[                   .Children(child =\>]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| **[                   {]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| **[                       child.Add().Text([\"Android 1.0\"]);]**                                                                                                                                           |
|                                                                                                                                                                                                                                                                         |
| **[                       child.Add().Text([\"Android 2.0\"]);]**                                                                                                                                           |
|                                                                                                                                                                                                                                                                         |
| **[                   });]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Eclipse\"]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [               items.Add()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [                   .Text([\"Unix\"]);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [           })]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [     ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [    [%\>]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                     |
|                                                                                                                                                         |
| **[]**                                                                                                              |
|                                                                                                                                                         |
| [    [\@{]]                                                                             |
|                                                                                                                                                         |
| [        ] [Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                         |
| [            .ListStyle([ListStyle].Numbered)]                                              |
|                                                                                                                                                         |
| [            .ListItemStyle([ListItemStyle].Option)]                                        |
|                                                                                                                                                         |
| [           .Items(items =\>]                                                                                       |
|                                                                                                                                                         |
| [           {]                                                                                                      |
|                                                                                                                                                         |
| [               items.Add()]                                                                                        |
|                                                                                                                                                         |
| [                   .Text([\"Windows\"])]                                                   |
|                                                                                                                                                         |
| [                   **.Children(child=\>**]                                                                         |
|                                                                                                                                                         |
| **[                       {]**                                                                                      |
|                                                                                                                                                         |
| **[                           child.Add().Text([\"Windows XP\"]);]**                        |
|                                                                                                                                                         |
| **[                           child.Add().Text([\"Windows Vista\"]);]**                     |
|                                                                                                                                                         |
| **[                           child.Add().Text([\"Windows 7\"]);]**                         |
|                                                                                                                                                         |
| **[                       });]** []                                             |
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
| [                   .Text([\"Android\"])]                                                   |
|                                                                                                                                                         |
| [                   **.Children(child =\>**]                                                                        |
|                                                                                                                                                         |
| **[                   {]**                                                                                          |
|                                                                                                                                                         |
| **[                       child.Add().Text([\"Android 1.0\"]);]**                           |
|                                                                                                                                                         |
| **[                       child.Add().Text([\"Android 2.0\"]);]**                           |
|                                                                                                                                                         |
| **[                   });]**                                                                                        |
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
| [    [}]] []                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   Build and run the application.

 

[] 

[ {border="0"} ]

Figure 60:Nested List

[] 

[] 

[] 

[] 

[ {border="0"} ]

Figure 61: Nested List - Sub item[]

 

[]{#related-topics}

