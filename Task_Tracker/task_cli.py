#!/usr/bin/python3
import datetime
import argparse
import os
import json


def main():
  path="task_list.json"
  task_list=load_json_file(path)
  command,args=register_and_get_arguments()
  try:
    command(task_list,**args)
    save_json_file(path,task_list)
  except Exception as e:
    print(f"error occurs: {e}")
  

def register_and_get_arguments():
  parser=argparse.ArgumentParser(description="commands")
  subparsers=parser.add_subparsers(dest='command',title='command',required=True)
  
  subqueries={"add":{"call":add_task,"help":"add new task","args":["desc"]},"update":{"call":update_task,"help":"update description of a task","args":["id","desc"]},"delete":{"call":delete_task,"help":"delete a task","args":["id"]},"mark-in-progress":{"call":mark_in_progress,"help":"change status of a task in-progress","args":["id"]},"mark-done":{"call":mark_done,"help":"change status of a task done","args":["id"]},"list":{"call":list_task,"help":"print list of tasks","args":["status"],"choices":["in-progress","done","todo"]}}
  
  for key,value in subqueries.items():
    p=subparsers.add_parser(key,help=value['help'])
    for arg in value['args']:
      if 'choices' in value:  # Optional argument (flag)
          p.add_argument(arg, help=f"Specify {arg[2:]}", choices=value['choices'],nargs='?')
      else:  # Positional argument
          p.add_argument(arg, help=f"Provide value for {arg}")
  args_dict=vars(parser.parse_args())
  command=subqueries[args_dict.pop('command')]['call']
  return command,args_dict
  

def load_json_file(path):
  try:
    with open(path) as f:
      task_list=json.load(f)
  except Exception as e:
    task_list={}
  finally:
    return task_list
  
def save_json_file(path,task_list):
  with open(path,'w') as f:
    json.dump(task_list,f,indent=4)
      
      
def add_task(dict_list,desc):
  try:
    createdAt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updatedAt=createdAt
    status="todo"
    cur_id=int(max("0",*dict_list.keys()))+1
    dict_list[cur_id]={"id":cur_id,"description":desc,"status":status,"createdAt":createdAt,"updatedAt":updatedAt}
    print(f'Task added successfully (ID: {cur_id})')
  except Exception as e:
    print(f"Failed to add task: {e}")

def update_task(dict_list,id,desc):
  try:
    task=dict_list[id]
    task["description"]=desc
    task["updatedAt"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dict_list[id]=task
    print(f'Task updated successfully (ID: {id})')
  except Exception as e:
    print(f"Failed to update task: {e}")

def delete_task(dict_list,id):
  try:
    if id in dict_list: del dict_list[id]
    print(f'Task deleted successfully (ID: {id})')
  except Exception as e:
    print(f"Failed to delete task: {e}")

def mark_in_progress(dict_list,id):
  try:
    task=dict_list[id]
    task["status"]="in-progress"
    task["updatedAt"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dict_list[id]=task
    print(f'Task updated successfully (ID: {id})')
  except Exception as e:
    print(f"Failed to update task: {e}")
    
def mark_done(dict_list,id):
  try:
    task=dict_list[id]
    task["status"]="done"
    task["updatedAt"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dict_list[id]=task
    print(f'Task updated successfully (ID: {id})')
  except Exception as e:
    print(f"Failed to update task: {e}")

def list_task(dict_list,status=None):
  for v in dict_list.values():
      if status==None or v["status"]==status.lower():
        print(f"{v['id']} {v['status']} {v['createdAt']} {v['updatedAt']} {v['description']}")
        
        
def __init__():
  main()