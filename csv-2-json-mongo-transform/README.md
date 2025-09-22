## Run the test

```
cd csv-2-json-mongo-transform
python -m unittest TestDataProcessor.py -v
```
## Example

**Input**(csv-2-json-mongo-transform-input.tsv)
```
generic_common_keys   ticker    notes     status    securities_name
Ushas                 NSDL      LONG TERM PORTFOLIO STOCK NSDL AT 920 TARGET 1100,1300,1500+ STOP LOSS AT 700 CLOSING BASIS
Ushas                 CCCL      Ushas PENNY STOCK CCCL 25, SL: 22, T1:35, T2:40 Entered   Sharekhan
```

**Output**(Output_Jumbled.tsv)
```
generic_common_keys   ticker    notes     status    securities_name
Ussha	              DLNS	    OLGN RETM ROIPLFOOT OKSCT DLNS TA 029 RTGAET 0001100,135,01+ OTPS LSSO TA 070 CLSNOGI SBSAI
sahsU              	  CCLC	    Uhssa EPNNY KTOSC CCLC 52, LS: 22, 31:5T, 0:2T4 DRENEET   Sehakahnr
```


**Output**(Output.JSON)
```
[
  {
    "created_at_str": "`2025-08-06",
    "generic_common_keys": "Ushas",
    "ticker": "NSDL",
    "notes": "LONG TERM PORTFOLIO STOCK NSDL AT 920 TARGET 1100,1300,1500+ STOP LOSS AT 700 CLOSING BASIS",
    "status": "",
    "cmp": "",
    "entry_price": "",
    "target1": "",
    "target2": "",
    "sl": "",
    "securities_name": "",
    "quantity": "",
    "unrealised_pnl": ""
  },
    {
    "created_at_str": "`2025-09-15",
    "generic_common_keys": "Ushas",
    "ticker": "CCCL",
    "notes": "Ushas PENNY STOCK CCCL 25, SL: 22, T1:35, T2:40",
    "status": "ENTERED",
    "cmp": "25",
    "entry_price": "25.22",
    "target1": "32",
    "target2": "38",
    "sl": "22",
    "securities_name": "Sharekhan",
    "quantity": "800",
    "unrealised_pnl": "5600"
  }
]
```
