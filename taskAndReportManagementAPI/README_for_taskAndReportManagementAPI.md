1. Functions completed:
	handle_createPeriodicTask.
		Used to create periodic tasks (weekly or monthly)
		Input Parameters: 
			targets: an array of targets
			task_name: a name string
			periodicType: "week" or "month"
			startTime: example: "12:06"
			end_date: example: "2022-07-07 14:48"
			pause_start: pause start time, example: "05:06"
			pause_end: pause end time, example: "11:08"
			scenario_template: Integer
				1. Full Penetration
				2. Website Penetration
				3. Internal Host Penetration
				4. Weak Credential Exploit
				5. 3rd Party Framework Penetration
				6. Asset Profiling
				7. Ransomware Attack Simulation


	handle_createOneTimeTask:
		Used to create one-time tasks (run now or run once)
		Input Parameters: 
			targets: an array of targets
			task_name: a name string
			periodicType: "week" or "month"
			pending_time: example: "2022-07-25 08:47"
			pause_start: pause start time, example: "05:06"
			pause_end: pause end time, example: "11:08"
			scenario_template: Integer
				1. Full Penetration
				2. Website Penetration
				3. Internal Host Penetration
				4. Weak Credential Exploit
				5. 3rd Party Framework Penetration
				6. Asset Profiling
				7. Ransomware Attack Simulation

	handle_getTaskStatus:
		Get task status
		Input Parameters: 
			task_id: the id of the task
		Return Value: running_status
	
	handle_taskStop:
		Stop a task by id
		Input Parameters: 
			task_id: the id of the task		
	
	handle_taskPause:
		Pause a task by id
		Input Parameters: 
			task_id: the id of the task		
	
	handle_taskInfo:
		Get a task info by id
		Input Parameters: 
			task_id: the id of the task			
		Return value: response data
	
	handle_taskStatistics:
		Get a task statisitcs by id
		Input Parameters: 
			task_id: the id of the task		
		Return value: response data
	
	handle_taskDelete:
		Delete an array of tasks by ids
		Input Parameters: 
			targets: an array of target task ids	
	
	handle_taskClone:
		Clone a task by id
		Input Parameters: 
			task_id: the id of the task

	handle_taskStart:
		Start a task by id
		Input Parameters: 
			task_id: the id of the task
	
	handle_taskRestart:
		Restart a task by id
		Input Parameters: 
			task_id: the id of the task

	handle_generateReport
		Use task_id and report type to generate a report
		Input Parameters: 
			task_id: the id of the task
			reportType: "pdf" or "csv"
			runIteration: whether this is the first time running the task or second time
		Return value: report id
	
	handle_downloadReport
		Download a report by report id
		Input Parameters: 
			report_name: the name you want give to the report 
			report_id: the id of the report
			reportType: "pdf" or "csv"
			folderName: the foldername you want put the report in

2. Functions are packaged in the class RidgeTaskAndReportAPI, which takes RidgeBotAPIURL and RidgeBotAuthToken as input parameters.
				
	

				
			

			
