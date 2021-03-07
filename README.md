# hw1
(1)
首先將csv檔案的內容讀取進來並轉為Python的dictionary格式
把每一列轉成一個dictionary並append至data的陣列
利用範例code的方法先濾掉TEMP==-99和TEMP==-999的資料
再利用同樣的方法抓出station_id為 "C0A880" "C0F9A0" "C0G640" "C0R190" "C0X260" 該列的資料並存進target_data中
由於只有五個station_id，所以就先把id按照lexicographical order建立一個二維陣列
該二維陣列的第一列為排序後的id，第二列全部都先設為預設的-1
接下來traverse target_data把同個id的TEMP去做比較，將比較大的值存進二維陣列中適當的位置
最後traverse儲存結果的二維陣列，若該id的對應值人的對應值仍為-1則把-1的結果改為存None進去
最後輸出結果
(2)

