# Balance on Hand Script
The purpose of this script is to compare two CSVs, "master" and "copy" which
represent inventory manifests from warehouse and SalesForce record.
Script serves to easily and quickly identify differences greater than or equal to
500 items.

- **copy** refers to the `cmls available` report which can be downloaded from [SalesForce](https://fas.my.salesforce.com).
- **master** refers to the `boh report` which can be downloaded from the [GPO RADS reporting system](https://pueblo.gpo.gov/GPODnld.php).

## Requirements
- [Python 3.6](https://python.org) or higher (available through the GSA software catalog).
- `csv` standard Python library.
- Ability to download or clone this repository from GitHub.

## Pro tips
- make sure the item numbers in `master` include leading zeros (0) on projects created in FY16 and later.
- manually remove the first two rows in `master` as their presence is not required and throws the execution of the script.

## Usage
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This project is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
This idea is of [my own](http://about.csethna.com) design and fabrication. It is provided free of charge for use and modification. It is not officially supported by me or anyone else.
