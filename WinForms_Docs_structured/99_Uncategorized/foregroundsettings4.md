---
title: foregroundsettings4.md
original_path: WinForms_Docs/99_Uncategorized/foregroundsettings4.md
created_at: 2025-08-05
---






##### Foreground Settings {#foreground-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section discusses the foreground settings of the ProgressBarAdv control.

 

The topics included are given below.

[] 

[] 

 

 

 

[]{#p711} 

###### 3.7.1.3.3.1      Foreground Segment Settings {#foreground-segment-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The foreground segment settings available in the ProgressBarAdv control are explained below.

[] 

The foreground of the ProgressBarAdv can be displayed with a segmented appearance using the property given below.

[] 


  ------------------------- --------------------------------------------
  ProgressBarAdv Property   Description
  ForeSegments              Determines if the foreground is segmented.
  ------------------------- --------------------------------------------


[] 

By default this property will be set to \'True\'. To set it to \'False\', use the code snippet given below.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [this][.progressBarAdv1.ForeSegments = [false];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                      |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [Me][.progressBarAdv1.ForeSegments = [False]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

[] 

Figure 963: ForeSegments property set to \"False\"

[] 

Segment Width

[] 

The foreground segments can be customized using the property given below.

[] 


  ------------------------- --------------------------------------
  ProgressBarAdv Property   Description
  SegmentWidth              Specifies the width of the segments.
  ------------------------- --------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [this][.progressBarAdv1.SegmentWidth = 20;] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                            |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [Me][.progressBarAdv1.SegmentWidth = 20] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 964: SegmentWidth property set to \"20\"

[] 

See Also

**[]** 

[[Background Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Background_Settings)[]{.UGHyperlink}

 

 

 

[]{#p712} 

###### 3.7.1.3.3.2      Foreground Color Settings {#foreground-color-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section illustrates the color settings that can be applied to the foreground of the ProgressBarAdv.

[] 

Font and Fore Color Settings

[] 

The font color and the fore color can be set using the properties given below.

[] 


  ------------------------- ------------------------------------------------------------------------------------
  ProgressBarAdv Property   Description
  ForeColor                 Specifies the color used to draw the foreground in segment mode and constant mode.
  FontColor                 Specifies the color of the font used to draw the text of the ProgressBarAdv.
  ------------------------- ------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [this][.progressBarAdv1.FontColor = System.Drawing.[Color].SteelBlue;] |
|                                                                                                                                                                                  |
| [this][.progressBarAdv1.ForeColor = System.Drawing.[Color].Turquoise;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                            |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [Me][.progressBarAdv1.FontColor = System.Drawing.[Color].SteelBlue] |
|                                                                                                                                                                               |
| [Me][.progressBarAdv1.ForeColor = System.Drawing.[Color].Turquoise] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 965: FontColor and ForeColor Set

[] 

Gradient Color Settings

[] 

The color of the foreground gradient can be changed using the properties given below.

[] 


+-----------------------------------+-----------------------------------------------------------+
| ProgressBarAdv Property           | Description                                               |
+-----------------------------------+-----------------------------------------------------------+
| GradientStartColor                | Specifies the start color of the foreground gradient.     |
|                                   |                                                           |
|                                   |                                                           |
|                                   |                                                           |
|                                   | The ProgressStyle property should be set to \'Gradient\'. |
+-----------------------------------+-----------------------------------------------------------+
| GradientEndColor                  | Specifies the start color of the foreground gradient.     |
|                                   |                                                           |
|                                   |                                                           |
|                                   |                                                           |
|                                   | The ProgressStyle property should be set to \'Gradient\'. |
+-----------------------------------+-----------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [this][.progressBarAdv1.GradientEndColor = System.Drawing.[Color].Yellow;]      |
|                                                                                                                                                                                           |
| [this][.progressBarAdv1.GradientStartColor = System.Drawing.[Color].OrangeRed;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                              |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [Me][.progressBarAdv1.GradientEndColor = System.Drawing.Color.Yellow]      |
|                                                                                                                                                                 |
| [Me][.progressBarAdv1.GradientStartColor = System.Drawing.Color.OrangeRed] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 966: Foreground Gradient Color Set

[] 

The foreground can be displayed with multiple colors using the property given below.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------+
| ProgressBarAdv Property           | Description                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------+
| MultipleColors                    | Specifies the array of colors used to draw the multiple gradient of the foreground. |
|                                   |                                                                                     |
|                                   |                                                                                     |
|                                   |                                                                                     |
|                                   | The ProgressStyle property should be set to \'MultipleGradient\'.                   |
+-----------------------------------+-------------------------------------------------------------------------------------+
| StretchMultGrad                   | Determines if the multiple gradient will be stretched.                              |
+-----------------------------------+-------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.progressBarAdv1.ProgressStyle = Syncfusion.Windows.Forms.Tools.[ProgressBarStyles].MultipleGradient;]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.progressBarAdv1.MultipleColors = [new] System.Drawing.[Color]\[\] {System.Drawing.[Color].Orange, System.Drawing.[Color].Yellow, System.Drawing.[Color].Blue, System.Drawing.[Color].Pink, System.Drawing.[Color].Green};] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.progressBarAdv1.StretchMultGrad = [false];]                                                                                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [Me][.progressBarAdv1.ProgressStyle = Syncfusion.Windows.Forms.Tools.ProgressBarStyles.MultipleGradient]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                |
| [Me][.progressBarAdv1.MultipleColors = [New] System.Drawing.Color\[\] {System.Drawing.Color.Orange, System.Drawing.Color.Yellow, System.Drawing.Color.Blue, System.Drawing.Color.Pink, System.Drawing.Color.Green};] |
|                                                                                                                                                                                                                                                                                                                                |
| [Me][.progressBarAdv1.StretchMultGrad = [False]]                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 967: Foreground Gradient displayed with Multiple Colors

[] 

Tube Color Settings

[] 

Colors can be set for the foreground tube of the ProgressBarAdv.

[] 


+-----------------------------------+-------------------------------------------------------+
| ProgressBarAdv Property           | Description                                           |
+-----------------------------------+-------------------------------------------------------+
| TubeStartColor                    | Specifies the start color of the foreground tube.     |
|                                   |                                                       |
|                                   |                                                       |
|                                   |                                                       |
|                                   | The ProgressStyle property should be set to \'Tube\'. |
+-----------------------------------+-------------------------------------------------------+
| TubeEndColor                      | Specifies the start color of the foreground tube.     |
|                                   |                                                       |
|                                   |                                                       |
|                                   |                                                       |
|                                   | The ProgressStyle property should be set to \'Tube\'. |
+-----------------------------------+-------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [this][.progressBarAdv1.TubeEndColor = System.Drawing.[Color].Black;] |
|                                                                                                                                                                                 |
| [this][.progressBarAdv1.TubeStartColor = System.Drawing.[Color].Red;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                    |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [Me][.progressBarAdv1.TubeEndColor = System.Drawing.Color.Black] |
|                                                                                                                                                       |
| [Me][.progressBarAdv1.TubeStartColor = System.Drawing.Color.Red] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 968: Foreground Tube Color Set

[] 

See Also

[] 

[[Background Color Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Background_Color_Settings)[]{.UGHyperlink}

 

 

 

[]{#p713} 

###### 3.7.1.3.3.3      Foreground Image Settings {#foreground-image-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section discusses the foreground image settings of ProgressBarAdv.

 

When the BackgroundStyle and ProgressStyle are set to the \'Image\' style, then the foreground image can be specified using the below given property.

[] 


  ------------------------- -----------------------------------------------------------
  ProgressBarAdv Property   Description
  ForegroundImage           Determines if the foreground is segmented.
  StretchImage              Indicates whether the foreground image will be stretched.
  ------------------------- -----------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                              |
| [this][.progressBarAdv1.ForegroundImage = ((System.Drawing.[Image])(resources.GetObject(][\"clouds\"][)));] |
|                                                                                                                                                                                                                                                                                                              |
| [this][.progressBarAdv1.StretchImage = [true];]                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
| [Me][.progressBarAdv1.ForegroundImage = [CType]((resources.GetObject(][\"clouds\"][)), System.Drawing.[Image])] |
|                                                                                                                                                                                                                                                                                                                                       |
| [Me][.progressBarAdv1.StretchImage = [True]]                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

[] 

Figure 969: ProgressBarAdv displayed with Foreground Image

 

 

 

[]{#p714} 

###### []{#_Foreground_Style_Settings}3.7.1.3.3.4      Foreground Style Settings {#foreground-style-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The progress style of the ProgressBarAdv control can be set using the properties given below.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ProgressBarAdv Property           | Description                                                                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ProgressStyle                     | Determines the foreground drawing style. It includes the options given below.                                                     |
|                                   |                                                                                                                                   |
|                                   |                                                                                                                                   |
|                                   |                                                                                                                                   |
|                                   | [·      ]Constant,                                                                                   |
|                                   |                                                                                                                                   |
|                                   | [·      ]Gradient,                                                                                   |
|                                   |                                                                                                                                   |
|                                   | [·      ]MultipleGradient,                                                                           |
|                                   |                                                                                                                                   |
|                                   | [·      ]Tube,                                                                                       |
|                                   |                                                                                                                                   |
|                                   | [·      ]Image and                                                                                   |
|                                   |                                                                                                                                   |
|                                   | [·      ]System.                                                                                     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ProgressFallbackStyle             | Determines the foreground drawing style when the ProgressStyle is set to \'System\', provided the system doesn\'t support themes. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [this][.progressBarAdv1.ProgressStyle = Syncfusion.Windows.Forms.Tools.[ProgressBarStyles].WaitingGradient;]          |
|                                                                                                                                                                                                                                 |
| [this][.progressBarAdv1.ProgressFallbackStyle = Syncfusion.Windows.Forms.Tools.[ProgressBarStyles].MultipleGradient;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [Me][.progressBarAdv1.ProgressStyle = Syncfusion.Windows.Forms.Tools.ProgressBarStyles.WaitingGradient]                                   |
|                                                                                                                                                                                                                                |
| [Me][.progressBarAdv1.ProgressFallbackStyle = Syncfusion.Windows.Forms.Tools.[ProgressBarStyles].MultipleGradient;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

[] 

Figure 970: Foreground Styles

[] 

The **Waiting Gradient** Style of the ProgressBarAdv consists of the following properties that can be used to change the appearance and behavior of the style.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ProgressBarAdv Property           | Description                                                                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| WaitingGradientEnabled            | Determines if the waiting gradient is enabled.                                                                                          |
|                                   |                                                                                                                                         |
|                                   |                                                                                                                                         |
|                                   |                                                                                                                                         |
|                                   | The ProgressStyle property should be set to \'WaitingGradient\'.                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| WaitingGradientInterval           | Determines the interval of the waiting gradient.                                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| WaitingGradientWidth              | Determines the width of the waiting gradient.                                                                                           |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| CustomWaitingRender               | Indicates whether the waiting gradient will be replaced by another custom waiting render which is defaulted to segments.                |
|                                   |                                                                                                                                         |
|                                   |                                                                                                                                         |
|                                   |                                                                                                                                         |
|                                   | This property when set to \'True\' will display the foreground with segments in the color that has been set for the ForeColor property. |
|                                   |                                                                                                                                         |
|                                   |                                                                                                                                         |
|                                   |                                                                                                                                         |
|                                   | This property when set to \'False\' will display the foreground in the default waiting gradient style.                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [this][.progressBarAdv1.WaitingGradientEnabled = [true];]            |
|                                                                                                                                                                                |
| [this][.progressBarAdv1.WaitingGradientInterval = 20;]                                    |
|                                                                                                                                                                                |
| [this][.progressBarAdv1.WaitingGradientWidth = 500;]                                      |
|                                                                                                                                                                                |
| [this][.progressBarAdv1.CustomWaitingRender = [true];]               |
|                                                                                                                                                                                |
| [this][.progressBarAdv1.ForeColor = System.Drawing.[Color].Crimson;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [Me][.progressBarAdv1.WaitingGradientEnabled = [True]] |
|                                                                                                                                                                  |
| [Me][.progressBarAdv1.WaitingGradientInterval = 20]                         |
|                                                                                                                                                                  |
| [Me][.progressBarAdv1.WaitingGradientWidth = 500]                           |
|                                                                                                                                                                  |
| [Me][.progressBarAdv1.CustomWaitingRender = [True]]    |
|                                                                                                                                                                  |
| [Me][.progressBarAdv1.ForeColor = System.Drawing.Color.Crimson]             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 971: CustomWaitingRender property of ProgressBarAdv

[] 

See Also

[] 

[[Background Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Background_Settings)[]{.UGHyperlink}

 

 

 

[]{#p715} 

[]{#related-topics}

