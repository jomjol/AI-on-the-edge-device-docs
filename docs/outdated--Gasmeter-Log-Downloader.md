# Gas Meter Log Downloader

!!! Warning
    This page no longer is maintained!

This small tool downloads the log files from your ESP32 and stores the last value of the day in an *.csv file.

To use this tool you need to **activate the debug log files** in your configuration (Configuration / Debug / Logfile). I go with 30 days of retention in days.

It downloads only the past log files (yesterday and older).

You can define the max. number of log files to download (beginning from newest [yesterday]).

I wrote this tool to get a chart of the daily gas consumption to optimize my gas powered heating.

**Variables to define by yourself:**

- **URL to Log file-Path on Device:** "http://ESP32-IP-Address/fileserver/log/message/"
- **Download Log files to:** enter a valid directory, e.g. "D:\Gaszaehler\Auswertung\Log-Downloads\"
- **Output CSV-File:** enter a valid directory, e.g. "D:\Gaszaehler\Auswertung\DailyValues.csv"
- **Download Log files from past # days:** enter the max. number of log files you want to download (<= your log files retention value in your device configuration)

Feel free to optimize and modify it.
