VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Sheet1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True


Sub Stock()

    ' declare vars
    'Dim i As Long
    'Dim j As Long
    'Dim total_volume As Long
    'Dim vol As Long
    
    
    
    ' open price on first row
    'closing price on last row
    Dim startPrice As Double
    Dim closePrice As Double
    Dim yearlyChange As Double
    Dim percentChange As Double
    
    
    Dim currStock As String
    Dim nextStock As String
    Dim summaryRow As Double
    Dim ws As Worksheet
    
    For Each ws In ThisWorkbook.Worksheets
    
    
    'summary of summary table
    Dim greatestIncrease As Double
    Dim greatestIncreasestock As Double
    
    Dim greatestDecrease As Double
    Dim greatestDecreasestock As Double
    
    Dim greatestVolume As Double
    Dim greatestVolumestock As Double
    
    ' assign
    total_volume = 0
    summaryRow = 2
    startPrice = ws.Cells(2, 3).Value
    
    'default to compare
    greatestIncreasestock = -99999999999#
    greatestDecreasestock = 1E+17
    greatestVolume = -99999999999#
  
  
  'column headers
    ws.Cells(1, 12).Value = "Ticker"
    ws.Cells(1, 13).Value = "Yearly Change"
    ws.Cells(1, 14).Value = "Percent Change"
    ws.Cells(1, 15).Value = "Total Stock Volume"
    
   
      
    
    
    'bold font, cite https://learn.microsoft.com/en-us/office/vba/api/excel.font.bold
    
    Worksheets("A").Range("L1:O1").Font.Bold = True
    Worksheets("A").Range("r2:r4").Font.Bold = True
    
    
    
    'do work
    For i = 2 To 22771
    
        currStock = ws.Cells(i, 1).Value
        nextStock = ws.Cells(i + 1, 1).Value
        
        ' add to total
        vol = ws.Cells(i, 7).Value
        total_volume = total_volume + vol
    
        If currStock <> nextStock Then
            'get the closing price
            closePrice = ws.Cells(i, 6).Value
            yearlyChange = closePrice - startPrice
            
            'error checking
            If startPrice = 0 Then
                percentChange = 0
            Else
            percentChange = yearlyChange / startPrice
            End If
                        
            
'write the output

            ws.Cells(summaryRow, 12).Value = currStock
            ws.Cells(summaryRow, 13).Value = yearlyChange
            ws.Cells(summaryRow, 14).Value = percentChange
            ws.Cells(summaryRow, 15).Value = total_volume
            
            'conditional formatting
           If yearlyChange < 0 Then
               ws.Cells(summaryRow, 13).Interior.ColorIndex = 3
            Else
                ws.Cells(summaryRow, 13).Interior.ColorIndex = 4
                
            End If
                                
            
            ' reset
            total_volume = 0
            startPrice = ws.Cells(i + 1, 3).Value
            
        'increment the summary table row
        summaryRow = summaryRow + 1
        End If
          
    Next i
                  
    'For j = 2 To summaryRow
   
        'If Cells(j, 14).Value > greatestIncrease Then
        ' greatestIncrease = Cells(j, 14).Value
         'greatestIncreasestock = Cells(j, 12).Value
       ' End If
             'If Cells(j, 14).Value < greatestDecrease Then
         'greatestDecrease = Cells(j, 14).Value
         'greatestDecreasestock = Cells(j, 12).Value
       ' End If
                 
     ' If Cells(j, 15).Value > greatestVolume Then
        'greatestVolume = Cells(j, 15).Value
         'greatestVolumestock = Cells(j, 12).Value
     'End If
     
     
    'Next j
    
     'Row labels
    ws.Cells(2, 18).Value = "GREATES%Increase"
    ws.Cells(3, 18).Value = "Greatest%Decrease"
    ws.Cells(4, 18).Value = "Greatest Total Volume"
    
    Next ws
    

End Sub

 




'show the output

