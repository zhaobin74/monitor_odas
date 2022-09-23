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
  - Execute the command below with python3

```csh

python -u ./monitor.py >& job-`date +%g%m%d-%H%M%S`.log &

```

