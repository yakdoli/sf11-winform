---
title: spellcheckformultiplecontrols.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\spellcheckformultiplecontrols.md
created_at: 2025-07-03
---






##### SpellCheck for Multiple controls {#spellcheck-for-multiple-controls style="tab-stops: 0pt"}

The SpellCheckControl allows you to check the spellings in various controls on the same page at one shot.

Use Case Scenario

The user can check the spellings of all the controls on the same page continuously, without having to manually start a spellcheck for each control.

This makes it very convenient for users who need to check a lot of spellings for various controls.

 

Where do I find Installed samples?

To view the samples:

1.   Click Dashboard. The Essential Studio Enterprise Edition window is displayed.

The User Interface Edition panel is displayed by default.

2.   Click the drop-down button of ASP.NET platform. 

3.   Click the Run Locally Installed Samples link. The Essential Studio ASP.NET Edition sample browser is displayed.

4.   When you click on Locally Installed Samples, the default ASP.NET Tools sample browser page opens.[]

       {border="0"}

Figure 94: ASP.NET Tools Sample Browser page

5.   Select **Editor Package** tab provided and browse through the **SpellChecker** features---You will find the samples for **Spellchecker for Multiple** **controls** under the **Multiple Controls** section

 

Source Code Location

The full source code of the SpellCheckControl will be available on the purchase of the product.

In order to go the source code location, go to-

***\[Location where you have installed Sync fusion Products\]***[à] **** ***Essential Studio\\vx.x.x.x\\Web\\Tools.Web\\Src***

 

Properties used

 

  -------------------------------------------- -------------------------------------------------------------------------------------------------------- --------------------------------------------- --------------------------------------------- -----------------------------------------
  Property[]          Description[]                                                                   Type of Property[]   Value it accepts[]   Dependencies[]
  ControlsToCheck[]   This property specifies the IDs of various controls that should be checked.[]   Array                                         Strings[]            NA[]
  -------------------------------------------- -------------------------------------------------------------------------------------------------------- --------------------------------------------- --------------------------------------------- -----------------------------------------

[] 

 

Adding SpellCheck for Multiple controls to ASP.NET Tools

 

To raise and process the Client-side events, follow the steps given below-

1.   Add a new web-page in your project.

2.   Drag and drop the SpellCheckControl.

3.   Add the required items (e.g.: TextBox1, TextBox2, etc.) to the ASPX page.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\[ASPX\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][syncfusion][:][SpellCheckControl ][ID][ [=] [\"SpellCheck1\"] [ControlsToCheck] [=] [\"TextBox1,TextBox2,TextBox3\"] [runat] [=] [\"server\"] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [syncfusion][:][SpellCheckControl][\>]                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                              |
| [\[CS\]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                              |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)]                                                                        |
|                                                                                                                                                                                                                                                                                              |
| [    {      ]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                              |
| [ [if](!Page.IsPostBack)]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                              |
| [   [this].SpellCheck1.ControlsToCheck = [new] [string]\[3\] { [\"TextBox1\"], [\"TextBox2\"], [\"TextBox3\"] };] |
|                                                                                                                                                                                                                                                                                              |
| [    }][]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\[VB\]]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Protected][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] [Me].Load] |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [        [If] [Not] Page.IsPostBack [Then]]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [            [Dim] ids(0 [To] 2) [As] [String]]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [            ids(0) = [\"TextBox1\"]]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [            ids(1) = [\"TextBox2\"]]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [            ids(2) = [\"TextBox3\"]]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [            [Me].SpellCheckControl1.ControlsToCheck = ids]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [        [End] [If]]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [       ]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [    [End] [Sub]][]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

4.   Build and run the application, and you will get the required output.

 

[]{#related-topics}

