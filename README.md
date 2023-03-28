# pp_cmd_orderby
Postprocessing command "orderby"
## Description
Command sorts rows by given columns 

### Arguments
- columns - positional infinite argument, text, not required. The names of the columns to sort by.
- asc - keyword argument, boolean, not required, default True. Sort ascending vs. descending

### Usage example
```
... | orderBy _time,money,"average effort"
```

```
query: readFile d.csv
         date         A         B         C         D
0  2013-01-01  1.075770 -0.109050  1.643563 -1.469388
1  2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
2  2013-01-03 -1.294524  0.413738  0.276662 -0.472035
3  2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061
4  2013-01-05  0.895717  0.805244 -1.206412  2.565646
```
```
query: readFile d.csv | orderby A, asc=False
         date         A         B         C         D
0  2013-01-01  1.075770 -0.109050  1.643563 -1.469388
4  2013-01-05  0.895717  0.805244 -1.206412  2.565646
1  2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
3  2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061
2  2013-01-03 -1.294524  0.413738  0.276662 -0.472035
```
```
query: readFile d.csv | orderby A
         date         A         B         C         D
2  2013-01-03 -1.294524  0.413738  0.276662 -0.472035
3  2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061
1  2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
4  2013-01-05  0.895717  0.805244 -1.206412  2.565646
0  2013-01-01  1.075770 -0.109050  1.643563 -1.469388

```

## Getting started
### Installing
1. Create virtual environment with post-processing sdk 
```bash
    make dev
```
That command  
- downloads [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates link to current command in postprocessing `pp_cmd` directory 

2. Configure `otl_v1` command. Example:  
```bash
    vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/otl_v1/config.ini
```
Config example:  
```ini
[spark]
base_address = http://localhost
username = admin
password = 12345678

[caching]
# 24 hours in seconds
login_cache_ttl = 86400
# Command syntax defaults
default_request_cache_ttl = 100
default_job_timeout = 100
```

3. Configure storages for `readFile` and `writeFile` commands:  
```bash
   vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/readFile/config.ini
   
```
Config example:  
```ini
[storages]
lookups = /opt/otp/lookups
pp_shared = /opt/otp/shared_storage/persistent
```

### Run orderby
Use `pp` to run orderby command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  orderby 
```
## Deploy
Unpack archive `pp_cmd_orderby` to postprocessing commands directory