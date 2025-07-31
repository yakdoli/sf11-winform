---
title: addinglocalizationfe3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addinglocalizationfe3.md
created_at: 2025-07-03
---








  





### Adding Localization [[feature]]{.Heading1Char} to an application {#adding-localization-feature-to-an-application style="tab-stops: 0pt"}

To add localization to an application, follow the steps given below:

1.   Create a Silverlight application

{border="0"}

Figure 25 New Project Dialog Window

 

2.  Add a folder into the Silverlight project and name it as "Resources".

{border="0"}

Figure 26 Solution Explorer with "Resources" Folder

 

3.   Right click on the Resources folder and Select Add -\> New Item from the context menu. From the dialog shown, select the Resource File and name it as shown below.

"**Syncfusion.OlapGrid.Silverlight.\<cultureCode\>.resx"**

For an instance, the file name for the Portuguese-Brazil culture could be:

**Syncfusion. OlapGrid.Silverlight.pt-BR.resx**

Refer to the following link for culture codes:

<http://msdn.microsoft.com/en-us/library/system.globalization.cultureinfo(v=vs.71).aspx>

{border="0"}

Figure 27 Add New Item Dialog Window

Now, the Syncfusion.OlapGrid.Silverlight.pt-BR.resx file is added to the Silverlight project.

{border="0"}

Figure 28 Solution Explorer with Added Resource File

4.  **O**pen the resource file, fill the Name and translate the value according to your locale with respect to the above table.

{border="0"}

Figure 29 Resource Editor Window

To switch the application between different languages, specify the supported culture in the Silverlight project file.

5.   In order to specify the supported culture in the Silverlight project file, unload the project by right-clicking over the Silverlight project and select the "**Unload Project**" from the context menu.

The project is unloaded from the solution as shown below:

{border="0"}

Figure 30 Solution Explorer with Unloaded Project

6.   Right-click the Silverlight project file and select the Edit project from the context menu. This brings the metadata of the Silverlight project.

7.   Look for the \<SupportedCultures\> tag within the \<PropertyGroup\> tag and add the culture code inside the \<SupportedCultures\> tag.

For multiple cultures, add each culture code within the same tag separated by a semicolon (;).

{border="0"}

Figure 31 Metadata of Silverlight Project

8.   Save the \*.csproj file. Right-click and select the "**Reload Project**" to reload the unloaded project.

9.   Add the following code inside the App constructor to set the current culture:

{border="0"}

Figure 32  App Constructor

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [            System.Threading.[Thread].CurrentThread.CurrentCulture = [new] System.Globalization.[CultureInfo]([\"pt-BR\"]);]   |
|                                                                                                                                                                                                                                                                               |
| [            System.Threading.[Thread].CurrentThread.CurrentUICulture = [new] System.Globalization.[CultureInfo]([\"pt-BR\"]);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Note: The bidirectional support can be utilized through setting the FlowDirection property.


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                     |
| [            [if] (Threading.[Thread].CurrentThread.CurrentUICulture.ToString() == [\"ar\"])] |
|                                                                                                                                                                                                                     |
| [            {]                                                                                                                                                    |
|                                                                                                                                                                                                                     |
| [                [this].olapGrid.FlowDirection = System.Windows.[FlowDirection].RightToLeft;]                         |
|                                                                                                                                                                                                                     |
| [            }]                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

