---
title: conceptsandfeatures7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\conceptsandfeatures7.md
created_at: 2025-07-03
---






##### Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

 

This section discusses the various features of the DropDownCalendarControl. It includes the following topics:

###### 5.1.2.3.2.1 Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

Aligning the control\'s value

[] 

The value of the calendar control inside the textbox can be aligned accordingly by setting the **TextAlignment** to the required option.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------+
|                                   |                                                                                                   |
|                                   |                                                                                                   |
| Property                          | Description                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| TextAlignment                     | Specifies the alignment of the value. Default value is Left. The options included are as follows: |
|                                   |                                                                                                   |
|                                   | [·      ]Left                                                        |
|                                   |                                                                                                   |
|                                   | [·      ]Right                                                       |
|                                   |                                                                                                   |
|                                   | [·      ]Center                                                      |
|                                   |                                                                                                   |
|                                   | [·      ]Justify                                                     |
+-----------------------------------+---------------------------------------------------------------------------------------------------+


[] 

Programmatically the alignment can be set as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                                          |
| []                                                                                      |
|                                                                                                                                                          |
| [DropDownCalendarControl1.TextAlignment = Syncfusion.Web.UI.[TextAlign].Right;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                            |
|                                                                                                                                                                                                             |
| []                                                                                                                                         |
|                                                                                                                                                                                                             |
| [Private][ DropDownCalendarControl1.TextAlignment = Syncfusion.Web.UI.TextAlign.Right] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Button Settings

[] 

Custom images can be set for the control that responds to user click action and drops down and displays the calendar. The default drop-down button can be replaced by setting the **DropDownElementType** to **Image**, and by providing the path of the image to the **DropDownImgSrc** property.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| DropDownElementType               | Specifies whether to display drop down button for calendar as button or image. Default value is Button. The options included are as follows. |
|                                   |                                                                                                                                              |
|                                   |                                                                                                                                              |
|                                   |                                                                                                                                              |
|                                   | [·      ]*Button*                                                                                               |
|                                   |                                                                                                                                              |
|                                   | [·      ]*Image*                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| DropDownImgSrc                    | Specifies the full path of the image to be displayed as the drop down button, which on clicking displays the calendar.                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Null Date and Value Settings

[] 

The control can be enabled to accept null/empty values by setting the **EnableNullDate** property.

Assigning some text to the **NullString** property, displays that string, when no date is selected.

To display some text in the control by default, instead of displaying the current date, **IsNullDate** can be enabled and the text to be displayed has to be set to NullString property. If no text is set, then no value will be displayed, in the control, initially.

By setting **EnableNullKeys**, when BACKSPACE or DELETE key is pressed, null value or text string can be displayed, when the focus is on the control.

**[]** 


  ---------------- ---------------------------------------------------------------------------------------------------------------------------------
  Property         Description
  EnableNullDate   Gets / sets the boolean value whether to enable null value. Default value is False.
  EnableNullKeys   Gets / sets the boolean value whether to reset the date to null when BACKSPACE or DELETE keys are used. Default value is False.
  IsNullDate       Gets / sets the boolean value to indicate if no date is selected. Default value is False.
  NullString       Specifies the text to display when no date is selected.
  ---------------- ---------------------------------------------------------------------------------------------------------------------------------


[] 

Programmatically the null string settings can be specified as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                       |
|                                                                                                                                                        |
| []                                                                                    |
|                                                                                                                                                        |
| [DropDownCalendarControl1.EnableNullDate = [true];]                           |
|                                                                                                                                                        |
| [DropDownCalendarControl1.EnableNullKeys = [true];]                           |
|                                                                                                                                                        |
| [DropDownCalendarControl1.NullString = [\"Select a date - not optional\"];] |
|                                                                                                                                                        |
| [DropDownCalendarControl1.IsNullDate = [true];]                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [Private][ DropDownCalendarControl1.EnableNullDate = [True]]                           |
|                                                                                                                                                                                                                                  |
| [Private][ DropDownCalendarControl1.EnableNullKeys = [True]]                           |
|                                                                                                                                                                                                                                  |
| [Private][ DropDownCalendarControl1.NullString = [\"Select a date - not optional\"]] |
|                                                                                                                                                                                                                                  |
| [Private][ DropDownCalendarControl1.IsNullDate = [True]]                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Setting Start and End dates

[] 

The start and end dates can be specified, such that values can be selected only between those dates by setting the **MaxVaue** and the **MinValue** properties. The default MaxValue is **12/31/2099** and the default MinValue is **1/1/1900**.

[] 


+-----------------------------------+-------------------------------------------------------+
|                                   |                                                       |
|                                   |                                                       |
| Property                          | Description                                           |
+-----------------------------------+-------------------------------------------------------+
| MaxValue                          | Specifies the maximum value displayed by the control. |
+-----------------------------------+-------------------------------------------------------+
| MinValue                          | Specifies the minimum value displayed by the control. |
+-----------------------------------+-------------------------------------------------------+


[] 

Programmatically the min and max dates can be set as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                    |
| []                                                                                                |
|                                                                                                                                                                    |
| [DropDownCalendarControl1.MaxValue = [new] [DateTime](2007, 12, 1);] |
|                                                                                                                                                                    |
| [DropDownCalendarControl1.MinValue = [new] [DateTime](2007, 1, 1);]  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                   |
|                                                                                                                                                                                                                       |
| [Private][ DropDownCalendarControl1.MaxValue = [New] DateTime(2007, 12, 1)] |
|                                                                                                                                                                                                                       |
| [Private][ DropDownCalendarControl1.MinValue = [New] DateTime(2007, 1, 1)]  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Indicating error values

[] 

Back and fore colors can be applied to indicate the error values, i.e., values beyond the min and max values, by setting the **ErrorBackColor** and **ErrorForeColor** properties.

[] 


  ---------------- ----------------------------------------------------------------------------
  Property         Description
  ErrorBackColor   Specifies the back color to use to indicate the date or time is not valid.
  ErrorForeColor   Specifies the fore color to use to indicate that the input is not valid.
  ---------------- ----------------------------------------------------------------------------


[] 

Programmatically the error colors can be set as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                                             |
| []                                                                                         |
|                                                                                                                                                             |
| [DropDownCalendarControl1.ErrorBackColor = System.Drawing.[Color].BlanchedAlmond;] |
|                                                                                                                                                             |
| [DropDownCalendarControl1.ErrorForeColor = System.Drawing.[Color].CadetBlue;]      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                               |
|                                                                                                                                                                                                                |
| []                                                                                                                                            |
|                                                                                                                                                                                                                |
| [Private][ DropDownCalendarControl1.ErrorBackColor = System.Drawing.Color.BlanchedAlmond] |
|                                                                                                                                                                                                                |
| [Private][ DropDownCalendarControl1.ErrorForeColor = System.Drawing.Color.CadetBlue]      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When **SpaceSymbol** is set, the unoccupied spaces for the date, day, month, year and time will be replaced with that symbol. By default, the value is a single white space.

[] 


  ------------- ------------------------------------------------------------------------------
  Property      Description
  SpaceSymbol   Specifies the symbol to use for filling the extra spaces of date time value.
  ------------- ------------------------------------------------------------------------------


[] 

Programmatically the space symbol can be set as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                              |
|                                                                                                                               |
| []                                                           |
|                                                                                                                               |
| [DropDownCalendarControl1.SpaceSymbol = [\'\*\'];] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                         |
|                                                                                                                                                                                                          |
| []                                                                                                                                      |
|                                                                                                                                                                                                          |
| [Private ][DropDownCalendarControl1.SpaceSymbol = [\"\*\"c]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

RightToLeft property

[] 

You can align the elements of the DropDownCalendarControl using this property.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                              |
|                                   |                                                                                                                              |
| Property                          | Description                                                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| RightToLeft                       | Gets / sets a value indicating whether the elements of the control are aligned to support locales using right-to-left fonts. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                          |
|                                                                                                                           |
| []                                                       |
|                                                                                                                           |
| [DropDownCalendarControl1.RightToLeft = [true];] |
+---------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                    |
|                                                                                                                                                                                                     |
| []                                                                                                                                 |
|                                                                                                                                                                                                     |
| [Private][ DropDownCalendarControl1.RightToLeft = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 54: Elements of the DropDownCalendarControl is aligned to Left

 

###### 5.1.2.3.2.2 Display Setting for Year Combo {#display-setting-for-year-combo style="tab-stops: 0pt"}

[] 

Number of years to be displayed in the drop-down can be customized by setting the appropriate value to the **YearsCount** property.

[] 


  ------------ ------------------------------------------------------------------------------------------------------------
  Property     Description
  YearsCount   Specifies the number of years to be displayed in the year drop down combo of the DropDownCalendar control.
  ------------ ------------------------------------------------------------------------------------------------------------


[] 

The following code snippet illustrates setting of 20 years in the drop-down. For example: From the year 1999-2018.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][syncfusion][:][DropDownCalendarControl][ [ID][=\"DropDownCalendarControl1\"] [runat][=\"server\"] [YearsCount][=\"20\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][syncfusion][:][DropDownCalendarControl][\>]                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                |
|                                                                                                 |
| **[]**                                      |
|                                                                                                 |
| [DropDownCalendarControl1.YearsCount = 20;] |
+-------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                           |
| **[]**                                                                                                                |
|                                                                                                                                                                           |
| [Private][ DropDownCalendarControl1.YearsCount = 20] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

Figure 55: YearsCount = \"20\"

 

###### 5.1.2.3.2.3 Date and Time Format {#date-and-time-format style="tab-stops: 0pt"}

[] 

The control offers various pre-defined formats, in which the date-time values can be displayed, by setting the required option to the **Format** property.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------+
| Property                          | Description                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------+
| Format                            | Represents the date-time format of the control. The options included are as follows: |
|                                   |                                                                                      |
|                                   | [·      ]Long                                           |
|                                   |                                                                                      |
|                                   | [·      ]Short                                          |
|                                   |                                                                                      |
|                                   | [·      ]Time                                           |
|                                   |                                                                                      |
|                                   | [·      ]CustomChar                                     |
|                                   |                                                                                      |
|                                   | [·      ]CustomString                                   |
+-----------------------------------+--------------------------------------------------------------------------------------+


[] 

When Format property is set to **CustomChar**, the values set for the **CustomFormatChar** property will be inherited and the date-time will be displayed in that format.

[] 


  ------------------ ---------------------------------------------------------------------------------------------------------
  Property           Description
  CustomFormatChar   Specifies the date-time format type. The various values that can be set are \'D, F, G, M, R, S and Y\'.
  ------------------ ---------------------------------------------------------------------------------------------------------


[] 

Programmatically the property can be set as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                                               |
| []                                                                           |
|                                                                                                                                               |
| [DropDownCalendarControl1.Format = [DateTimeFormatType].CustomChar;] |
|                                                                                                                                               |
| [DropDownCalendarControl1.CustomFormatChar = [\'M\'];]             |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                             |
|                                                                                                                                                                                                              |
| []                                                                                                                                          |
|                                                                                                                                                                                                              |
| [Private][ DropDownCalendarControl1.Format = DateTimeFormatType.CustomChar]             |
|                                                                                                                                                                                                              |
| [Private][ DropDownCalendarControl1.CustomFormatChar = [\"M\"]c] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


  -------------------------- --------------------------------------------------------------------------------------------------------------------------------
           Property          Description
  CustomFormat               Specifies the date format when Format property of DropDownCalendarControl is set to CustomString. For eg: dd/mm/yyyy hh:mm:ss.
  -------------------------- --------------------------------------------------------------------------------------------------------------------------------


 

###### 5.1.2.3.2.4 Culture Settings {#culture-settings style="tab-stops: 0pt"}

[] 

The culture information can be obtained either from the data posted by the browser (By setting the FromClient option) else from the web-server hosting page (By setting the FromServer option) or the user can define the culture settings.

The drop down calendar control allows you to override the default culture information (AM/PM Designator, Time/Date Separator, GroupSeparator, GroupSizes, NegativeSign and CurrencySymbol properties) when the **CultureSource** property is set to **UserOverride**.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------+
| CultureSource                     | Specifies the current culture for the control. The values included are as follows:                      |
|                                   |                                                                                                         |
|                                   | [·      ]*FromClient*: culture is obtained from the data posted by browser |
|                                   |                                                                                                         |
|                                   | [·      ]*FromServer*: culture is obtained from web-server hosting page    |
|                                   |                                                                                                         |
|                                   | [·      ]*UserOverride*: user-defined culture                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------------+


[] 

Globalization

[] 

**UserOvrrideCulture** allows you to set the required culture to represent the value to the specific requirement whose default value is **English(United States)**.

[] 


  --------------------- -------------------------------------------
  Property              Description
  UserOverrideCulture   Specifies the various cultures supported.
  --------------------- -------------------------------------------


[] 

Programmatically UserOverrideCulture can be set as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                                       |
| []                                                                                   |
|                                                                                                                                                       |
| [DropDownCalendarControl1.CultureSource = [CultureSourceType].UserOverride;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                         |
|                                                                                                                                                                                                          |
| []                                                                                                                                      |
|                                                                                                                                                                                                          |
| [Private][ DropDownCalendarControl1.CultureSource = CultureSourceType.UserOverride] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Designators and Separators for time and date

[] 

The AM and PM designators can be used to customize the time convention indicator.

[] 


  -------------- ------------------------------------------------------------------------
  Property       Description
  AMDesignator   Specifies the culture specific AM designator. The default value is AM.
  PMDesignator   Specifies the culture specific PM designator. The default value is PM.
  -------------- ------------------------------------------------------------------------


[] 

Programmatically the designators can be specified as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                                |
| []                                                            |
|                                                                                                                                |
| [DropDownCalendarControl1.AMDesignator=[\"A.M.\"];] |
|                                                                                                                                |
| [DropDownCalendarControl1.PMDesignator=[\"P.M.\"];] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                         |
|                                                                                                                                                                                                          |
| []                                                                                                                                      |
|                                                                                                                                                                                                          |
| [Private][ DropDownCalendarControl1.AMDesignator=[\"A.M.\"]] |
|                                                                                                                                                                                                          |
| [Private][ DropDownCalendarControl1.PMDesignator=[\"P.M.\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The separators for the date and time can be customized using the **DateSeparator** and **TimeSeparator** properties.

[] 


+-----------------------------------+------------------------------------------------------------------+
|                                   |                                                                  |
|                                   |                                                                  |
| Property                          | Description                                                      |
+-----------------------------------+------------------------------------------------------------------+
| DateSeparator                     | Specifies the separator to use for date. Default value is \'/\'. |
+-----------------------------------+------------------------------------------------------------------+
| TimeSeparator                     | Specifies the separator to use for time. Default value is \':\'. |
+-----------------------------------+------------------------------------------------------------------+


[] 

Programmatically the separators can be set as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                                |
| []                                                            |
|                                                                                                                                |
| [DropDownCalendarControl1.DateSeparator = [\"-\"];] |
|                                                                                                                                |
| [DropDownCalendarControl1.TimeSeparator=[\".\"];]   |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                                           |
| [Private][ DropDownCalendarControl1.DateSeparator = [\"-\"];] |
|                                                                                                                                                                                                           |
| [Private][ DropDownCalendarControl1.TimeSeparator=[\".\"]]    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 5.1.2.3.2.5 DropDown Calendar Settings {#dropdown-calendar-settings style="tab-stops: 0pt"}

[] 

Display setting for dropdown calendar

[] 

The dropdown calendar can be made visible by default at design time, on setting the **ShowDropDown** property.

Also the header of the calendar (displaying the month and year dropdowns, and the next and previous month navigation buttons) can be hidden by setting the **ShowHeader** property, which displays only the month that has been set and so the selection can be made only from that month.

[] 


  -------------- --------------------------------------------------------
  Property       Description
  ShowDropDown   Specifies whether to show the dropdown at design time.
  ShowHeader     Indicates whether day header is displayed or not.
  -------------- --------------------------------------------------------


[] 

Programmatically these properties can be set as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                            |
| []                                                        |
|                                                                                                                            |
| [DropDownCalendarControl1.ShowDropDown = [true];] |
|                                                                                                                            |
| [DropDownCalendarControl1.ShowHeader = [false];]  |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                     |
|                                                                                                                                                                                                      |
| []                                                                                                                                  |
|                                                                                                                                                                                                      |
| [Private][ DropDownCalendarControl1.ShowDropDown = [True]] |
|                                                                                                                                                                                                      |
| [Private][ DropDownCalendarControl1.ShowHeader = [False]]  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Display setting for week days

[] 

The week days can be either represented in short form or just the first or first two letters by setting the corresponding options to the **DayNameFormat**.

To customize the beginning day of the week, the required day can be set to the **StartWeekDay** property.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| DayNameFormat                     | Specifies the weekday format for the DropDownCalendarControl. Default value is Short. The options included are as follows: |
|                                   |                                                                                                                            |
|                                   | [·      ]Short                                                                                |
|                                   |                                                                                                                            |
|                                   | [·      ]FirstLetter                                                                          |
|                                   |                                                                                                                            |
|                                   | [·      ]FirstTwoLetter                                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| StartWeekDay                      | Specifies the day to be used as starting day of the week for the control.                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+


[] 

Programmatically the property can be set as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                     |
|                                                                                                                                                                                      |
| []                                                                                                                  |
|                                                                                                                                                                                      |
| [DropDownCalendarControl1.DayNameFormat = Syncfusion.Web.UI.WebControls.Tools.[DayNameFormat].FirstLetter;] |
|                                                                                                                                                                                      |
| [DropDownCalendarControl1.StartWeekDay = [DayOfWeek].Sunday;]                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [Private][ DropDownCalendarControl1.DayNameFormat = Syncfusion.Web.UI.WebControls.Tools.DayNameFormat.FirstLetter] |
|                                                                                                                                                                                                                                         |
| [Private][ DropDownCalendarControl1.StartWeekDay = DayOfWeek.Sunday]                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Month Navigation button settings

[] 


  --------------- -------------------------------------------------------------------------------------------------------
  Property        Description
  NextMonthText   Specifies the text that will be used to indicate the next month string. The default value is \"&gt\".
  PrevMonthText   Specifies the text that will be used for indicating the previous month. The default value is \"&lt\".
  --------------- -------------------------------------------------------------------------------------------------------


[] 

Programmatically the property can be set as follows.

[] 

+---------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                        |
|                                                                                                         |
| []                                     |
|                                                                                                         |
| [DropDownCalendarControl1.NextMonthText= \"&gt\";]  |
|                                                                                                         |
| [DropDownCalendarControl1.PrevMonthText = \"&lt\";] |
+---------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                  |
|                                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                                   |
| [Private ][DropDownCalendarControl1.NextMonthText= \"&gt\"]  |
|                                                                                                                                                                                   |
| [Private ][DropDownCalendarControl1.PrevMonthText = \"&lt\"] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Cell settings

[] 

Padding for calendar cells can be applied using **CellPadding** and space between cells can be set through **CellSpacing** properties.

[] 


  ------------- --------------------------------------------
  Property      Description
  CellPadding   Specifies the calendar table cell padding.
  CellSpacing   Specifies the calendar table cell spacing.
  ------------- --------------------------------------------


[] 

Programmatically the property can be set as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                             |
|                                                                                                                              |
| []                                                          |
|                                                                                                                              |
| [DropDownCalendarControl1.CellPadding = [\'1\'];] |
|                                                                                                                              |
| [DropDownCalendarControl1.CellSpacing = [\'1\'];] |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                        |
|                                                                                                                                                                                                         |
| []                                                                                                                                     |
|                                                                                                                                                                                                         |
| [Private][ DropDownCalendarControl1.CellPadding = [\"1\"]c] |
|                                                                                                                                                                                                         |
| [Private][ DropDownCalendarControl1.CellSpacing = [\"1\"]c] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### 5.1.2.3.2.6 ClientObjectID {#clientobjectid style="tab-stops: 0pt"}

[] 

The ClientObjectID can be used to access the control\'s object model on the client side.

ClientObjectID can be effectively used to refer the control\'s objects when used with MasterPages and UserControls. By default, a client object id is computed by concatenating \'\_sf\' and the control\'s **ID** property. However in the case of hosting the control in a MasterPage or UserControl, the computed client object id is very unintuitive. To make things simpler you can specify a custom value on this property and access the client side object model using that value.

[] 


  ---------------- ------------------------------------------------------------------------
  Property         Description
  ClientObjectID   Specifies the user defined id for accessing the object on client side.
  ---------------- ------------------------------------------------------------------------


[] 

Programmatically the ClientObjectID can be set as follows.

[  ]

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                         |
| []                                                                     |
|                                                                                                                                         |
| [DropDownCalendarControl1.ClientObjectID = [\"Custom ID\"];] |
+-----------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| []                                                                                                                                               |
|                                                                                                                                                                                                                   |
| [Private][ DropDownCalendarControl1.ClientObjectID = [\"Custom ID\"]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 5.1.2.3.2.7 Look and Feel Settings {#look-and-feel-settings style="tab-stops: 0pt"}

 

The DropDownCalendarControl can be customized with the pre-defined style settings by using the AutoFormat options and by handling the various style properties discussed in this section    []{#p73}

5.1.2.3.2.7.1      AutoFormat Style Options

[] 

The DropDownCalendarControl control provides pre-defined set of styles that can be applied to your control just on a click of the button. You can set the desired look and feel for the control that includes some popular styles too.

Right-clicking the control and selecting the \'Auto Format\...\' option opens the following Auto Format dialog box.

[] 

{border="0"}

Figure 56

[] 

The left pane lists the various pre-defined style scheme that are available. The right pane shows the preview of the currently selected scheme. Select the required style and click OK to apply the selected scheme to the control.

[] 

Example of a popular look and feel

[] 

The following image shows the DropDownCalendarControl with **Image Blue** style setting.

[] 

{border="0"}

Figure 57

 

5.1.2.3.2.7.2      Style Settings

[] 

The various style properties allows you to set styles for the various segments of the dropdown calendar control. Style settings enable to customize the font and it\'s styles, borders and it\'s styles, and the alignment of the values.

[] 

{border="0"}

[] 

Figure 58: Calendar control with style settings for dropdown calendar

[] 


+-----------------------+-------------------------------+------------------------------------------------------------+
| Property              | Color                         | Description                                                |
+-----------------------+-------------------------------+------------------------------------------------------------+
| CalendarStyle         | 
|                       |   --------------------------- |                                                            |
|                       |   []    |                                                            |
|                       |   --------------------------- |                                                            |
|                       | 
+-----------------------+-------------------------------+------------------------------------------------------------+
| DayHeaderStyle        | 
|                       |   --------------------------- |                                                            |
|                       |   []    |                                                            |
|                       |   --------------------------- |                                                            |
|                       | 
+-----------------------+-------------------------------+------------------------------------------------------------+
| DayStyle              | 
|                       |   --------------------------- |                                                            |
|                       |   []    |                                                            |
|                       |   --------------------------- |                                                            |
|                       | 
+-----------------------+-------------------------------+------------------------------------------------------------+
| OtherDayStyle         | 
|                       |   --------------------------- |                                                            |
|                       |   []    |                                                            |
|                       |   --------------------------- |                                                            |
|                       | 
+-----------------------+-------------------------------+------------------------------------------------------------+
| SelectedDayStyle      | 
|                       |   --------------------------- |                                                            |
|                       |   []    |                                                            |
|                       |   --------------------------- |                                                            |
|                       | 
+-----------------------+-------------------------------+------------------------------------------------------------+
| TitleStyle            | 
|                       |   --------------------------- |                                                            |
|                       |   []    |                                                            |
|                       |   --------------------------- |                                                            |
|                       | 
+-----------------------+-------------------------------+------------------------------------------------------------+
| TodayDayStyle         | 
|                       |   --------------------------- |                                                            |
|                       |   []    |                                                            |
|                       |   --------------------------- |                                                            |
|                       | 
+-----------------------+-------------------------------+------------------------------------------------------------+
| WeekendDayStyle       | 
|                       |   --------------------------- |                                                            |
|                       |   []    |                                                            |
|                       |   --------------------------- |                                                            |
|                       | 
+-----------------------+-------------------------------+------------------------------------------------------------+


 

###### 5.1.2.3.2.8 Client-Side Object Model {#client-side-object-model style="tab-stops: 0pt"}

[] 

The client side methods can be used to control the behavior of the DropDownCalendarControl, that allows to interact with it. All the following methods of DropDownCalendarControl client side object are as follows.

[] 


  ---------- ----------- ------------- ---------------------------------------
  Method     Parameter   Return Type   Description
  GetText    \-          string        Get text of TextBox.
  SetText    string      \-            Set text of TextBox.
  GetValue   \-          Date          Get value of DropDownCalendarControl.
  SetValue   Date        \-            Set value of DropDownCalendarControl.
  ---------- ----------- ------------- ---------------------------------------


[] 

The following code snippet demonstrates how to use **GetText** method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][ssw][:][DropDownCalendarControl][ [ID][=\"DropDownCalendarControl1\"] [ClientObjectId][=\"\_sfDropDownCalendarControl1\"] [runat][=\"server\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][input][ [type][=\"button\"] [value][=\"Show Date\"] [onclick][=\"alert(**\_sfDropDownCalendarControl1.GetText()**)\"] [/\>]]                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

ClientEventData Object for DropDownCalendarControl Client-Side Events

**[]** 


  -------------- -------- -------------------------------------------------------------------------------------
  Property       Type     Description
  ID             string   Specifies the client side identifier.
  Text           string   Specifies the text of textbox.
  Tooltip        string   Specifies the help message that showing when user moves the mouse over the control.
  Value          Date     Value of DropDownCalendarControl.
  InstanceName   string   Specifies the client-side DropDownCalendarControl object identifier.
  Instance       object   Represents DropDownCalendarControl client-side object.
  HtmlID         string   Specifies DropDownCalendarControl HTML-element identifier.
  Element        object   Represents DropDownCalendarControl HTML-element.
  TextBox        object   Represents textbox HTML-element.
  Event          object   Represents event.
  -------------- -------- -------------------------------------------------------------------------------------


[] 

See Also

[] 

[Client-Side Events]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#related-topics}

