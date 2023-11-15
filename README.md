# NxNxN-Cubes
A simulation of **ANY** NxNxN Rubik’s Cube, using standard cubing notation.

## Notation:

| **Command** | **Description** |
| :---: | :---- |
| `HELP` | Shows list of commands. |
| `EXIT` | Terminates program. |
| `RESET` | Resets cube to solved state. |
| `RESIZE` | Changes size of cube. |
| `HISTORY` | Shows past moves. |
| `CLEAR` | Clears past moves. |

| **Command** | **Description** |
| :---: | :---- |
| `U` | Turns top layer 90° clockwise. |
| `D` | Turns bottom layer 90° clockwise. |
| `F` | Turns front layer 90° clockwise. |
| `B` | Turns back layer 90° clockwise. |
| `R` | Turns right layer 90° clockwise. |
| `L` | Turns left layer 90° clockwise. |
| `U'` | Turns top layer 90° counterclockwise. |
| `U2` | Turns top layer 180°. |
| `#U` | Turns `#`th layer from the top 90° clockwise, relative to top layer. |
| `Uw` | Turns top two layers 90° clockwise. |
| `#Uw` | Turns top `#` layers 90° clockwise. |

| **Command** | **Description** |
| :---: | :---- |
| `X` | Rotates entire cube 90° clockwise, relative to left layer. |
| `Y` | Rotates entire cube 90° clockwise, relative to top layer. |
| `Z` | Rotates entire cube 90° clockwise, relative to front layer. |
| `X'` | Rotates entire cube 90° counterclockwise, relative to left layer. |
| `X2` | Rotates entire cube 180°, relative to left layer. |

| **Command** | **Description** |
| :---: | :---- |
| `U F` | Turns top layer 90° clockwise, then turns front layer 90° clockwise. |
| `(…)` | Same as `…`. |
| `(…)#` | Runs through `…` a total of `#` times. |
| `​` | Runs most recent moves again. |
| `name = …` | Defines `name` as alias for `…`. |
| `name` | Runs algorithm that `name` is alias of. |
| `? name` | Shows algorithm that `name` is alias of. |

### Slicing:

As this is a generalized NxN cube simulation, the 3x3-specific `M`, `S`, and `E` moves are not included. However, there is a simple way to include them without changing the code:

```
>> M = 2L
>> S = 2F
>> E = 2U
```

You can also add on to it:

```
>> M' = 2L'
>> M2 = 2L2
>> S' = 2F'
>> S2 = 2F2
>> E' = 2U'
>> E2 = 2U2
```