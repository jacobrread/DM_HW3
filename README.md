# Options as a Financial Tool

## Part 1
The average price of each vanilla option varies slightly between runs. The value I got last time I ran it was 9.03667.

## Part 2
For stock1.csv the best fit was a 'lognorm' with the following parameters:
's': 0.02386003772788231, 'loc': -111.12909636088716, 'scale': 210.9681444980447

For stock2-1.csv the best fit was 'chi2' with the following parameters:
'df': 151.15702025584812, 'loc': 49.5410601597393, 'scale': 0.3529476376911609

## Running this program
To run my code for part 1 simply uncomment the Part1() method call at the end of EuropeanMonteCarlo.py and run the python file.

To run my code for part 2 simply uncomment the Part2() method call at the end of EuropeanMonteCarlo.py and run the python file.


### all distributions results
Best for stock1.csv: 
{'dweibull': {'c': 1.3673277264003287, 'loc': 100.44393205651139, 'scale': 4.473217390326258}}

Best for stock2-1.csv: 
{'recipinvgauss': {'mu': 0.007944861329583223, 'loc': 34.301568367779936, 'scale': 0.5407452830600006}}