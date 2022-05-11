G1 X-0.480 Y577.600 Z300.00
T0

S16000

M03 =
$ANOUT[1] = 0.75
WAIT SEC 1
$OUT[94] = TRUE
WAIT SEC 8

M05=
$OUT[94] = FALSE
$ANOUT[1] = 0



G4 P60000
M05

ANOUT 0.75

130 inches min
55mm/s

M03 

M_RunCode(%1)
M_RunCode(%3)


If %1 = 3 then
    $ANOUT[1] = 0.75
    WAIT SEC 1
    $OUT[94] = TRUE
    WAIT SEC 8
Elseif %1 = 5 then
    $OUT[94] = FALSE
    $ANOUT[1] = 0
