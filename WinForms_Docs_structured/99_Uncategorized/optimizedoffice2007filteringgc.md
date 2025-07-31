---
title: optimizedoffice2007filteringgc.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\optimizedoffice2007filteringgc.md
created_at: 2025-07-03
---






#### Optimized Office2007Filter in GGC {#optimized-office2007filter-in-ggc style="tab-stops: 0pt"}

**Use Case Scenarios**

If the Office2007Filter is used in a WF GridGroupingControl where the columns have a large number of unique items (say 5000 or 10000 unique items), the grid is unusable (hanged). To improve the performance, the new optimized Office2007Filter can be used.

 

**Methods**


  **[Method ]**[]   **[Description ]**[]   **[Parameters ]**[]   **[Type ]**[]   **[Return Type ]**[]
  ------------------------------------------------------------- ------------------------------------------------------------------ ----------------------------------------------------------------- ----------------------------------------------------------- ------------------------------------------------------------------
  WireGrid                                                      Wires grid with filter.                                            this.gridGroupingControl1 (control as argument)                    Method                                                      void
  UnWireGrid                                                    Unwire grid with filter.                                           this.gridGroupingControl1 (control as argument)                    Method                                                      void


Sample Link

To view a sample:

[·      ]Open **Syncfusion Dashboard.**

[·      ]Select **UI \> Windows Forms**.

[·      ]Click **Run Samples**. 

[·      ]Navigate to **GridGrouping Samples \> Filters and Expressions \> Optimized Excel Filter Demo**

**[]** 

Implementing optimized Office2007Filter to GGC

Set **AllowFilter** to **True** when the Grid control is wired with the GridOffice2007Filter to enable Excel-like filtering in the grid filter bar.

The following code illustrates how to add the Excel-like filter to the grid filter bar:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [GridExcelFilter][ filter;][]                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [         ][private][ ][void][ showFilter_CheckedChanged(][object][ sender, ][EventArgs][ e)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            ][this][.gridGroupingControl1.TableDescriptor.Columns\[0\].AllowFilter = ][true][;]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            ][if][ (][this][.showFilter.Checked)]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            {]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                filter.WireGrid(][this][.gridGroupingControl1);]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            }]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            ][else][]                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            {]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                filter.UnWireGrid(][this][.gridGroupingControl1);]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            }]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                         |
| [Private][ filter [As] GridExcelFilter]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                         |
| [             [Private] [Sub] showFilter_CheckedChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                         |
| [                  [Me].gridGroupingControl1.TableDescriptor.Columns(0).AllowFilter = [True]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                         |
| [                  [If] [Me].showFilter.Checked [Then]]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                         |
| [                        filter.WireGrid([Me].gridGroupingControl1)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                         |
| [                  [Else]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [                        filter.UnWireGrid([Me].gridGroupingControl1)]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
| [                  [End] [If]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [             [End] [Sub]]                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

 

[]{#related-topics}

