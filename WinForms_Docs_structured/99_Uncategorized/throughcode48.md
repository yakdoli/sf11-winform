---
title: throughcode48.md
original_path: WinForms_Docs/99_Uncategorized/throughcode48.md
created_at: 2025-08-05
---






##### Through Code {#through-code style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

To create a StatusBarAdv control programmatically,

[] 

1.               Open a new Visual C# or VB.NET application in Visual Studio .NET.

[] 

2.   Add the Syncfusion.Shared.Base and Syncfusion.Tools.Windows assemblies to your application.

[] 

3.   Declare the StatusBarAdv and StatusBarAdvPanel controls.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [private][ Syncfusion.Windows.Forms.Tools.[StatusBarAdv] statusBarAdv1;]           |
|                                                                                                                                                                                              |
| [private][ Syncfusion.Windows.Forms.Tools.[StatusBarAdvPanel] statusBarAdvPanel1;] |
|                                                                                                                                                                                              |
| [private][ Syncfusion.Windows.Forms.Tools.[StatusBarAdvPanel] statusBarAdvPanel2;] |
|                                                                                                                                                                                              |
| [private][ Syncfusion.Windows.Forms.Tools.[StatusBarAdvPanel] statusBarAdvPanel3;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [Private][ statusBarAdv1 [As] Syncfusion.Windows.Forms.Tools.StatusBarAdv]           |
|                                                                                                                                                                                                |
| [Private][ statusBarAdvPanel1 [As] Syncfusion.Windows.Forms.Tools.StatusBarAdvPanel] |
|                                                                                                                                                                                                |
| [Private][ statusBarAdvPanel2 [As] Syncfusion.Windows.Forms.Tools.StatusBarAdvPanel] |
|                                                                                                                                                                                                |
| [Private][ statusBarAdvPanel3 [As] Syncfusion.Windows.Forms.Tools.StatusBarAdvPanel] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Initialize the controls.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdv1 = [new] Syncfusion.Windows.Forms.Tools.[StatusBarAdv]();]           |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdvPanel1 = [new] Syncfusion.Windows.Forms.Tools.[StatusBarAdvPanel]();] |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdvPanel2 = [new] Syncfusion.Windows.Forms.Tools.[StatusBarAdvPanel]();] |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdvPanel3 = [new] Syncfusion.Windows.Forms.Tools.[StatusBarAdvPanel]();] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [Me][.statusBarAdv1 = [New] Syncfusion.Windows.Forms.Tools.StatusBarAdv() ]                                                 |
|                                                                                                                                                                                                                                       |
| [Me][.statusBarAdvPanel1 = [New] Syncfusion.Windows.Forms.Tools.StatusBarAdvPanel() ]                                       |
|                                                                                                                                                                                                                                       |
| [Me][.statusBarAdvPanel2 = [New] Syncfusion.Windows.Forms.Tools.StatusBarAdvPanel() ]                                       |
|                                                                                                                                                                                                                                       |
| [Me][.statusBarAdvPanel3 = [New] Syncfusion.Windows.Forms.Tools.StatusBarAdvPanel()][ ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Set the properties to customize the control\'s appearance, and add the control to the form.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdv1.BackColor = System.Drawing.[Color].LightSteelBlue;]                                      |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdv1.BorderColor = System.Drawing.[Color].Black;]                                             |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdv1.Dock = System.Windows.Forms.[DockStyle].Bottom;]                                         |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdv1.Name = [\"statusBarAdv1\"];]                                                           |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdv1.Controls.Add([this].statusBarAdvPanel1);]                                                |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdv1.Controls.Add([this].statusBarAdvPanel2);]                                                |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdv1.Controls.Add([this].statusBarAdvPanel3);]                                                |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdvPanel1.PanelType = Syncfusion.Windows.Forms.Tools.[StatusBarAdvPanelType].CurrentCulture;] |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdvPanel2.PanelType = Syncfusion.Windows.Forms.Tools.[StatusBarAdvPanelType].ShortDate;]      |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdvPanel3.PanelType = Syncfusion.Windows.Forms.Tools.[StatusBarAdvPanelType].ShortTime;]      |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdvPanel1.Size = [new] System.Drawing.[Size](100, 27);]                  |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdvPanel2.Size = [new] System.Drawing.[Size](100, 27);]                  |
|                                                                                                                                                                                                                          |
| [this][.statusBarAdvPanel3.Size = [new] System.Drawing.[Size](100, 27);]                  |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [this][.Controls.Add([this].statusBarAdv1);]                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [Me][.statusBarAdv1.BackColor = System.Drawing.Color.LightSteelBlue]                                      |
|                                                                                                                                                                                                |
| [Me][.statusBarAdv1.BorderColor = System.Drawing.Color.Black]                                             |
|                                                                                                                                                                                                |
| [Me][.statusBarAdv1.Dock = System.Windows.Forms.DockStyle.Bottom]                                         |
|                                                                                                                                                                                                |
| [Me][.statusBarAdv1.Name = \"statusBarAdv1\"]                                                             |
|                                                                                                                                                                                                |
| [Me][.statusBarAdv1.Controls.Add([Me].statusBarAdvPanel1)]                           |
|                                                                                                                                                                                                |
| [Me][.statusBarAdv1.Controls.Add([Me].statusBarAdvPanel2)]                           |
|                                                                                                                                                                                                |
| [Me][.statusBarAdv1.Controls.Add([Me].statusBarAdvPanel3)]                           |
|                                                                                                                                                                                                |
| [Me][.statusBarAdvPanel1.PanelType = Syncfusion.Windows.Forms.Tools.StatusBarAdvPanelType.CurrentCulture] |
|                                                                                                                                                                                                |
| [Me][.statusBarAdvPanel2.PanelType = Syncfusion.Windows.Forms.Tools.StatusBarAdvPanelType.ShortDate]      |
|                                                                                                                                                                                                |
| [Me][.statusBarAdvPanel3.PanelType = Syncfusion.Windows.Forms.Tools.StatusBarAdvPanelType.ShortTime]      |
|                                                                                                                                                                                                |
| [Me][.statusBarAdvPanel1.Size = [New] System.Drawing.Size(100, 27)]                  |
|                                                                                                                                                                                                |
| [Me][.statusBarAdvPanel2.Size = [New] System.Drawing.Size(100, 27)]                  |
|                                                                                                                                                                                                |
| [Me][.statusBarAdvPanel3.Size = [New] System.Drawing.Size(100, 27)]                  |
|                                                                                                                                                                                                |
| []                                                                                                                                            |
|                                                                                                                                                                                                |
| [Me][.Controls.Add([Me].statusBarAdv1)]                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Run the application. You will see the StatusBarAdv control docked to the bottom of the form. By default it will be docked to \'Bottom\'.

[] 

{border="0"}

**[]** 

Figure 1007: StatusBarAdv Control created Through Code

**[]** 

See Also

[] 

[[Through Designer]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Through_Designer_3)[]{.UGHyperlink}

 

 

 

 

[]{#related-topics}

