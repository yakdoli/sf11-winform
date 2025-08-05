---
title: usingpropertiesmodel70.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel70.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the setting of the Syncfusion themes to the Listbox using the Properties model.

1.   In the **Controller**, create an instance of the **MobListboxModel**, followed by the AutoFormat property with the desired theme as an argument and  pass the instance through **view specific data** to **View** as given below.**

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                                        |
|                                                                                                                                                                                                   |
| [        ] [public] [ [ActionResult] ListBox()]  |
|                                                                                                                                                                                                   |
| [        {]                                                                                                                                                   |
|                                                                                                                                                                                                   |
| [            [MobListBoxModel] list = [new][MobListBoxModel]();]                         |
|                                                                                                                                                                                                   |
| [            **list.AutoFormat = [MobSkins].DarkNight;**]                                                                             |
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
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Android\"] });]   |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Eclipse\"] });]   |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Unix\"] });]      |
|                                                                                                                                                                                                   |
| [            ViewData\[[\"lbCore\"]\] = list;]                                                                                        |
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

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                           |
| [    ] [\<%] [=] [ Html.MobSyncfusion().ListBox([\"lbCore\"]) [%\>]] |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [    [\@{]] [Html.MobSyncfusion().ListBox([\"lbCore\"])] [.Render();[}]] |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.

 

[] 

[ {border="0"} ]

Figure 69: ListBox with DarkNight Theme

 

[ {border="0"} ]

Figure 70 : ListBox with Spinach Theme[]

[] 

[ {border="0"} ]

Figure 71: ListBox with MetroBlue Theme[]

[] 

[ {border="0"} ]

Figure 72: ListBox with BlueLight Theme[]

[] 

[] 

 

[]{#related-topics}

