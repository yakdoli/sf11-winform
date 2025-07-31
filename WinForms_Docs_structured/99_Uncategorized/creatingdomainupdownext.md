---
title: creatingdomainupdownext.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingdomainupdownext.md
created_at: 2025-07-03
---






##### Creating DomainUpDownExt {#creating-domainupdownext style="tab-stops: 0pt"}

To use a DomainUpDownExt control in your application, all you need to do is drag and drop the DomainUpDownExt control from the controls toolbox onto your form.[]

[] 

{border="0"}

Figure 441: DomainUpDownExt Control in Toolbox 

You can add items in the String Collection Editor of DomainUpDownExt control and Click Ok.[]

[] 

{border="0"}

Figure 442: Adding Items by using String Collection Editor

[] 

It can be created programmatically as follows.[]

[] 

1.   Add Shared.Base, Shared.Windows, Tools.Base and Tools.Windows assembly references and include the required namespace.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                               |
|                                                                                                                                                                      |
| []                                                                                                                                             |
|                                                                                                                                                                      |
| [using ][Syncfusion.Windows.Forms.Tools;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                            |
|                                                                                                                                                                       |
| []                                                                                                                                              |
|                                                                                                                                                                       |
| [Imports][ Syncfusion.Windows.Forms.Tools][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create an instance of the DomainUpDownExt. Add that instance to the Form.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [private][ Syncfusion.Windows.Forms.Tools.DomainUpDownExt domainUpDownExt1;][]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.domainUpDownExt1=][new][ Syncfusion.Windows.Forms.Tools.DomainUpDownExt();][] |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [// Add items.][]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.domainUpDownExt1.Items.Add(\"One\");][]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.domainUpDownExt1.Items.Add(\"Two\");][]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.domainUpDownExt1.Items.Add(\"Three\");][]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.domainUpDownExt1.Items.Add(\"Four\");][]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.domainUpDownExt1.Items.Add(\"Five\");][]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.Controls.Add(][this][.domainUpDownExt1);][]                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                  |
| [Private][ domainUpDownExt1 ][As][ Syncfusion.Windows.Forms.Tools.DomainUpDownExt][] |
|                                                                                                                                                                                                                                                                                                                  |
| [Me][.domainUpDownExt1 = ][New][ Syncfusion.Windows.Forms.Tools.DomainUpDownExt()][] |
|                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                  |
| [\' Add items.][]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                  |
| [Me][.domainUpDownExt1.Items.Add(][\"One\"][)][]                                   |
|                                                                                                                                                                                                                                                                                                                  |
| [Me][.domainUpDownExt1.Items.Add(][\"Two\"][)][]                                   |
|                                                                                                                                                                                                                                                                                                                  |
| [Me][.domainUpDownExt1.Items.Add(][\"Three\"][)][]                                 |
|                                                                                                                                                                                                                                                                                                                  |
| [Me][.domainUpDownExt1.Items.Add(][\"Four\"][)][]                                  |
|                                                                                                                                                                                                                                                                                                                  |
| [Me][.domainUpDownExt1.Items.Add(][\"Five\"][)][]                                  |
|                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                  |
| [Me][.Controls.Add(][Me][.domainUpDownExt1)][]                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 443: DomainUpDownExt Created Programmatically

 

[]{#related-topics}

