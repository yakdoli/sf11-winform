---
title: usingbuilder100.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder100.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the handling of client side events of the Listbox using Builder.

1.   In the **View**, invoke the Listbox helper with the Control ID as the first argument followed by the event handler methods with the desired handlers as argument.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| **[\[ASPX\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [    ] [\<%] [Html.MobSyncfusion().ListBox([\"lbCore\"])] |
|                                                                                                                                                                                                                   |
| [          **.OnButtonClick([\"OnButtonClick\"])**]                                                                                                   |
|                                                                                                                                                                                                                   |
| **[          .OnItemSelect([\"OnItemSelect\"])]**                                                                                                     |
|                                                                                                                                                                                                                   |
| **[          .OnListLoad([\"OnListLoad\"])]**                                                                                                         |
|                                                                                                                                                                                                                   |
| [           .Items(items =\>]                                                                                                                                                 |
|                                                                                                                                                                                                                   |
| [           {]                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| [               items.Add()]                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| [                   .Text([\"Windows 7\"]).Children(ch =\> { ch.Add().Text([\"hjgghf\"]); });]                                |
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
| **[]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                |
|                                                                                                                                                                                    |
| **[]**                                                                                                                                         |
|                                                                                                                                                                                    |
| [       [\@{]]                                                                                                     |
|                                                                                                                                                                                    |
| [           ] [Html.MobSyncfusion().ListBox([\"lbCore\"])]                         |
|                                                                                                                                                                                    |
| [          **.OnButtonClick([\"OnButtonClick\"])**]                                                                    |
|                                                                                                                                                                                    |
| **[          .OnItemSelect([\"OnItemSelect\"])]**                                                                      |
|                                                                                                                                                                                    |
| **[          .OnListLoad([\"OnListLoad\"])]**                                                                          |
|                                                                                                                                                                                    |
| [           .Items(items =\>]                                                                                                                  |
|                                                                                                                                                                                    |
| [           {]                                                                                                                                 |
|                                                                                                                                                                                    |
| [               items.Add()]                                                                                                                   |
|                                                                                                                                                                                    |
| [                   .Text([\"Windows 7\"]).Children(ch =\> { ch.Add().Text([\"hjgghf\"]); });] |
|                                                                                                                                                                                    |
| [               items.Add()]                                                                                                                   |
|                                                                                                                                                                                    |
| [                   .Text([\"Linux\"]);]                                                                               |
|                                                                                                                                                                                    |
| [               items.Add()]                                                                                                                   |
|                                                                                                                                                                                    |
| [                   .Text([\"Ubuntu\"]);]                                                                              |
|                                                                                                                                                                                    |
| [               items.Add()]                                                                                                                   |
|                                                                                                                                                                                    |
| [                   .Text([\"Solaris\"]);]                                                                             |
|                                                                                                                                                                                    |
| [               items.Add()]                                                                                                                   |
|                                                                                                                                                                                    |
| [                   .Text([\"Android\"]);]                                                                             |
|                                                                                                                                                                                    |
| [               items.Add()]                                                                                                                   |
|                                                                                                                                                                                    |
| [                   .Text([\"Eclipse\"]);]                                                                             |
|                                                                                                                                                                                    |
| [               items.Add()]                                                                                                                   |
|                                                                                                                                                                                    |
| [                   .Text([\"Unix\"]);]                                                                                |
|                                                                                                                                                                                    |
| [           })]                                                                                                                                |
|                                                                                                                                                                                    |
| [     .Render();]                                                                                                                              |
|                                                                                                                                                                                    |
| [}]                                                                                                                        |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In the **Javascript**, define the handlers as given below.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| **[\[Javascript\]]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| **[  ]** [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [      function] [ OnListLoad(event, model) {]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [        ] [//event --\> event object.] []                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [        ] [//Model --\> Listbox model object] []                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [       function] [ OnButtonClick(event, Model) {]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [        ] [//event --\> event object.] []                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [        ] [//Model --\> Listbox model object] []                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [            ]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        [function] OnItemSelect(event, data) {]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                 |
| [        ] [//event -- event object.] []                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        ] [//data]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                 |
| [          -selectedItem -\> selectem item element]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                 |
| [          -selectedItemIndex -\> selected item index]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                 |
| [          -hasChild -\> returns(true or false) whether the selected item has child or not] []                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [   ] [\</] [script] [\>]                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.

 

You can observe the handlers getting invoked when the corresponding event is triggered.

**[]**  

[]{#related-topics}

