---
title: usingpropertiesmodel69.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel69.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how you can enable the filtering feature using the EnableFiltering property:**

1.   In the **Controller**, create an instance of **MobListboxModel**, define the **EnableFiltering** property and pass the instance through view specific data to **View** as given below.**

*[[ [] ]]{.underline}*  

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                    |
|                                                                                                                                                                                                   |
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
| [            **list.EnableFiltering = [true];**]                                                                                         |
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
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Eclipse\"] });]   |
|                                                                                                                                                                                                   |
| [            list.ItemsCollection.Add([new][ListBoxItem]() { Text = [\"Unix\"] });]      |
|                                                                                                                                                                                                   |
| [            ViewData\[[\"lbCore\"]\] = list;]                                                                                        |
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

3.   Build and run the application.

 

[] 

{border="0"}

Figure 10 :ListBox - Filtering[]

 

{border="0"}

Figure 11 :ListBox - Displaying Child Count[]

 

[]{#related-topics}

