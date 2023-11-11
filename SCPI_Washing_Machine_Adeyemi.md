# Washing Machine

- Detergent Dispensing System
- Water Supply System
- Heating Element
- Motor and Transmission System

|                             |                 |                   |                                                                                                                        |
| --------------------------- | --------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Keyword                     | Parameter Form  | Example           | Comment                                                                                                                |
| DETergent Dispensing:ENABle | {ON\|1\|OFF\|0} | DET:ENAB ON       | Start dispensing the detergent into the washing compartment                                                            |
| DETergent Dispensing:PRESet | {ON\|1\|OFF\|0} | DET:PRES OFF      | Turns off the preset value of the detergent dispensing system                                                          |
| DETergent Dispensing:BLEach | {0...100}       | DET:BLE 45           | Sets the volume of bleach that should be dispensed                                                                     |
|                             |                 |                   |                                                                                                                        |
| WATer Supply:VALVes         | {MIN\|MAX}      | WAT:VALV MIN      | Set the water valve opening to the minimum                                                                             |
| WATer Supply:FILTers        | {DEF}           | WAT:FILT DEF      | Sets the water filtration process to the default value set by the user                                                 |
| WATer Supply:STATe          | {ON\|1\|OFF\|0} | WAT:STAT OFF      | Turns off the water supply so that machine can spin and wash the clothes                                               |
|                             |                 |                   |                                                                                                                        |
| HEATing Element:TEMPerature | {RANGE}         | HEAT:TEMP RANG 40 | It sets the washing machine water heating element temperature to 40 degrees                                            |
| HEATing Element:STAin       | {AUTO}          | HEAT:STA AUTO     | The heating element ensures that the water temperature aligns with the selected wash program for optimal stain removal |
| HEATing Element:LEVel       | {MIN\|MAX}      | HEAT:LEV MAX      | Sets the heatting level of the washing machine to the maximum for the slecected washing option selected by the user    |
|                             |                 |                   |                                                                                                                        |
| MOTor:ROTate                | {INF\|NIN}      | MOT:ROT INF       | Alowa the motor transmission of the washing machine to rotate to the infinite number posible which is set at  9.9 E 37 |
| MOTor:DIRection             | {RIGHT\|LEFT}   | MOT:DIR RIGHT     | Sets the rotation direction of the washing machine motor to Right                                                      |
| MOTor:STATe                 | {ON\|1\|OFF\|0} | MOT:STAT OFF      | This command stops the motor's operation.                                                                              |
