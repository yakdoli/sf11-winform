---
title: highfrequencyupdates1.md
original_path: WinForms_Docs/99_Uncategorized/highfrequencyupdates1.md
created_at: 2025-08-05
---






#### High Frequency Updates {#high-frequency-updates style="tab-stops: 0pt"}

This section illustrates an example that let you know how to handle high frequency updates using grid while keeping the CPU usage at a minimum level. It uses a simple data source with few double-valued columns. It changes random cell values and also does record insertions and removals, using a timer event.

 

The following code illustrates changing of random cell values:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [private][ [void] timer_Tick([object] sender, [EventArgs] e)]           |
|                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [\...\...\...\...\...\.....]                                                                                                                                                               |
|                                                                                                                                                                                                                                |
| [for][ ([int] i = 0; i \< numberOfChangesEachTimer; i++)]                                                            |
|                                                                                                                                                                                                                                |
| [            {]                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [                [int] recNum = rand.Next(table.Rows.Count - 1);]                                                                                                     |
|                                                                                                                                                                                                                                |
| [                [int] col = rand.Next(table.Columns.Count - 1) + 1;]                                                                                                 |
|                                                                                                                                                                                                                                |
| [                [DataRow] drow = table.Rows\[recNum\];]                                                                                                           |
|                                                                                                                                                                                                                                |
| [                [if] (drow.RowState != [DataRowState].Deleted && !(drow\[col\] [is] [DBNull]))] |
|                                                                                                                                                                                                                                |
| [                {]                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [                    [double] value = ([int])([Convert].ToDouble(drow\[col\]) \* (rand.Next(50) / 100.0f + 0.8));]       |
|                                                                                                                                                                                                                                |
| [                    [//Console.WriteLine(\"{0}, {1}: {2}\", recNum, col, value);]]                                                                                  |
|                                                                                                                                                                                                                                |
| [                    drow\[col\] = value;]                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [                }]                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [           }]                                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code illustrates record insertions and removals:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                           |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [private][ [void] timer_Tick([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                      |
|                                                                                                                                                                                                                      |
| [\...\...\...\...\...\.....]                                                                                                                                                     |
|                                                                                                                                                                                                                      |
| [if][ (toggleInsertRemove \> 0 && (timerCount % insertRemoveModulus) == 0)]                                                     |
|                                                                                                                                                                                                                      |
| [            {]                                                                                                                                                                  |
|                                                                                                                                                                                                                      |
| [                icount = ++icount % (toggleInsertRemove \* 2);]                                                                                                                 |
|                                                                                                                                                                                                                      |
| [                shouldInsert = icount \< toggleInsertRemove;]                                                                                                                   |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [                [if] (shouldInsert)]                                                                                                                       |
|                                                                                                                                                                                                                      |
| [                {]                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [                    [for] ([int] ri = 0; ri \< insertRemoveCount; ri++)]                                                              |
|                                                                                                                                                                                                                      |
| [                    {]                                                                                                                                                          |
|                                                                                                                                                                                                                      |
| [                        [int] recNum = rand.Next([Math].Min(30, table.Rows.Count));]                                               |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [                        [double] next = rand.Next(100);]                                                                                                   |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [                        [object]\[\] values = [new] [object]\[table.Columns.Count\];]                            |
|                                                                                                                                                                                                                      |
| [                        values\[0\] = [\"H\"] + ti.ToString([\"00000\"]);]                                                      |
|                                                                                                                                                                                                                      |
| [                        [for] ([int] n = 1; n \< table.Columns.Count; n++)]                                                           |
|                                                                                                                                                                                                                      |
| [                            values\[n\] = next + n;]                                                                                                                            |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [                        [DataRow] drow = table.NewRow();]                                                                                               |
|                                                                                                                                                                                                                      |
| [                        drow.ItemArray = values;]                                                                                                                               |
|                                                                                                                                                                                                                      |
| [                        table.Rows.InsertAt(drow, recNum);]                                                                                                                     |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [                        ti++;]                                                                                                                                                  |
|                                                                                                                                                                                                                      |
| [                    }]                                                                                                                                                          |
|                                                                                                                                                                                                                      |
| [                }]                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [                [else]]                                                                                                                                    |
|                                                                                                                                                                                                                      |
| [                {]                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [                    [for] ([int] ri = 0; ri \< insertRemoveCount; ri++)]                                                              |
|                                                                                                                                                                                                                      |
| [                    {]                                                                                                                                                          |
|                                                                                                                                                                                                                      |
| [                        [int] recNum = 5; [//rand.Next(m_set.Count - 1);]]                                                           |
|                                                                                                                                                                                                                      |
| [                        [int] rowNum = recNum + 1;]                                                                                                        |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [                        [// Underlying data structure (this could be a data table or whatever structure]]                                                 |
|                                                                                                                                                                                                                      |
| [                        [// you use behind a virtual grid).]]                                                                                             |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [                        [if] (table.Rows.Count \> 10)]                                                                                                     |
|                                                                                                                                                                                                                      |
| [                            table.Rows.RemoveAt(recNum);]                                                                                                                       |
|                                                                                                                                                                                                                      |
| [                    }]                                                                                                                                                          |
|                                                                                                                                                                                                                      |
| [                }]                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [            }]                                                                                                                                                                  |
|                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: For complete code of this example, refer the following browser sample:


 

\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\ Samples\\3.5\\WindowsSamples\\Grid Data Control -- Advanced\\Trader Grid Test Demo

 

 

[]{#related-topics}

