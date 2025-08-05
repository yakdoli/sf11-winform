---
title: localizationsupport.md
original_path: WinForms_Docs/99_Uncategorized/localizationsupport.md
created_at: 2025-08-05
---






##### Localization support {#localization-support style="tab-stops: 0pt"}

[Localization is the process of customizing the User Interface (UI) as locale-specific, in order to display regional data i.e. in a language and culture specific to a particular country or region.]

[This helps to provide IT solutions to global customers in their native languages.]

[Localization is done with the help of localized resources by the control. UploadBox provides an inherent support to localize its UI.]

 

**Server side Properties**

*[]* 


+------------------+-------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------+------------------+
| **Property**     | **Description**                                                         | **Type**    | **Value it accepts**                                                        | **Dependencies** |
+------------------+-------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------+------------------+
| Localize         | Get or set the localization culture of Grid                             | String      | A string containing the name of the target System.Globalization.CultureInfo | NA               |
+------------------+-------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------+------------------+
| LocalizationPath | Get or set the localization resource path of the resource file location | String      | Any string value.                                                           | Localize         |
|                  |                                                                         |             |                                                                             |                  |
|                  |                                                                         |             | Default : "\~/App_GlobalResources"                                          |                  |
+------------------+-------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------+------------------+


**[]** 

**[Using UploadBox Builder ]**

[To enable localization feature using UploadBox Builder:]

[] 

1.   Create a model in the application

2.   Create a strongly typed view

3.   [Create a folder named **App_GlobalResources** in the application and create your own localization resource (.resx) file in this folder.]

[] 

[{border="0"}][]

Figure 333: App_GlobalResource Folder

[] 

[] 

[In order to create a new localization resource file, download the default localization file from the following location, rename it and then use Visual Studio to edit the values.]

[] 

[[UploadBoxResource.zip]](http://www.syncfusion.com/uploads/redirect.aspx?&team=support&file=UploadBoxResource-1690666839.zip)[]

[] 

[The default English localization file is shown in the following screenshot:]

[ {border="0"}][]

Figure 334: Resource File for English Culture

[] 

[] 

[] 

[] 

***[{border="0"}]**[Note: The name of the localization file should be in the format UploadBoxResource.\[culture\].resx. For example : \"]*** ***[UploadBoxResource.fr-FR.resx \"]***

[] 

1.   [Create the UploadBox control in **View** and configure its properties.]

2.   [In the controller return to view.]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [ [ ][public][ ][ActionResult][ Index()\                           |
|    {\                                                                                                                                                                                                                                           |
| \                                                                                                                                                                                                                                               |
| ]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [\                                                                                                                                                                                                                                              |
|         ][return][ View();] |
|                                                                                                                                                                                                                                                 |
| [   }]                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[Specifying the culture using **Localize**() method:]

[] 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [            [\<%][=] Html.Syncfusion().UploadBox([\"upload\"])][] |
|                                                                                                                                                                                                                     |
| [                             .AsyncUpload]                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [                             (]                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [                                 s =\> s.AutoUpload([false])]                                                                                             |
|                                                                                                                                                                                                                     |
| [                                     .SaveAction([\"Save\"], [\"uploadbox\"])]                                                 |
|                                                                                                                                                                                                                     |
| [                                     .RemoveAction([\"Remove\"], [\"uploadbox\"])]                                             |
|                                                                                                                                                                                                                     |
| [                             ).AutoFormat([Skins].Sandune)]                                                                                            |
|                                                                                                                                                                                                                     |
| [                           .Localize([\"fr-FR\"])]                                                                                                     |
|                                                                                                                                                                                                                     |
| [                           .LocalizationPath([\"\~/Content\"])  [%\>]]                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

3.   [Run the application. The control will appear as shown below:]

[] 

[{border="0"}][]

Figure 335: UploadBoxWith French Culture

 

**Using UploadBoxPropertiesModel:[]**

[  ][]

[To enable localization feature using UploadBoxPropertiesModel:]

1.   [Follow the first two steps that are listed under the **Using UploadBox Builder** method.]

2.   [Then, add the following code in the **View **page, to create the UploadBox control in the View.]

[] 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [   [\<%][=] Html.Syncfusion().UploadBox([\"uploadbox\"], ([UploadBoxModel])Model) [%\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**[]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [     [@(] [new] [HtmlString](Html.Syncfusion().UploadBox([\"upload\"],([UploadBoxModel])Model).ToString())[)]][] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   [You can specify the culture information, as shown in the previous section- **Using UploadBox Builder.**]

4.   [Create an UploadBoxModel in the Index method, and use Localize property to specify the culture details.]

[] 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[]                                                                            |
|                                                                                                                                                                           |
| [        [public] [ActionResult] Index()][]          |
|                                                                                                                                                                           |
| [        {]                                                                                                                           |
|                                                                                                                                                                           |
| [    ]                                                                                                                                |
|                                                                                                                                                                           |
| [            [UploadBoxModel] model = [new] [UploadBoxModel]();] |
|                                                                                                                                                                           |
| [         [//  ..]]                                                                                             |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [            model.Localize = [\"fr-FR\"];]                                                                   |
|                                                                                                                                                                           |
| [            model.LocalizationPath = [\"\~/Content\"];]                                                      |
|                                                                                                                                                                           |
| [            [return] View(model);]                                                                              |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[] 

5.   [Run the application. The output you get will be as follows:]

[] 

[{border="0"}][]

Figure 336: UploadBox with French Culture

[] 

[]{#related-topics}

