---
title: usingbuilder94.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder94.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how to implement an item type for the listbox control:

1.   In **View**, invoke the Listbox Helper with the control ID as the first argument and configure the ListBox item with the specified item type, using the **ItemType()**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [    ] [\<%] [=] [ Html.MobSyncfusion().ListBox([\"list\"])] |
|                                                                                                                                                                                                                                                                       |
| [           .Items(items =\>]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                       |
| [           {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                  .Text([\"A\"]).**ItemType([ItemType].Divider);**]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                   .Text([\"Android\"]);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                  .Text([\"E\"]).**ItemType([ItemType].Divider);**]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                  .Text([\"Eclipse\"]);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                  .Text([\"L\"]).**ItemType([ItemType].Divider);**]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                  .Text([\"Linux\"]);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                  .Text([\"S\"]).**ItemType([ItemType].Divider);**]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                   .Text([\"Solaris\"]);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                  .Text([\"U\"]).**ItemType([ItemType].Divider);**]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                   .Text([\"Ubuntu\"]);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                   .Text([\"Unix\"]);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                  .Text([\"W\"]).**ItemType([ItemType].Divider);**]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [               items.Add()]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [                   .Text([\"Windows\"]);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [           })]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [     ]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [    [%\>]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                      |
|                                                                                                                                                          |
| **[]**                                                                                                               |
|                                                                                                                                                          |
| [    [\@{]]                                                                              |
|                                                                                                                                                          |
| [        ] [Html.MobSyncfusion().ListBox([\"list\"])]    |
|                                                                                                                                                          |
| [           .Items(items =\>]                                                                                        |
|                                                                                                                                                          |
| [           {]                                                                                                       |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                  .Text([\"A\"]).**ItemType([ItemType].Divider);**] |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                   .Text([\"Android\"]);]                                                   |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                  .Text([\"E\"]).**ItemType([ItemType].Divider);**] |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                  .Text([\"Eclipse\"]);]                                                    |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                  .Text([\"L\"]).**ItemType([ItemType].Divider);**] |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                  .Text([\"Linux\"]);]                                                      |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                  .Text([\"S\"]).**ItemType([ItemType].Divider);**] |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                   .Text([\"Solaris\"]);]                                                   |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                  .Text([\"U\"]).**ItemType([ItemType].Divider);**] |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                   .Text([\"Ubuntu\"]);]                                                    |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                   .Text([\"Unix\"]);]                                                      |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                  .Text([\"W\"]).**ItemType([ItemType].Divider);**] |
|                                                                                                                                                          |
| [               items.Add()]                                                                                         |
|                                                                                                                                                          |
| [                   .Text([\"Windows\"]);]                                                   |
|                                                                                                                                                          |
| [           })]                                                                                                      |
|                                                                                                                                                          |
| [.Render();]                                                                                                         |
|                                                                                                                                                          |
| [    [}]]                                                                                |
|                                                                                                                                                          |
| []                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   Build and run the application.

 

[ {border="0"} ]

Figure 62: Listbox - Divider[]

 

**[]**  

[]{#related-topics}

