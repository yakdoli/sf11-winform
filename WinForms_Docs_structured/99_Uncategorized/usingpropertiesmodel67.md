---
title: usingpropertiesmodel67.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel67.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the addition of animations to the Listbox using the Properties model;

1.   In the **Controller**, create an instance of **MobListboxModel**, add the ListItemCollection, configure the list item with the specified item type using the ItemType property and pass the instance through **View Specific Data** to **View** as given below:**[]**

*[[ [] ]]{.underline}*  

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| **[\[Controller\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                      |
| [        ] [public] [ [ActionResult] ListBox()]                                                     |
|                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                      |
| [            [MobListBoxModel] list = [new][MobListBoxModel]();]                                                                            |
|                                                                                                                                                                                                                                                      |
| [            list.ListStyle = [ListStyle].Numbered;]                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| [            list.ListItemStyle = [ListItemStyle].Option;]                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection = [new][List]\<[ListBoxItem]\>();]                                                                        |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"A\"], **ItemType= [ItemType].Divider** });]  |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]()]                                                                                                         |
|                                                                                                                                                                                                                                                      |
| [            {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                      |
| [                Text = [\"Android\"],]                                                                                                                                                  |
|                                                                                                                                                                                                                                                      |
| [                Items = [new][List]\<[ListBoxItem]\>()]                                                                                    |
|                                                                                                                                                                                                                                                      |
| [                {]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [                    [new][ListBoxItem](){ Text=[\"Android 1.0\"]},]                                                                        |
|                                                                                                                                                                                                                                                      |
| [                    [new][ListBoxItem](){ Text=[\"Android 2.0\"]}]                                                                         |
|                                                                                                                                                                                                                                                      |
| [                }]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [            });]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"E\"], **ItemType = [ItemType].Divider** });] |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Eclipse\"] });]                                                      |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"L\"], **ItemType = [ItemType].Divider** });] |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Linux\"] });]                                                        |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"S\"], **ItemType = [ItemType].Divider** });] |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Solaris\"] });]                                                      |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"U\"], **ItemType = [ItemType].Divider** });] |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Ubuntu\"] });]                                                       |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Unix\"] });]                                                         |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"W\"], **ItemType = [ItemType].Divider** });] |
|                                                                                                                                                                                                                                                      |
| [            list.ItemsCollection.Add([new][ListBoxItem]()]                                                                                                         |
|                                                                                                                                                                                                                                                      |
| [            {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                      |
| [                Text = [\"Windows\"],]                                                                                                                                                  |
|                                                                                                                                                                                                                                                      |
| [                Items = [new][List]\<[ListBoxItem]\>()]                                                                                    |
|                                                                                                                                                                                                                                                      |
| [                {]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [                    [new][ListBoxItem](){ Text=[\"Windows XP\"]},]                                                                         |
|                                                                                                                                                                                                                                                      |
| [                    [new][ListBoxItem](){ Text=[\"Windows Vista\"]},]                                                                      |
|                                                                                                                                                                                                                                                      |
| [                    [new][ListBoxItem](){ Text=[\"Windows 7\"]}]                                                                           |
|                                                                                                                                                                                                                                                      |
| [                }]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [            });]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                      |
| [            ViewData\[[\"list\"]\] = list;]                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [            [return] View();]                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In View, invoke the listbox helper with the view data key as the control ID[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| **[\[ASPX\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| [        ] [\<%] [=] [ Html.MobSyncfusion().ListBox([\"list\"]) [%\>]] |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [    [\@{]] [Html.MobSyncfusion().ListBox([\"list\"])] [.Render();[}]] |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   Build and run the application.

 

[ {border="0"} ]

Figure 63: Listbox - Divider[]

[] 

 

[]{#related-topics}

