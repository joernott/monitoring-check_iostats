# icinga-plugin-check_iostats
This plugin shows the I/O usage of the specified disk, using the iostat external program.
It prints three statistics: Transactions per second (tps), Kilobytes per second
read from the disk (KB_read/s) and and written to the disk (KB_written/s)

## License
BSD 3clause
I did not find any license info on the original files, but various sources, including SuSE
had it as BSD

## Usage
```
/usr/lib64/nagios/plugins/check_iostats:
        -d <disk>               Device to be checked (without the full path, eg. sda)
                                (also accepted are device mapper names)
        -c <tps>,<read>,<wrtn>  Sets the CRITICAL level for tps, KB_read/s and KB_written/s, respectively
        -w <tps>,<read>,<wrtn>  Sets the WARNING level for tps, KB_read/s and KB_written/s, respectively
        -C <percent>     Sets the CRITICAL level for iowait
        -W <percent>     Sets the WARNING level for iowait
                         (if no level is set for iowait, no warning is set for this value)
```
## Changelog  
* Version 0.1 - Nov/2011 Ruediger Oertel ro@suse.de
 - rewrite in perl, no need for external grep, awk, bc
 - add output for iowait
 - implement using device mapper names, e.g. $vg-$lv
* Version 0.0.2 - Jan/2009 Thiago Varela - thiago@iplenix.com
 - added device verification 
