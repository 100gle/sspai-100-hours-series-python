from redbird.repos import CSVFileRepo
from rocketry import Rocketry
from rocketry.log import LogRecord

app = Rocketry(
    execution="async",
    logger_repo=CSVFileRepo(
        filename="task_log.csv",
        model=LogRecord,
    ),
    config={
        'task_pre_exist': 'raise',
        'force_status_from_logs': True,
        'silence_task_prerun': False,
        'silence_task_logging': False,
        'silence_cond_check': False,
        'max_process_count': 5,
        'restarting': 'replace',
        'cycle_sleep': 0.1,
    },
)
