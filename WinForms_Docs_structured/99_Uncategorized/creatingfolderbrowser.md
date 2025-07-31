---
title: creatingfolderbrowser.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingfolderbrowser.md
created_at: 2025-07-03
---






##### Creating FolderBrowser {#creating-folderbrowser style="tab-stops: 0pt"}

[] 

FolderBrowser control can be created in the following ways.

[] 

###### []{#_Through_Designer_6}3.3.7.1.2.1 Through Designer []{#p493} {#through-designer style="tab-stops: 0pt"}

[] 

The designer based approach for creating and initializing the FolderBrowser component is shown below.

[] 

1.   Select the **FolderBrowser** control from the Visual Studio .NET toolbox window and drop it onto the design form. An instance of the FolderBrowser component will be added to the design form\'s component tray.

[] 

{border="0"}

Figure 429: FolderBrowser in Toolbox

[] 

2.   Select a suitable value for the **FolderBrowser.StartLocation** property from the enumerator list provided by the property grid. This specifies the location at which browsing should be started in the folder hierarchy. This property is the functional equivalent of the **Win32 PIDL**\'**s.**

 

3.   Specify an appropriate value for the **FolderBrowser.Style** property. The **FolderBrowserStyles** enumeration specifies various options for the FolderBrowser Dialog.

 

4.   To display the FolderBrowser window, simply invoke the **FolderBrowser.ShowDialog()** method from within your application\'s code.

[] 

This method is a modal function and if the return code indicates success, the **FolderBrowser.DirectoryPath** property may be used to access the selected folder.

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                             |
|                                                                                                                            |
| []                                                                       |
|                                                                                                                            |
| [this][.folderBrowser1.ShowDialog();] |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                      |
|                                                                                                                         |
| []                                                                    |
|                                                                                                                         |
| [Me][.folderBrowser1.ShowDialog()] |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 430: FolderBrowser created Through Designer

[] 

See Also

[] 

[Through Code]{.UGHyperlink}[]{.UGHyperlink}

###### []{#p494}3.3.7.1.2.2 Through Code {#through-code style="tab-stops: 0pt"}

[] 

The programmatic approach for using the FolderBrowser component is shown below.

[] 

1.   Create an instance of the FolderBrowser component.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [// Declare the FolderBrowser component.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [private][ Syncfusion.Windows.Forms.[FolderBrowser] folderBrowser1;]                                                                   |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [// Create an instance of the FolderBrowser component.]                                                                                                                                           |
|                                                                                                                                                                                                                                                     |
| [this][.folderBrowser1 = [new] Syncfusion.Windows.Forms.[FolderBrowser]([this].components);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Declare the FolderBrowser component.]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][ folderBrowser1 [As] Syncfusion.Windows.Forms.FolderBrowser]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Create an instance of the FolderBrowser component.]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.folderBrowser1 = ][New][ Syncfusion.Windows.Forms.FolderBrowser(][Me][.components)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Set the FolderBrowser.StartLocation and FolderBrowser.Style property values.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                 |
| [// Specify the Start location.]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                 |
| [this][.folderBrowser1.StartLocation = Syncfusion.Windows.Forms.[FolderBrowserFolder].MyComputer;]                                                                                                 |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                 |
| [// Specify the styles for the FolderBrowser Dialog.]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [this][.folderBrowser1.Style = (Syncfusion.Windows.Forms.[FolderBrowserStyles].RestrictToFilesystem \| Syncfusion.Windows.Forms.[FolderBrowserStyles].BrowseForComputer);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Specify the Start location.]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.folderBrowser1.StartLocation = Syncfusion.Windows.Forms.FolderBrowserFolder.MyComputer]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Specify the styles for the FolderBrowser Dialog.]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.folderBrowser1.Style = Syncfusion.Windows.Forms.FolderBrowserStyles.RestrictToFilesystem ][Or][ Syncfusion.Windows.Forms.FolderBrowserStyles.BrowseForComputer] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Invoke the **FolderBrowser.ShowDialog()** method to display the FolderBrowser Dialog.

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                             |
|                                                                                                                            |
| []                                                                       |
|                                                                                                                            |
| [this][.folderBrowser1.ShowDialog();] |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                      |
|                                                                                                                         |
| []                                                                    |
|                                                                                                                         |
| [Me][.folderBrowser1.ShowDialog()] |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 431: FolderBrowser created Through Code

[] 

See Also

[] 

[[Through Designer]{.UGHyperlink}]()[]{.UGHyperlink}

[]{#related-topics}

