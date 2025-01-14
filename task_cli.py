import sys 
import json 
import os 
from datetime import datetime

#Define qual arquivo ira armazenar as tarefas

TASKS_FILE = "tasks.json"

#inicializa o arquivo caso nao exista

def initialize_tasks_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            json.dump([],file)

#le as tarefas no arquivo

def load_tasks():
    with open(TASKS_FILE, "r") as file:
        return json.load(file)
    
#salva as tarefas no arquivo 

def save_tasks(tasks):
    with open(TASKS_FILE, w) as file:
        json.dump(tasks, file, indent=4)

#adiciona uma nova tarefa

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "descripition": description,
        "status": "todo",
        "createAt": datetime.now().isoformat(),
        "updateAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarefa adiciona com Sucesso (ID: {new_task['id']})")
                                                       

#atualiza a descricao da tarefa

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] == new_description
            task["updateAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"tarefa {task_id} atualizada com sucesso")
            return
    print(f"Tarefa com ID {task_id} não encontrada")

#exclui uma tarefa

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task ["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        print(f"Tarefa com ID {task_id} não encontrada")
    else:
        save_tasks(updated_tasks)
        print(f"Tarefa {task_id} excluida com sucesso")


#Altera o estado de uma tarefa

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updateAt"] = datetime.now().isofornat()
            save_tasks(tasks)
            print(f"Tarefa {task_id} marcada como {status}")
            return
    print(f"Tarefa com ID {task_id} não encontrada")

#Lista de tarefas

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    if tasks: 
        for task in tasks:
            print(f"[{task['id']}] {task['description'] - {task['status']}} (Criada em {task ['createdAt']})")
    else: 
        print("Nenhuma tarefa encontrada")   

#funcao principal para interpretar os comandos da CLI

def main():
    initialize_tasks_file()

    if len(sus.argv) < 2:
        print("Uso: task-cli <comando> [argumentos]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 4:
            print("Uso: task-cli update <id> <nova descricao>")
        else:
            add_task(" ".join(sys.argv[2:]))

    elif command == "update":
        if len(sys.argv) < 4:
            print("Uso: task-cli update <id> <nova descricao>")
        else:
            update_task(int(sys.argv[2]), "".join(sys.argv[3:]))

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Uso: task-cli delete <id>")
        else:
            delete_task(int(sys.argv[2]))


    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Uso: task-cli mark in-progress <id>")
        else:
            mark_tasks(int(sys.argv[2]), "in progress")

    elif command == "mark-done":
        if len(sys.argv) < 2:
            print("uso: task-cli mark-done <id>")
        else:
            mark_task(int(sys.argv[2], "done"))
                      
    elif command == "list":
        if len(sys.argv) < 3:
            list_tasks()
        else:
            list_tasks(sys.argv[2])

    else:
        print(f"comando desconhecido {command}")

    if __name__ == "__main__":
        main()    

    





                                                       
                            
        


    


