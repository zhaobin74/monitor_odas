# ODAS Job Monitor

## How to use

  - First create a jobs.json file with content like

```json
{
  "exps": [ {"name":"exp1", "path":"/path/to/exp1"},
            {"name":"exp2", "path":"/path/to/exp2"}
          ] 

}

``` 
where ```exp1``` and ```exp2``` are names of the experiment to be monitored; ```"path"``` refers the directory where ```gcm_run.j``` resides

  - Execute the command below with python3

```csh

python -u ./monitor.py >& job-`date +%g%m%d-%H%M%S`.log &

```

  - Above command puts the monitor process in background. To stop the process, either delete ```jobs.json``` file or rename it.

