# Data Logging

When Data Logging is enabled (See parameter [`DataLogActive`](../Parameters/#parameter-datalogactive)),
the results of every round gets written to the SD-Card.

The data files are stored in `/log/data` on the SD-Card.

## Data Format
The data is stored as CSV with the following columns:
`time`, `name-of-number`, `raw-value`, `return-value`, `pre-value`, `change-rate`, `change-absolute`, `error-text`, `cnn-digital`, `cnn-analog`