---
title: image.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\image.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Image {#image style="tab-stops: 0pt"}

The Form Button control can render an icon along with the text property. The icon can be set for a button with the **ImageURL** property.

 

Properties

  ---------- ---------------------------------------- ------------------ ------------------ ------------
  Name       Description                              Type of Property   Value it Accepts   Dependency
  ImageUrl   Sets the image for the button control.   String             ActionBuilder      \-
  ---------- ---------------------------------------- ------------------ ------------------ ------------

 

Using Builder

The following steps explain how to set the icon settings in the Form Button control using Builder:

1.   In the **view**, invoke the **Button** helper with the control ID as the first argument followed by the **ImageUrl**, **AutoFormat**, and **Text** methods with their respective text and images as desired by the user.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%] [=] [Html.MobSyncfusion().Button([\"Button\"]).ImageUrl([\"../Content/Button/Images/Delete.png\"]).Text([\"Delete\"]).AutoFormat([MobSkins].Spinach) [%\>]]            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [   ] [\@{] [ Html.MobSyncfusion().Button([\"Button\"]).ImageUrl([\"../Content/Button/Images/Delete.png\"]).Text([\"Delete\"]).AutoFormat([MobSkins].Spinach).Render(); [}]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

 

Using Properties Model

The following steps explain how to set the image settings in the Form Button control using the properties model:

 

1.   In the **controller**, create an instance of **MobButtonModel**, define the **ImageUrl** property, and pass the instance through **ViewData** to the **view** as given below:**

*[[]]{.underline}*  

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                  |
| [        [public][ActionResult] Button()]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                  |
| [        {]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                  |
| [            [MobButtonModel] model = [new][MobButtonModel]()]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                  |
| [            {]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                  |
| [                ] [Text=[\"Delete\"],]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                  |
| [                ImageUrl] [([\"../Content/Button/Images/Delete.png]] [\"] [,[]] |
|                                                                                                                                                                                                                                                                                                  |
| [                AutoFormat=[MobSkins].Spinach]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                  |
| [            };]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                  |
| [            ViewData\[[\"button\"]\] = model;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                  |
| [            [return] View();]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                  |
| [        }]                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In the **view**, invoke the **Button** helper with the **ViewData** key as the first argument.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| [       [\<%][=]Html.MobSyncfusion().Button] [([\"button\"]] [)[%\>]] [] |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                               |
| [       [\@{]Html.MobSyncfusion().Button([\"button\"]).Render();[}]]                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

The output is shown in the following screenshot.

 

{border="0"}

Figure 6: Button---ImageUrl Property

 

[]{#related-topics}

