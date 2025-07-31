---
title: usingbuilder95.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder95.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how you can use the above property to display the child count:

1.   In **View**, invoke the Listbox Helper with the control ID as the first argument followed by the **ShowChildCount()** with the desired value as an argument.

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
| **[                    .ShowChildCount([true])]**                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [                   .Children(child=\>]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [                       {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [                           child.Add().Text([\"Windows XP\"]);]                                                                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [                           child.Add().Text([\"Windows Vista\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [                           child.Add().Text([\"Windows 7\"]);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [                       });]                                                                                                                                                                                                        |
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
| [                    .Text([\"Android\"])]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| **[                    .ShowChildCount([true])]**                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| **[                   ]** [.Children(child =\>]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [                   {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [                       child.Add().Text([\"Android 1.0\"]);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [                       child.Add().Text([\"Android 2.0\"]);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [                   });]                                                                                                                                                                                                            |
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
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
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
| **[                    .ShowChildCount([true])]**                                              |
|                                                                                                                                                         |
| [                   .Children(child=\>]                                                                             |
|                                                                                                                                                         |
| [                       {]                                                                                          |
|                                                                                                                                                         |
| [                           child.Add().Text([\"Windows XP\"]);]                            |
|                                                                                                                                                         |
| [                           child.Add().Text([\"Windows Vista\"]);]                         |
|                                                                                                                                                         |
| [                           child.Add().Text([\"Windows 7\"]);]                             |
|                                                                                                                                                         |
| [                       });]                                                                                        |
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
| [                   .Text([\"Android\"])]                                                   |
|                                                                                                                                                         |
| **[                    .ShowChildCount([true])]**                                              |
|                                                                                                                                                         |
| [                   .Children(child =\>]                                                                            |
|                                                                                                                                                         |
| [                   {]                                                                                              |
|                                                                                                                                                         |
| [                       child.Add().Text([\"Android 1.0\"]);]                               |
|                                                                                                                                                         |
| [                       child.Add().Text([\"Android 2.0\"]);]                               |
|                                                                                                                                                         |
| [                   });]                                                                                            |
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
| [    [}]]                                                                               |
|                                                                                                                                                         |
| []                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

 

[] 

[ {border="0"} ]

Figure 10 :ListBox - Displaying Child Count[]

 

**[]**  

[]{#related-topics}

