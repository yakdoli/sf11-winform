---
title: displayinghtmlbyusingthehtmluicontrol.md
original_path: WinForms_Docs/99_Uncategorized/displayinghtmlbyusingthehtmluicontrol.md
created_at: 2025-08-05
---








  









### Displaying HTML By Using the HTMLUI Control {#displaying-html-by-using-the-htmlui-control style="tab-stops: 0pt"}

[] 

1.   Create a new **Windows Forms** application and open the main form for the application in the designer. Add the Syncfusion controls to your VS.NET toolbox if you haven\'t done so already. Drag an **HTMLUI control** onto the form.

2.   HTML can be loaded into the HTMLUI control from the following sources:

[] 

[·      ]From a HTML file

[·      ]From a URI (Uniform resource Identifier)

[·      ]From a Stream

[] 

3.   Add a **MainMenu** component from the toolbox onto the form. Also add a **OpenFileDialog** component to the form and name it as \"openDlg\".

[] 

{border="0"}

[] 

Figure 5: HTMLUI Control and Menu for Loading HTML Files

[] 

4.   Add a handler for the **Open** menu item by double-clicking on the menu.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [this][.menuItem2.Click += [new] System.[EventHandler]([this].menuItem2_Click);] |
|                                                                                                                                                                                                                                                                         |
| [        ]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [private][ [void] menuItem2_Click([object] sender, System.[EventArgs] e)]        |
|                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [    [// Gets or Sets the initial directory displayed by file dialog box]]                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [openDlg.InitialDirectory = GetFilesLocation();]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [     [// Gets or Sets the current file name filter string, which determines the choices that appear in the ]]                                                                                |
|                                                                                                                                                                                                                                                                         |
| [    [// \"Save as File Type\" or \"File of type\" box in the dialog box.]]                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [openDlg.Filter = [\"HTML files (\*.htm)\|\*.htm\|HTML Files (\*.html)\|\*.html\"];]                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [if][( [DialogResult].OK == openDlg.ShowDialog() )]                                                                        |
|                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [string][ filePath = openDlg.FileName;]                                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [this][.htmluiControl1.LoadHTML(filePath);]                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.menuItem2.Click += [New] System.EventHandler([Me].menuItem2_Click)]                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] menuItem2_Click([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [\'  Gets or Sets the initial directory displayed by file dialog box]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                     |
| [openDlg.InitialDirectory = GetFilesLocation()]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [\' Gets or Sets the current file name filter string, which determines the choices that appear in the ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                     |
| [\'  \"Save as File Type\" or \"File of type\" box in the dialog box.]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [openDlg.Filter = [\"HTML files (\*.htm)\|\*.htm\|HTML Files (\*.html)\|\*.html\"]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                     |
| [If][ DialogResult.OK = openDlg.ShowDialog() [Then]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Dim][ filePath [As] [String] = openDlg.FileName]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.htmluiControl1.LoadHTML(filePath)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [If]]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Now run the sample and try loading a HTML document into the HTMLUI control.

[] 

{border="0"}

[] 

Figure 6: Document Loaded into the HTMLUI Control

[] 

Any HTML document can be loaded from a file by using the method shown in this sample.

 

 

 

[]{#related-topics}

