---
title: customizingdayheadertext.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizingdayheadertext.md
created_at: 2025-07-03
---








  









### Customizing Day Header Text {#customizing-day-header-text style="LINE-HEIGHT: 150%; tab-stops: 0pt"}

[·      ]You can customize the day header text using converter properties in schedule control.

[·      ]For **DaysView,** header text customization uses the **DaysHeaderTextConverter** property and for **MonthView,** header text customization uses the **MonthViewDateTextConverter** property.

[·      ]Both properties accept the **IValueConverter** object.

[·      ]In that converter the **Value** comes as **string** in the convert method.

The following code illustrates customizing the header text for both days namely view header text and the month view header text.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                     |
| [// Assign the IValueConverterClass Object into both days view header text Property and the monthview header text property. ][]                                                                                               |
|                                                                                                                                                                                                                                                                                                                     |
| [Schedule][ schedule = [new] [Schedule]();          ]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                     |
| [DaysHeaderTextConverter][ daysHeaderTextConverter = [new] [DaysHeaderTextConverter](); schedule.DaysHeaderTextConverter = daysHeaderTextConverter;[]] |
|                                                                                                                                                                                                                                                                                                                     |
| [MonthHeaderTextConverter][ monthHeaderTextConverter = [new] [MonthHeaderTextConverter]();]                                                                                    |
|                                                                                                                                                                                                                                                                                                                     |
| [schedule.MonthViewDateTextConverter = monthHeaderTextConverter;]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                     |
| [// IValueConverter Class for DaysHeaderTextConverter][]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                     |
| [  [public] [class] [DaysHeaderTextConverter] : [IValueConverter]]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                     |
| [        [public] [object] Convert([object] value, [Type] targetType, [object] parameter, [CultureInfo] culture)]                           |
|                                                                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [            [object] result = [\"\"];]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                     |
| [            [if] (([string])value == [\"Monday\"])]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"Mon\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Tuesday\"])]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"Tue\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Wednesday\"])]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"Wed\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Thursday\"])]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"Thu\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Friday\"])]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"Fri\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Saturday\"])]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"Sat\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Sunday\"])]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"Sun\"];            ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                     |
| [            [return] result;]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [        [public] [object] ConvertBack([object] value, [Type] targetType, [object] parameter, [CultureInfo] culture)]                       |
|                                                                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [            [throw] [new] [NotImplementedException]();]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [   // IValueConverter Class for MonthHeaderTextConverter][]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                     |
| [    [public] [class] [MonthHeaderTextConverter] : [IValueConverter]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                     |
| [        [public] [object] Convert([object] value, [Type] targetType, [object] parameter, [CultureInfo] culture)]                           |
|                                                                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [            [object] result = [\"\"];]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                     |
| [            [if] (([string])value == [\"Monday\"])]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"MON\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Tuesday\"])]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"TUE\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Wednesday\"])]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"WED\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Thursday\"])]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"THU\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Friday\"])]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"FRI\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Saturday\"])]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"SAT\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [            [else] [if] (([string])value == [\"Sunday\"])]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [                result = [\"SUN\"];            ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                     |
| [            [return] result;]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [        [public] [object] ConvertBack([object] value, [Type] targetType, [object] parameter, [CultureInfo] culture)]                       |
|                                                                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [            [throw] [new] [NotImplementedException]();]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [    }[]]                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The above code results in the following,

{border="0"}

 

Figure 49:DaysHeaderTextConverter

*[]* 

{border="0"}

 

Figure 50: MonthHeaderTextConverter

**[]** 

[]{#related-topics}

