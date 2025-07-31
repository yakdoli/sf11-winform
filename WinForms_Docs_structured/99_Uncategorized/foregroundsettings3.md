---
title: foregroundsettings3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\foregroundsettings3.md
created_at: 2025-07-03
---






##### Foreground Settings {#foreground-settings style="tab-stops: 0pt"}

[] 

This section will walk you through the foreground settings of the Dock tabs, caption area and AutoHidden tabs.

[] 

###### 3.2.3.5.1.1 Dock Tab and Label Settings {#dock-tab-and-label-settings style="tab-stops: 0pt"}

[] 

The docking Manager provides tab and label settings for the docked windows. These settings lets you control the appearance of the dock tabs.

[] 

Foreground Settings for the Dock Tabs

**[]** 

The font style and the height of the tab controls in a tabbed docking group, can be controlled using the below properties respectively.

[] 


  ------------------------- ---------------------------------------------------------------------------
  DockingManager Property   Description
  DockTabFont               Gets or sets the font for the tab control used in tabbed docking group.
  DockTabHeight             Gets or sets the height for the tab control used in tabbed docking group.
  ------------------------- ---------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                        |
| [this][.dockingManager1.DockTabFont = [new] System.Drawing.Font(\"Arial\", 9F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold \| System.Drawing.FontStyle.Underline))), System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));] |
|                                                                                                                                                                                                                                                                                                                                                        |
| [this][.dockingManager1.DockTabHeight = 30;]                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Me][.DockingManager1.DockTabFont = [New] System.Drawing.Font(\"Arial\", 9.0!, [CType]((System.Drawing.FontStyle.Bold [Or] System.Drawing.FontStyle.Underline), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, [CType](0, [Byte]))] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Me][.DockingManager1.DockTabHeight = 30]                                                                                                                                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 72: FontStyle = \"Arial 9, Bold, Underline\"; TabHeight = \"30\"

[] 


{border="0"} Note:[ ]ResetDockTabFont and ResetDockTabHeight methods lets you reset the above settings.


[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                      |
|                                                                                                                                     |
| []                                                                                              |
|                                                                                                                                     |
| [//Restoring to default settings]                                                 |
|                                                                                                                                     |
| [this][.dockingManager1.ResetDockTabFont();]   |
|                                                                                                                                     |
| [this][.dockingManager1.ResetDockTabHeight();] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                               |
|                                                                                                                                  |
| []                                                                                           |
|                                                                                                                                  |
| [\'Restoring to default settings]                                              |
|                                                                                                                                  |
| [Me][.dockingManager1.ResetDockTabFont()]   |
|                                                                                                                                  |
| [Me][.dockingManager1.ResetDockTabHeight()] |
+----------------------------------------------------------------------------------------------------------------------------------+

**[]** 

See Also

[] 

Tabbing the Docked controls in Tabbed Docking[]

###### []{#p66}[]{#_AutoHidden_Tabs}3.2.3.5.1.2 AutoHidden Tabs {#autohidden-tabs style="tab-stops: 0pt"}

[] 

The font style for the autohidden tabs can be specified in **AutoHideTabFont** property.

[] 


  ------------------------- ----------------------------------------------------
  DockingManager Property   Description
  AutoHideTabFont           Gets or sets the tab for the autohide tab control.
  ------------------------- ----------------------------------------------------


 


{border="0"} Note: This setting will effect only with DockingManager.VisualStyle property set as Default.


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [//Setting Auto hide tab Font style]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [this][.dockingManager1.AutoHideTabFont = [new] System.Drawing.Font(\"Arial\", 9.75F, ((System.Drawing.FontStyle)(((System.Drawing.FontStyle.Bold \| System.Drawing.FontStyle.Italic) ] |
|                                                                                                                                                                                                                                                                                                   |
| [\| System.Drawing.FontStyle.Underline))), System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));]                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [\'Setting Auto hide tab Font style]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                           |
| [Me][.DockingManager1.AutoHideTabFont = [New] System.Drawing.Font(\"Arial\", 9.75!, [CType](((System.Drawing.FontStyle.Bold [Or] System.Drawing.FontStyle.Italic) \_] |
|                                                                                                                                                                                                                                                                                                                           |
| [Or][ System.Drawing.FontStyle.Underline), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, [CType](0, [Byte]))]                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 73: Docked Window with AutoHideTabFont Set

**[]** 

The height for the auto hidden tabs can be specified in **AutoHideTabHeight** property.

[] 


  ------------------------- ------------------------------------------------------
  DockingManager Property   Description
  AutoHideTabHeight         Gets or sets the height of the autohide tab control.
  ------------------------- ------------------------------------------------------


[] 


{border="0"} Note: This setting will effect only with DockingManager.VisualStyle property set as Default.


[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                       |
| **[]**                                                                              |
|                                                                                                                                       |
| [//Setting Auto hide tab height]                                                    |
|                                                                                                                                       |
| [this][.dockingManager1.AutoHideTabHeight = 35;] |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                 |
|                                                                                                                                    |
| []                                                                               |
|                                                                                                                                    |
| [\'Setting Auto hide tab height]                                                 |
|                                                                                                                                    |
| [Me][.DockingManager1.AutoHideTabHeight = 35] |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 74: Docked Window with AutoHideTabHeight Set

**[]** 

See Also

[] 

[Visual Styles]{.UGHyperlink}[]{.UGHyperlink}

 

###### []{#p67}[]{#_Active_and_Inactive}3.2.3.5.1.3 Active and Inactive caption {#active-and-inactive-caption style="tab-stops: 0pt"}

 

Active Caption Settings

[] 

Caption FontStyle and foreground settings, for an active docked control, can be controlled by **ActiveCaptionFont** and **ActiveCaptionForeGround** properties.

[] 


  ------------------------- --------------------------------------------------------------
  DockingManager Property   Description
  ActiveCaptionFont         Gets or sets the font for the active caption.
  ActiveCaptionForeGround   Indicates the color of the caption text in the active state.
  ------------------------- --------------------------------------------------------------


[] 


{border="0"} Note: These settings will effect only with DockingManager.VisualStyle property set as Default.


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [this][.dockingManager1.ActiveCaptionFont = [new] System.Drawing.Font(\"Trebuchet MS\", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));] |
|                                                                                                                                                                                                                                                                                                  |
| [this][.dockingManager1.ActiveCaptionForeGround = System.Drawing.Color.Red;]                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [Me][.dockingManager1.ActiveCaptionFont = [New] System.Drawing.Font(\"Trebuchet MS\", 9.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, [CType](0, [Byte]))] |
|                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [Me][.DockingManager1.ActiveCaptionForeGround = System.Drawing.Color.Red]                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 75: Docked Window with Active Caption Foreground Set

**[]** 

Inactive Caption settings

**[]** 

By setting the **InactiveCaptionFont** and **InactiveCaptionForeGround** properties, the caption foreground appearance of the inactive controls among the docked controls can be customized.

**[]** 


  --------------------------- ------------------------------------------------------------
  DockingManager Property     Description
  InactiveCaptionFont         Gets or sets the font of the inactive caption.
  InactiveCaptionForeGround   Indicates the color of the caption text in inactive state.
  --------------------------- ------------------------------------------------------------


**[]** 


{border="0"} Note: These settings will effect only with DockingManager.VisualStyle property set as Default.


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                              |
| [this][.dockingManager1.InActiveCaptionFont = [new] System.Drawing.Font(\"Arial\", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));] |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [this][.dockingManager1.InActiveCaptionForeGround = System.Drawing.Color.Blue;]                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                     |
| [Me][.DockingManager1.InActiveCaptionFont = [New] System.Drawing.Font(\"Arial\", 11.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, [CType](0, [Byte]))] |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                     |
| [Me][.DockingManager1.InActiveCaptionForeGround = System.Drawing.Color.MediumSlateBlue]                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 76: Docked Window with Inactive Captions

**[]** 

The Docking Manager provides the ProvideGraphicsItems event that can be handled for custom rendering the docking window caption area. This event is fired whenever a docking window's caption needs to be painted and the ProvideGraphicsItemsEventArgs provides the control being drawn and allows you to specify the new set of graphics objects to use.

[] 

See Also

[] 

[Visual Styles]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

