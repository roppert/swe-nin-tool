# Swedish National Identification Number Tool

Creates a valid national identification number for
Sweden (personal identity number, called personnummer in swedish)

 * http://sv.wikipedia.org/wiki/Personnummer_i_Sverige
 * http://en.wikipedia.org/wiki/Personal_identity_number_%28Sweden%29

## Example Usage

If no argument is given a random number will be generated. If a date
of birth, in form yyyymmdd, is supplied as argument it will be used.
If birth number is supplied it will be used insted of generating one.

    $ python swenin.py
    19750622-8233
    $ python swenin.py 19860606
    19860606-2423
    $ python swnin.py 19860606-242
    19860606-2423
    $ python swnin.py 19860606-242x
    19860606-2423
