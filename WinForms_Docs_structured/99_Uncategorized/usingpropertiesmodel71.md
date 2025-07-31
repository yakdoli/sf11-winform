---
title: usingpropertiesmodel71.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel71.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the handling of the client side events of the Listbox through the Properties model.

1.   In the **Controller**, create an instance of **MobListboxModel**, define the event handler properties and pass the instance through **View Specific Data** to **View** as given below.**

**[]**  

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| **[\[Controller\]]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                                        |
|                                                                                                                                                                                                   |
| [        ] [public] [ [ActionResult] Listbox()]  |
|                                                                                                                                                                                                   |
| [        {]                                                                                                                                                   |
|                                                                                                                                                                                                   |
| [            [MobListBoxModel] list = [new][MobListBoxModel]();]                         |
|                                                                                                                                                                                                   |
| [            **list.OnListLoad = [\"OnListLoad\"];**]                                                                                 |
|                                                                                                                                                                                                   |
| **[            list.OnItemSelect = [\"OnItemSelect\"];]**                                                                             |
|                                                                                                                                                                                                   |
| **[            list.OnButtonClick = [\"OnButtonClick\"];]** []                                    |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection = [new][List]\<[ListBoxItem]\>();]                     |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Windows 7\"] });] |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Linux\"] });]     |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Ubuntu\"] });]    |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Solaris\"] });]   |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Android\"] });]   |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Eclipse\"] });]   |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Unix\"] });]      |
|                                                                                                                                                                                                   |
| [             ViewData\[[\"lbCore\"]\] = list;]                                                                                       |
|                                                                                                                                                                                                   |
| [            [return] View();]                                                                                                           |
|                                                                                                                                                                                                   |
| [        }]                                                                                                                                                   |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

2.   In View, invoke the listbox helper with the view data key as the control ID[]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                               |
| [    ] [\<%] [=] [ Html.MobSyncfusion().ListBox([\"lbCore\"]) [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Razor\]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                             |
| [    [\@{]] [Html.MobSyncfusion().ListBox([\"lbCore\"])] [.Render();[}]] |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In Javascript, define the handlers as given below.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Javascirpt\]**                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ]                                                                      |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                |
| [      function] [ OnListLoad(event, model) {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                |
| [        ] [//event --\> event object.] []                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                |
| [        ] [//Model --\> Listbox model object] []                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| [       function] [ OnButtonClick(event, Model) {]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                |
| [        ] [//event --\> event object.] []                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                |
| [        ] [//Model --\> Listbox model object] []                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [            ]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| [        [function] OnItemSelect(event, data) {]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [        ] [//event -- event object.] []                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                |
| [        ] [//data]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                |
| [          -selectedItem -\> selectem item element]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [          -selectedItemIndex -\> selected item index]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                |
| [          -hasChild -\> returns(true or false) whether the selected item has child or not] []                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| [   ] [\</] [script] [\>] [] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

You can observe the handlers getting invoked when the corresponding event is triggered.

 

 

[]{#related-topics}

