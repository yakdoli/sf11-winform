---
title: filepathregistrycustomdatasourcesupport.md
original_path: WinForms_Docs/03_Data_Binding/filepathregistrycustomdatasourcesupport.md
created_at: 2025-08-05
---






#### FilePath, Registry & Custom Data Source Support {#filepath-registry-custom-data-source-support style="tab-stops: 0pt"}

AutoComplete can be used with different kinds of Data Source like FilePath, Registry & CustomSource. The Data Source of the AutoComplete control can be set using the **Source** property.

When the value of the Source property is set as FilePath, the AutoComplete will displays the path in the local system as the source. This is illustrated in the image given below.

 

{border="0"}

Figure 22: Source---FilePath

 

When the value of the Source property is set as Registry, the AutoComplete loads the values from the Registry. It is used when the Registry keys are required as input. This is illustrated in the image given below.

{border="0"}

Figure 23: Source---Registry

 

When the value of the Source property is set as Custom, the AutoComplete loads the values from the Business objects bounded to the AutoComplete control using the CustomSource property. This is illustrated in the image given below.

{border="0"}

Figure 24: Source---Custom

 

Adding Data Source Support to an Application

 

AutoComplete can be used with different kinds of Data Sources using the Source property. This support can be added to the application as mentioned in the code snippet below.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete1\"][ Source][=\"FilePath\"/\>]                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete2\"][ Source][ =\"Registry\"/\>]**[]** |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete3\"][ Source][=\"Custom\"\>]                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [     \<][syncfusion][:][AutoComplete.CustomSource][\>][]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [             ][\<][local][:][CustomerListCollection][/\>][]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [     ][\</][syncfusion][:][AutoComplete.CustomSource][\>][]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][syncfusion][:][AutoComplete][\>]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [AutoComplete][ autoComplete1 = [new] [AutoComplete]();]                                                          |
|                                                                                                                                                                                                                                                        |
| [this][.][autoComplete1][.Source = [SourceMode].FilePath;]        |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [AutoComplete][ autoComplete2 = [new] [AutoComplete]();]                                                          |
|                                                                                                                                                                                                                                                        |
| [this][.][autoComplete2][.SelectionMode = [SourceMode].Registry;] |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [AutoComplete][ autoComplete3 = [new] [AutoComplete]();]                                                          |
|                                                                                                                                                                                                                                                        |
| [this][.][autoComplete3][.SelectionMode = [SourceMode].Custom;]   |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [List][\<[String]\> products = [new] [List]\<[String]\>();]       |
|                                                                                                                                                                                                                                                        |
| [customSource.Add([\"Diagram\"]);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| [customSource.Add([\"Gauge\"]);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                        |
| [customSource.Add([\"Chart\"]);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                        |
| [customSource.Add([\"Schedule\"]);]                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [customSource.Add([\"Grid\"]);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [customSource.Add([\"DocIo\"]);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                        |
| [customSource.Add([\"XlsIo\"]);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                        |
| [customSource.Add([\"Pdf\"]);]                                                                                                                                                             |
|                                                                                                                                                                                                                                                        |
| [customSource.Add([\"RichTextBox\"]);]                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| [customSource.Add([\"ReportBuilder\"]);]                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [this][.][autoComplete3][.CustomSource = products;]                                       |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Tables for properties, methods, and events

Properties

Table 3: Property Table for Data Source Support

  ---------- ---------------------------------------------- -------------------- ------------------ -----------------
  Property   Description                                    Type                 Data Type          Reference links
  Source     Gets or sets the Source of the AutoComplete.   DependencyProperty   SourceMode(enum)   
  ---------- ---------------------------------------------- -------------------- ------------------ -----------------

 

Events

Table 4: Event Table for Data Source Support

+---------------+--------------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| Event         | Description                                                              | Arguments                          | Type                              | Reference links |
+---------------+--------------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| SourceChanged |  When the Source property value is changed this event will be triggered. | DependencyObject,                  | DependencyPropertyChangedCallBack |                 |
|               |                                                                          |                                    |                                   |                 |
|               | It cannot be cancelled.                                                  | DependencyPropertyChangedEventArgs |                                   |                 |
+===============+==========================================================================+====================================+===================================+=================+

**[]** 

Sample Link

WPF Sample Browser-\> Tools -\> Editors -\> AutoComplete Demo

 

[]{#related-topics}

