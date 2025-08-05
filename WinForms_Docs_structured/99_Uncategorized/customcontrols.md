---
title: customcontrols.md
original_path: WinForms_Docs/99_Uncategorized/customcontrols.md
created_at: 2025-08-05
---








  









## []Custom Controls {#custom-controls style="tab-stops: 0pt"}

[[[]]]{.underline} 

The Custom Controls are not standard HTML elements but user-defined controls that are created for improving the application\'s richness and productivity.

The **Custom** tag is used to include the custom controls in an HTML document. The custom tag comes with two attributes: **assembly** and **class**.

The **assembly** attribute refers to the namespace where the control is located. The **class** attribute represents the control.

An HTML document containing custom controls is shown below.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[HTML\]]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [\<][html][\>]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [\<][body][\>]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [\<][div][\>]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| [CheckBoxAdv:[\<][CUSTOM] [class][=\"Syncfusion.Windows.Forms.Tools.CheckBoxAdv\"] [assembly][=\"Syncfusion.tools.windows\"\>]]                             |
|                                                                                                                                                                                                                                                                                                                                               |
| [\</][CUSTOM][\>]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [\</][div][\>][ ]                                                                    |
|                                                                                                                                                                                                                                                                                                                                               |
| [\<][div][\>]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| [NumericUpDown:[\<][CUSTOM] [class][=\"NumericUpDown\"] [assembly][=\"System.Windows.Forms\"\>\</][CUSTOM][\>]] |
|                                                                                                                                                                                                                                                                                                                                               |
| [\</][div][\>][ ]                                                                    |
|                                                                                                                                                                                                                                                                                                                                               |
| [\</][body][\>][ ]                                                                   |
|                                                                                                                                                                                                                                                                                                                                               |
| [\</][html][\>]                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The custom controls defined in the HTML document are interfaced with their equivalent windows forms control with the help of the **PreRenderDocument** event. The PreRenderDocument event occurs at a time when the HTML document is being loaded into the HTMLUI control, but the elements are not yet positioned.

The HTML elements are loaded into an hash table with an equivalent id as their key. An equivalent Base class object, here **BaseElement** class, is defined to link the HTML elements stored in the hash table with the help of the key associated with the element. The BaseElement is the Base class for all HTML elements. All HTML tag elements inherit this class.

The **CustomControlBase** implements the base functionality of the Windows forms control on the HTML tag element.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                         |
| [private][ [void] htmluiControl1_PreRenderDocument([object] sender, Syncfusion.Windows.Forms.HTMLUI.[PreRenderDocumentArgs] e) ] |
|                                                                                                                                                                                                                                                                                                                         |
| [{ ]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                         |
| [Hashtable][ htmlelements = [new] [Hashtable](); ]                                                                                                 |
|                                                                                                                                                                                                                                                                                                                         |
| [htmlelements = e.Document.ElementsByUserID; ]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                         |
| [// Here the base functionality of the \'this.checkBoxAdv1\' is implemented to the \'checkBoxAdvElement1\'. ]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                         |
| [BaseElement][ CheckBoxAdvElement1 = htmlelements\[[\"CheckBoxAdv\"]\] [as] [BaseElement];]                                |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                         |
| [// Create a new Wrapper object.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                         |
| [new][ [CustomControlBase]( CheckBoxAdvElement1, [this].CheckBoxAdv1 ); ]                                                                             |
|                                                                                                                                                                                                                                                                                                                         |
| [BaseElement][ NumericUpDownElement = htmlelements\[[\"NumericUpDown\"]\] [as] [BaseElement]; ]                            |
|                                                                                                                                                                                                                                                                                                                         |
| [new][ [CustomControlBase]( NumericUpDownElement, [this].NumericUpDown1 ); ]                                                                          |
|                                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] htmluiControl1_PreRenderDocument([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentArgs)]                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ htmlelements [As] Hashtable = [New] Hashtable()]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [htmlelements = e.Document.ElementsByUserID]                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Here the base functionality of the \'this.checkBoxAdv1\' is implemented to the \'checkBoxAdvElement1\'. ]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ CheckBoxAdvElement1 [As] BaseElement = [CType](IIf([TypeOf] htmlelements([\"CheckBoxAdv\"]) [Is] BaseElement, htmlelements([\"CheckBoxAdv\"]), [Nothing]), BaseElement)]      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Create a new Wrapper object.]                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ oTemp1 [As] CustomControlBase = [New] CustomControlBase(CheckBoxAdvElement1, [Me].CheckBoxAdv1)]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ NumericUpDownElement [As] BaseElement = [CType](IIf([TypeOf] htmlelements([\"NumericUpDown\"]) [Is] BaseElement, htmlelements([\"NumericUpDown\"]), [Nothing]), BaseElement)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ oTemp2 [As] CustomControlBase = [New] CustomControlBase(NumericUpDownElement, [Me].NumericUpDown1)]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image illustrates three custom controls created using HTMLUI.

[] 

                            {border="0"}

***[]*** 

Figure 28: Custom Controls created by using the HTMLUI Control

 

More:





