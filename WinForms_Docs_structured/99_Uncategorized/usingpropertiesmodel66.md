---
title: usingpropertiesmodel66.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel66.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how you can implement the nested list using Properties model:

1.   In the **Controller**, create an instance of **MobListboxModel**, add the ListItemCollection and pass the instance through **View Specific Data** to **View** as given below:**[]**

**[]**  

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                         |
|                                                                                                                                                                                                  |
| **[]**                                                                                                                                                       |
|                                                                                                                                                                                                  |
| [        ] [public] [ [ActionResult] ListBox()] |
|                                                                                                                                                                                                  |
| [        {]                                                                                                                                                  |
|                                                                                                                                                                                                  |
| [            [MobListBoxModel] list = [new][MobListBoxModel]();]                        |
|                                                                                                                                                                                                  |
| [            list.ListStyle = [ListStyle].Numbered;]                                                                                 |
|                                                                                                                                                                                                  |
| [            list.ListItemStyle = [ListItemStyle].Option;]                                                                           |
|                                                                                                                                                                                                  |
| [            list.ItemsCollection = [new][List]\<[ListBoxItem]\>();]                    |
|                                                                                                                                                                                                  |
| [            list.ItemsCollection.Add([new][ListBoxItem]()]                                                     |
|                                                                                                                                                                                                  |
| [            {]                                                                                                                                              |
|                                                                                                                                                                                                  |
| [                Text = [\"Windows\"],]                                                                                              |
|                                                                                                                                                                                                  |
| [                **Items = [new][List]\<[ListBoxItem]\>()**]                            |
|                                                                                                                                                                                                  |
| **[                {]**                                                                                                                                      |
|                                                                                                                                                                                                  |
| **[                    [new][ListBoxItem](){ Text=[\"Windows XP\"]},]**                 |
|                                                                                                                                                                                                  |
| **[                    [new][ListBoxItem](){ Text=[\"Windows Vista\"]},]**              |
|                                                                                                                                                                                                  |
| **[                    [new][ListBoxItem](){ Text=[\"Windows 7\"]}]**                   |
|                                                                                                                                                                                                  |
| **[                }]**                                                                                                                                      |
|                                                                                                                                                                                                  |
| [            });]                                                                                                                                            |
|                                                                                                                                                                                                  |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Linux\"] });]    |
|                                                                                                                                                                                                  |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Ubuntu\"] });]   |
|                                                                                                                                                                                                  |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Solaris\"] });]  |
|                                                                                                                                                                                                  |
| [            list.ItemsCollection.Add([new][ListBoxItem]() ]                                                    |
|                                                                                                                                                                                                  |
| [            {]                                                                                                                                              |
|                                                                                                                                                                                                  |
| [                Text = [\"Android\"],]                                                                                              |
|                                                                                                                                                                                                  |
| [                **Items = [new][List]\<[ListBoxItem]\>()**]                            |
|                                                                                                                                                                                                  |
| **[                {]**                                                                                                                                      |
|                                                                                                                                                                                                  |
| **[                    [new][ListBoxItem](){ Text=[\"Android 1.0\"]},]**                |
|                                                                                                                                                                                                  |
| **[                    [new][ListBoxItem](){ Text=[\"Android 2.0\"]}]**                 |
|                                                                                                                                                                                                  |
| **[                }]**                                                                                                                                      |
|                                                                                                                                                                                                  |
| [            });]                                                                                                                                            |
|                                                                                                                                                                                                  |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Eclipse\"] });]  |
|                                                                                                                                                                                                  |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Unix\"] });]     |
|                                                                                                                                                                                                  |
| [            ViewData\[[\"list\"]\] = list;]                                                                                         |
|                                                                                                                                                                                                  |
| [            [return] View();]                                                                                                          |
|                                                                                                                                                                                                  |
| [        }]                                                                                                                                                  |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In View, invoke the listbox helper with the view data key as the control ID[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| [        ] [\<%] [=] [ Html.MobSyncfusion().ListBox([\"list\"]) [%\>]] |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                      |
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

 

[] 

[ {border="0"} ]

Figure 8: Nested List

[] 

[] 

[] 

[] 

[ {border="0"} ]

Figure 9: Nested List - Sub item[]

 

[]{#related-topics}

