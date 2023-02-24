# Options as a Financial Tool

## Part 1
The average price of each vanilla option varies slightly between runs. The value I got last time I ran it was 9.03667.

## Part 2
For stock1.csv the best fit was a 'lognorm' with the following parameters:
's': 0.02386003772788231, 'loc': -111.12909636088716, 'scale': 210.9681444980447

For stock2-1.csv the best fit was 'chi2' with the following parameters:
'df': 151.15702025584812, 'loc': 49.5410601597393, 'scale': 0.3529476376911609

"Second, find the option price for the asset in Part 1 if the value is determined by outperforming the average value of the two options."
* After a few runs this is the result I got: The most competitive option is Stock2-1 with a price of 10.289150684931508

"Compute again for outperforming the max value of either of the two options. (Assume the same 1-year window of expiry)"
* After a few runs this is the result I got: The most competitive option is based on the max is Stock2-1 with a price of 12.2

## Running this program
To run my code for part 1 simply uncomment the Part1() method call at the end of EuropeanMonteCarlo.py and run the python file.

To run my code for part 2 simply uncomment the Part2() method call at the end of EuropeanMonteCarlo.py and run the python file.
