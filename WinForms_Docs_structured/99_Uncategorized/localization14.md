---
title: localization14.md
original_path: WinForms_Docs/99_Uncategorized/localization14.md
created_at: 2025-08-05
---






#### Localization {#localization style="tab-stops: 0pt"}

Localization is the process of customizing the user interface as locale-specific in order to display regional data i.e. in a language and culture specific to a particular country or region. Localization is the key feature for providing solutions to global customers. This is done with the help of localized resources served by the control. GridDataControl provides an inherent XAML based support to localize its user interface.

**[]** 

How to Localize a Grid

The default \"en-US\" culture satellite assembly named as Syncfusion.Grid.Wpf.Resources.dll can be used to utilize the localization support for any culture. Any pre-built text such as Group drop area text, prompt strings, message strings, Column Options UI text and Filter dialog text can be localized.

 

Following are the steps to localize the grid:

 

Extracting the Resource Strings to a .csv File Using the LocBaml.exe File

The following steps will help you to extract the resource strings to a .csv file using the LocBaml.exe file:

**[]** 

1.   Download the LocBaml.exe file from the following location if you don\'t have it already.

[] 

[[http://files.syncfusion.com/support/Tools.WPF/UG/LocBaml.zip]{.UGHyperlink}](http://files.syncfusion.com/support/Tools.WPF/UG/LocBaml.zip)[]{.UGHyperlink}

[] 

2.   Copy the LocBaml.exe file and Syncfusion.Grid.Wpf.Resources.dll to the following location.

[] 

\<Your Application path\>\\bin\\Debug\\en-US

[] 


{border="0"}Note: This Syncfusion.Grid.Wpf.Resources.dll will be available in the following installation location.


[] 

\<Installed location\>\\Syncfusion\\Essential Studio\\\<Version Number\>\\Assemblies\\3.5

[] 

3.   Open the command prompt and navigate to the same directory.

**[]** 

4.   Use the following command to generate the .csv file from the existing Syncfusion.Grid.Wpf.Resources.dll.

[] 

\<Your Application path\>\\bin\\Debug\\en-US \\LocBaml /parse Syncfusion.Grid.Wpf.Resources.dll /out:resourceStrings.csv

[] 


[{border="0"}]Note: The .csv files can be edited in MS Excel (or) Notepad. This file contains our string resources with the default text in English language.


**[]** 

Creating Localized GridData control

[] 

1.   Open the .csv file using MS Excel or Notepad, and change the text based on your culture.

**[]** 

The following screen shots show change of text from English to German.

[] 

{border="0"}

Figure 233: CSV file for US culture- English

[] 

Below is the screen shot of the CSV file for German Culture (de).

[] 

{border="0"}

Figure 234: CSV file for German Culture

**[]** 

The next step is to generate localized satellite dll using the modified .csv file and install it in the application.

1.   Open command prompt, and navigate to the en-US directory.

2.   Create another directory[ ]de[ ]under Bin\\Debug folder using the[ ]md de command[.]

**[]** 


[{border="0"}]Note:[ ]Directory name should follow proper culture name.


**[]** 

3.   Generate your own culture-specified assembly using the following command from en-US folder.

**[]** 

LocBaml/generate/tran: resourceStrings.csv/out:../de/cul:de Syncfusion.Grid.Wpf.Resources.dll

**[]** 


[{border="0"}]Note:[ ]You will be able to view the generated satellite assembly under de folder.


**[]** 

4.   Run your application with the CurrentUICulture as \'de\' in App.xaml file as follows.

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                           |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                      |
| [public][ App()]                                                                                                                |
|                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [    CultureInfo][ ci = [new] [CultureInfo]([\"de\"]);] |
|                                                                                                                                                                                                                      |
| [    Thread][.CurrentThread.CurrentUICulture = ci;      ]                                                                    |
|                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

[{border="0"}]Note:[ ]At the end of this process, the application should have the following criteria to achieve localization.


[·      ]Your Application.exe file.

[·      ]The en-US directory with Resources.dll.

[·      ]The de directory with corresponding Resources.dll and Syncfusion Assemblies (if you had set Copy Local=True).

**[]** 

The output shows the GridData control in German Culture.

**[]** 

{border="0"}

Figure 235: Localized GridDataControl


 

[{border="0"}]Note:

1\. Localized strings are not displayed in your application until the created satellite assembly is signed. Send your newly created assemblies to Syncfusion for signing. Your assemblies will be signed and sent immediately.

2\. The satellite assemblies need not be installed in GAC or Assemblies folder.

3\. Ensure your en-US directory contains the default satellite assembly, which is available in the Precompiled Assemblies (or) Assemblies folder.

4\. Application culture change should be included before the InitializeComponent() method calls in the application. It is suggested to include culture change in the App.xaml file.


[]{#related-topics}

