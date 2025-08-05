---
title: howtogetindividualfloatingcontrolsproperties.md
original_path: WinForms_Docs/99_Uncategorized/howtogetindividualfloatingcontrolsproperties.md
created_at: 2025-08-05
---






##### How to get individual floating controls properties? {#how-to-get-individual-floating-controls-properties style="tab-stops: 0pt"}

 

To get the x,y coordinates if it is floating

[] 

1.   Add a list view and a docking manager to your form.

2.   Enable the listview as a dock control.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| **[]**                                                                                                                                           |
|                                                                                                                                                                                                    |
| [this][.dockingManager1.SetEnableDocking([this].listView1,[true]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [Me][.dockingManager1.SetEnableDocking([Me].listView1, [True])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Set the control as a non-dockable floating window.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [this][.dockingManager1.SetFloatOnly([this].listView1,[true]);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                  |
|                                                                                                                                                                                           |
| [Me][.dockingManager1.SetFloatOnly([Me].listView1,[True])] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Determine whether the control is floating using the DockingManager.IsFloating() method. 

[] 

[·      ]If true, then the control is being hosted in a subclass of the Form type and this host form can be retrieved through the control's **TopLevelControl** property. 

[·      ]Once you have the top level form, just use the **Control.Location** property on that form to get it's x and y co-ordinates.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| **[]**                                                                                                               |
|                                                                                                                                                                        |
| [// Get the FloatingForm object to get location of control.FloatingForm is a Form derived class.]                    |
|                                                                                                                                                                        |
| [DockHost dhost = [this].listView1.Parent [as] Syncfusion.Windows.Forms.Tools.DockHost;] |
|                                                                                                                                                                        |
| [FloatingForm floatfrm = dhost.ParentForm [as] FloatingForm;]                                                 |
|                                                                                                                                                                        |
| [MessageBox.Show(floatfrm.Location.ToString());]                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Get the FloatingForm object to get location of control.FloatingForm is a Form derived class.]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ dhost [As] DockHost = [CType](IIf([TypeOf] [Me].listView1.Parent [Is] Syncfusion.Windows.Forms.Tools.DockHost, [Me].listView1.Parent, [Nothing]), Syncfusion.Windows.Forms.Tools.DockHost)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ floatfrm [As] FloatingForm = [CType](IIf([TypeOf] dhost.ParentForm [Is] FloatingForm, dhost.ParentForm, [Nothing]), FloatingForm)]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [MessageBox.Show(floatfrm.Location.ToString())]                                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

